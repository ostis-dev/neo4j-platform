grammar scs;

content: ('_')? CONTENT_BODY;

contour
	@init {count = 1}:
	CONTOUR_BEGIN {count > 0}? (sentence_wrap*) CONTOUR_END {
count -= 1
if count == 0:
    pass
    };

connector
	returns[str symbol]:
	c = (
		'<>'
		| '>'
		| '<'
		| '..>'
		| '<..'
		| '->'
		| '<-'
		| '<=>'
		| '=>'
		| '<='
		| '-|>'
		| '<|-'
		| '-/>'
		| '</-'
		| '~>'
		| '<~'
		| '~|>'
		| '<|~'
		| '~/>'
		| '</~'
		| '_<>'
		| '_>'
		| '_<'
		| '_..>'
		| '_<..'
		| '_->'
		| '_<-'
		| '_<=>'
		| '_=>'
		| '_<='
		| '_-|>'
		| '_<|-'
		| '_-/>'
		| '_</-'
		| '_~>'
		| '_<~'
		| '_~|>'
		| '_<|~'
		| '_~/>'
		| '_</~'
	) {$ctx.symbol = $c.text};

// ------------- Rules --------------------

syntax: sentence_wrap* EOF;

sentence_wrap: (sentence ';;');

sentence: sentence_lvl1 | sentence_assign | sentence_lvl_common;

ifdf_alias: ALIAS_SYMBOLS;

idtf_system: ID_SYSTEM | '...' | idtf_lvl1_preffix;

sentence_assign: ALIAS_SYMBOLS '=' idtf_common;

idtf_lvl1_preffix: 'sc_node' | 'sc_link' | 'sc_edge' | 'sc_arc';

idtf_lvl1_value
	returns[Element el]:
	t = idtf_lvl1_preffix '#' i = ID_SYSTEM {
$ctx.el = self._impl._processIdtfLevel1($t.text, $i.text)
};

idtf_lvl1
	returns[Element el]:
	idtf_lvl1_value {
$ctx.el = $idtf_lvl1_value.el
};

idtf_edge: '(' idtf_atomic connector attr_list? idtf_atomic ')';

idtf_set:
	'{' attr_list? idtf_common (';' attr_list? idtf_common)* '}';

idtf_atomic: ifdf_alias | idtf_system;

idtf_url: LINK;

idtf_common:
	idtf_atomic
	| idtf_edge
	| idtf_set
	| contour
	| content
	| idtf_url;

idtf_list:
	idtf_common internal_sentence_list? (
		';' i2 = idtf_common internal_sentence_list?
	)*;

internal_sentence: connector attr_list? idtf_list;

internal_sentence_list: '(*' (internal_sentence ';;')+ '*)';

sentence_lvl1:
	src = idtf_lvl1 '|' edge = idtf_lvl1 '|' trg = idtf_lvl1 {
self._impl.append_triple($src.el, $edge.el, $trg.el)
};

sentence_lvl_4_list_item: connector attr_list? idtf_list;

sentence_lvl_common:
	idtf_common sentence_lvl_4_list_item (
		';' sentence_lvl_4_list_item
	)*;

attr_list: (ID_SYSTEM EDGE_ATTR)+;

// ----------------------------
ID_SYSTEM: ('a' ..'z' | 'A' ..'Z' | '_' | '.' | '0' ..'9')+;

ALIAS_SYMBOLS:
	'@' ('a' ..'z' | 'A' ..'Z' | '_' | '0' ..'9')+;

fragment CONTENT_ESCAPED: '\\' ('[' | ']' | '\\');

fragment CONTENT_SYBMOL: (CONTENT_ESCAPED | ~('[' | ']' | '\\'));

fragment CONTENT_SYBMOL_FIRST_END: (
		CONTENT_ESCAPED
		| ~('[' | ']' | '\\' | '*')
	);

CONTOUR_BEGIN: '[*';

CONTOUR_END: '*]';

CONTENT_BODY:
	'[]'
	| '[' CONTENT_SYBMOL_FIRST_END CONTENT_SYBMOL* ']';

LINK: '"' (~('"') | '\\"')* '"';

EDGE_ATTR: ':' | '::';

LINE_TERMINATOR: [\r\n\u2028\u2029] -> channel(HIDDEN);

LINE_COMMENT:
	'//' ~('\n' | '\r')* '\r'? '\n' -> channel(HIDDEN);

MULTINE_COMMENT: '/*' .*? '*/' -> channel(HIDDEN);

WS: ( ' ' | '\t' | '\r' | '\n') -> channel(HIDDEN);