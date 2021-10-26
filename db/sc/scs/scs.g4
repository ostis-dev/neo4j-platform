grammar scs;

@parser::header {
from sc.scs.types import *

def create_token_context(ctx: any) -> TokenContext:
	return TokenContext(line=ctx.line, column=ctx.column, text=ctx.text)
}

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

ifdf_alias
	returns[Element el]:
	ALIAS_SYMBOLS {
$ctx.el = self._impl.create_alias(create_token_context($ALIAS_SYMBOLS))
};

idtf_system
	returns[Element el]:
	value = (ID_SYSTEM | '...') {
$ctx.el = create_token_context($value)
};

sentence_assign:
	ALIAS_SYMBOLS '=' idtf_common {

context = create_token_context($ALIAS_SYMBOLS)
self._impl.define_alias(self._impl.create_alias(context), $idtf_common.el)
};

idtf_lvl1_preffix
	returns[context]:
	value = ('sc_node' | 'sc_link' | 'sc_edge' | 'sc_arc') {
$ctx.context = create_token_context($value)
};

idtf_lvl1_value
	returns[el]:
	t = idtf_lvl1_preffix '#' i = ID_SYSTEM {
context = $t.context
context._length += 1 + len($i.text)
$ctx.el = self._impl._processIdtfLevel1(context, $t.text, $i.text)
};

idtf_lvl1
	returns[el]:
	idtf_lvl1_value {
$ctx.el = $idtf_lvl1_value.el
};

idtf_edge: '(' idtf_atomic connector attr_list? idtf_atomic ')';

idtf_set:
	'{' attr_list? idtf_common (';' attr_list? idtf_common)* '}';

idtf_atomic
	returns[Element el]:
	ifdf_alias {$ctx.el = $ifdf_alias.el}
	| idtf_system {$ctx.el = $idtf_system.el};

idtf_url: LINK;

idtf_common
	returns[Element el]:
	idtf_atomic {$ctx.el = $idtf_atomic.el}
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