grammar scs;

options {
	language = Python3;
}

@parser::header {
from sc.scs.types import *
from enum import Enum

def create_token_context(ctx: any) -> TokenContext:
	return TokenContext(line=ctx.line, column=ctx.column, text=ctx.text)

class ConnectorType:
	ARC = 0
	EDGE = 1
}

content
	returns[Element el]: (v='_')? CONTENT_BODY {
token_context = create_token_context($CONTENT_BODY)
$ctx.el = self._impl.create_link(token_context, $CONTENT_BODY.text[1:-1], Link.Type.STRING, $v is not None)
};

contour returns[Element el]
	@init {count = 1}:
	CONTOUR_BEGIN {count > 0}? {self._impl.start_contour()} (sentence_wrap*) CONTOUR_END {
count -= 1
if count == 0:
	contour = self._impl.create_node(create_token_context($CONTOUR_BEGIN))
	self._impl.end_contour(contour)
	$ctx.el = contour
};

connector_edge
	returns[Element el]:
	symbol = (
		'<>'
		| '<=>'
		| '_<>'
		| '_<=>'
		| '>'
		| '<'
		| '=>'
		| '<='
		| '_=>'
		| '_<='
	) {$ctx.el = self._impl.create_edge(create_token_context($symbol), $symbol.text)};

connector_arc
	returns[Element el]:
	symbol = (
		'..>'
		| '<..'
		| '->'
		| '<-'
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
		| '_..>'
		| '_<..'
		| '_->'
		| '_<-'
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
	) {$ctx.el = self._impl.create_arc(create_token_context($symbol), $symbol.text)};

connector
	returns[Element el]:
	connector_edge {$ctx.el = $connector_edge.el}
	| connector_arc {$ctx.el = $connector_arc.el};

// ------------- Rules --------------------

syntax: sentence_wrap* EOF;

sentence_wrap: (sentence SENTENCE_SEP);

sentence: sentence_assign | sentence_lvl_common;

ifdf_alias
	returns[Element el]:
	ALIAS_SYMBOLS {
$ctx.el = self._impl.create_alias(create_token_context($ALIAS_SYMBOLS))
};

idtf_system
	returns[Element el]:
	value = (ID_SYSTEM | '...') {
$ctx.el = self._impl.create_node(create_token_context($value))
};

sentence_assign:
	ALIAS_SYMBOLS '=' idtf_common {

context = create_token_context($ALIAS_SYMBOLS)
self._impl.define_alias(self._impl.create_alias(context), $idtf_common.el)
};

idtf_edge
	returns[Elemen el]:
	'(' src = idtf_atomic connector attr = attr_list? trg = idtf_atomic ')' {
self._impl.append_triple($src.el, $connector.el, $trg.el)
$ctx.el = $connector.el

if $ctx.attr is not None:
	for a, e in $attr.items:
		self._impl.append_triple(a, e, $connector.el)
};

idtf_set_item[Element set]:
	attr = attr_list? idtf = idtf_common {
edge = self._impl.create_arc($idtf.el.ctx.clone(), '->')
self._impl.append_triple($set, edge, $idtf.el)
if $ctx.attr is not None:
	for a, e in $attr.items:
		self._impl.append_triple(a, e, edge)
};

idtf_set_item_list[Element set]:
	idtf_set_item[set] (';' idtf_set_item[set])*;

idtf_set
	returns[Element el]:
	t = '{' {
context = create_token_context($t)
$ctx.el = self._impl.create_node(context)
	} idtf_set_item_list[$ctx.el] '}';

idtf_atomic
	returns[Element el]:
	ifdf_alias {$ctx.el = $ifdf_alias.el}
	| idtf_system {$ctx.el = $idtf_system.el};

idtf_url
	returns[Element el]:
	LINK {
context = create_token_context($LINK)
$ctx.el = self._impl.create_link(context, $LINK.text[1:-1], Link.Type.URL, False)
};

idtf_common
	returns[Element el]:
	idtf_atomic {$ctx.el = $idtf_atomic.el}
	| idtf_edge {$ctx.el = $idtf_edge.el}
	| idtf_set {$ctx.el = $idtf_set.el}
	| contour {$ctx.el = $contour.el}
	| content {$ctx.el = $content.el}
	| idtf_url {$ctx.el = $idtf_url.el};

idtf_list
	returns[items]
	@init {$ctx.items = []}:
	first = idtf_common {$ctx.items.append($first.el)} internal_sentence_list[$first.el]? (
		';' second = idtf_common {$ctx.items.append($second.el)} internal_sentence_list[$first.el]?
	)*;

internal_sentence[Element src]:
	c = connector attr = attr_list? target = idtf_list {

for t in $target.items:
	edge = None
	if isinstance($c.el, Edge):
		edge = self._impl.create_edge($c.el.ctx, $c.el.connector)
	else:
		edge = self._impl.create_arc($c.el.ctx, $c.el.connector)
	self._impl.append_triple($src, edge, t)
	if $ctx.attr is not None:
		for a, e in $attr.items:
			self._impl.append_triple(a, e, edge)

};

internal_sentence_list[Element src]:
	'(*' (internal_sentence[src] SENTENCE_SEP)+ '*)';

sentence_lvl_4_list_item[Element src]:
	(c = connector attr = attr_list? target = idtf_list) {
for t in $target.items:
	edge = None
	if isinstance($c.el, Edge):
		edge = self._impl.create_edge($c.el.ctx, $c.el.connector)
	else:
		edge = self._impl.create_arc($c.el.ctx, $c.el.connector)

	self._impl.append_triple($src, edge, t)
	if $ctx.attr is not None:
		for a, e in $attr.items:
			self._impl.append_triple(a, e, edge)
};

sentence_lvl_common:
	idtf_common sentence_lvl_4_list_item[$idtf_common.el] (
		';' sentence_lvl_4_list_item[$idtf_common.el]
	)*;

attr_list
	returns[items]
	@init {$ctx.items = []}: (
		ID_SYSTEM EDGE_ATTR {
node = self._impl.create_node(create_token_context($ID_SYSTEM))
edge = None
connector = "->" if $EDGE_ATTR.text == ":" else "_->"
edge = self._impl.create_arc(create_token_context($EDGE_ATTR), connector)

$ctx.items.append((node, edge))
}
	)+;

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

SENTENCE_SEP: ';;';
