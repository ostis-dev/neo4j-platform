from sc.core.keynodes import KeynodeNames

from typing import Dict, List, Set, Tuple, Union

from .parse_issue import ParseIssue
from .types import Alias, Arc, Edge, Element, Link, Node, TokenContext

from antlr4.error.Errors import ParseCancellationException


Triple = Tuple[Element, Union[Arc, Edge], Element]


class SCsParserImpl:

    def __init__(self) -> None:
        # list of parsed triples
        self._triples = []

        # Dictionary of element types.
        # They should be in format: {element.name, set(str)}
        self._types = {}

        # Counter for generated names
        self._names_counter = 0

        # Set of type keynodes (for fast access)
        self._type_keynodes = set()
        self._type_keynodes.update(KeynodeNames.CORE_TYPES)
        self._type_keynodes.update(KeynodeNames.CONST_TYPES)
        self._type_keynodes.update(KeynodeNames.NODE_TYPES)
        self._type_keynodes.update(KeynodeNames.ARC_PERM_TYPES)
        self._type_keynodes.update(KeynodeNames.ARC_POS_TYPES)

        # Dictionary of alias definitions <str, AliasDefinition>
        self._aliases = {}

        # List of warnings
        self._errors = []
        self._warnings = []

    @property
    def errors(self) -> List[ParseIssue]:
        return self._errors

    @property
    def warnings(self) -> List[ParseIssue]:
        return self._warnings

    @property
    def types(self) -> Dict[str, Set[str]]:
        """Returns dictionary with element types"""
        return self._types

    @property
    def triples(self) -> List[Triple]:
        """Returns list of triples"""
        return self._triples

    def _process_name(self, name: str, prefix: str = "el") -> str:
        def next_id():
            self._names_counter += 1
            return self._names_counter

        return name if name is not None or name == "..." else f"..{prefix}_generated_{next_id()}"

    def _is_type_keynode(self, name: str) -> bool:
        """Checks if specified name if a type keynode"""
        return name in self._type_keynodes

    def _break_parsing(self, msg: str):
        """Raises error to break parsing"""
        raise ParseCancellationException(msg)

    def create_alias(self, ctx: TokenContext) -> Alias:
        return Alias(ctx.text, ctx, None)

    def create_node(self, ctx: TokenContext) -> Node:
        return Node(self._process_name(ctx.text, prefix="node"), ctx)

    def create_link(self, ctx: TokenContext, value: Link.Value, type: Link.Type) -> Link:
        return Link(self._process_name(ctx.text, prefix="link"), value, type, ctx)

    def create_edge(self, ctx: TokenContext, connector: str) -> Edge:
        return Edge(connector, self._process_name(None, prefix="edge"), ctx)

    def create_arc(self, ctx: TokenContext, connector: str) -> Arc:
        return Arc(connector, self._process_name(None, prefix="arc"), ctx)

    def append_triple(self, src: Element, edge: Union[Edge, Arc], trg: Element):
        def _resolve_alias(alias: Alias) -> Element:
            try:
                return self._aliases[alias.name].target
            except KeyError:
                self._new_error(alias.ctx,
                                f"Alias {alias.name} is not defined")
                self._break_parsing(f"Alias {alias.name} is not defined")

        if src.kind == Element.Kind.ALIAS:
            src = _resolve_alias(src)
        if trg.kind == Element.Kind.ALIAS:
            trg = _resolve_alias(trg)

        if edge._reverse_if_back():
            self._triples.append((trg, edge, src))
        else:
            self._triples.append((src, edge, trg))

    def define_alias(self, alias: Alias, target: Element) -> Alias:
        """Create new alias to specified element"""
        assert alias.target is None
        try:
            prev_alias = self._aliases[alias.name]
            self._new_warning(alias.ctx,
                              (f"Alias {alias.name} was previously defined at line: {prev_alias.ctx.line}"
                               " column: {prev_alias.ctx.column}"))
        except KeyError:
            pass

        new_alias = Alias(alias.name, alias.ctx, target)
        self._aliases[new_alias.name] = new_alias
        return new_alias

    def _new_error(self, ctx: TokenContext, msg: str):
        self._errors.append(
            ParseIssue(ctx.line, ctx.column, ctx.text, msg, ParseIssue.Type.ERROR))

    def _new_warning(self, ctx: TokenContext, msg: str):
        self._warnings.append(
            ParseIssue(ctx.line, ctx.column, ctx.text, msg, ParseIssue.Type.ERROR))

    def _add_type(self, name: str, type_keynode: str):
        try:
            self._types[name].add(type_keynode)
        except KeyError:
            self._types[name] = {type_keynode}

    def _processIdtfLevel1(self, ctx: TokenContext, type_: str) -> Element:
        """Determines which element should be created by identifier from scs-level-1."""
        if type_ == KeynodeNames.SC_NODE:
            return self.create_node(ctx)
        elif type_ == KeynodeNames.SC_ARC:
            return self.create_arc(ctx, '..>')
        elif type_ == KeynodeNames.SC_EDGE:
            return self.create_edge(ctx, '>')
        elif type_ == KeynodeNames.SC_LINK:
            return self.create_link(ctx, "", Link.Type.STRING)
        else:
            self._new_error(ctx, (f"Type `{type_}` is not supported. You should use only types from a list: "
                                  "{KeynodeNames.SC_NODE},  {KeynodeNames.SC_ARC}, "
                                  "{KeynodeNames.SC_EDGE}, {KeynodeNames.SC_LINK}"))

        return None
