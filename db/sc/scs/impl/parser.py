from sc.scs.element import *
from typing import AsyncIterable, List, Tuple, Union

from sc.core.keynodes import KeynodeNames

Alias = str
TripleElement = Union[Element, Alias]
Triple = Tuple[TripleElement, TripleElement, TripleElement]


class SCsParserImpl:

    class AliasDefinition:
        def __init__(self, alias: str, line: int, element: Element) -> None:
            self._alias = alias
            self._line = line
            self._element = element

        @property
        def alias(self) -> str:
            return self._alias

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(alias: {self._alias}, line: {self._line}, element: {self._element})"

    def __init__(self) -> None:
        # list of parsed triples
        self._triples = []

        # List of triples that determine type of elements.
        # They should be in format: type -> element;;
        self._type_triples = []

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

    @property
    def type_triples(self) -> List[Triple]:
        return self._type_triples

    @property
    def triples(self) -> List[Triple]:
        return self._triples

    def _process_name(self, name: str, prefix: str = "el") -> str:
        def next_id():
            self._names_counter += 1
            return self._names_counter

        return name if name is not None else f"..{prefix}_generated_{next_id()}"

    def _is_type_keynode(self, name: str) -> bool:
        """Checks if specified name if a type keynode"""
        return name in self._type_keynodes

    def define_alias(self, alias: str, element: Element, line: int) -> str:
        """Create definition of alias

        If alias already exists, then raises KeyError
        """
        try:
            found_alias = self._aliases[alias]
            raise KeyError(
                f"Alias `{alias}` already defined before in line {found_alias.line}")
        except KeyError:
            self._aliases[alias] = SCsParserImpl.AliasDefinition(
                alias=alias, line=line, element=element)
        return

    def create_node(self, name: str = None) -> Node:
        return Node(name=self._process_name(name, prefix="node"))

    def create_link(self, name: str = None, value: Link.Value = None, type: Link.Type = Link.Type.UNKNOWN) -> Link:
        return Link(name=self._process_name(name, prefix="link"), value=value, type=type)

    def create_edge(self, src: Union[Element, Alias], trg: Union[Element, Alias], connector: str = None) -> Edge:
        edge = Edge(self._process_name(None, prefix="edge"))
        self._append_triple(src, edge, trg)
        return edge

    def create_arc(self, src: Union[Element, Alias], trg: Union[Element, Alias], connector: str = None) -> Arc:
        arc = Arc(self._process_name(None, prefix="arc"))
        self._append_triple(src, arc, trg)
        return arc

    def _append_triple(self, src: Union[Element, Alias], edge: Union[Edge, Arc], trg: Union[Element, Alias]):
        if self._is_type_keynode(src.name):
            self._type_triples.append((src, edge, trg))
        else:
            self._triples.append((src, edge, trg))
