from sc.core.types import ArcType, BaseType, EdgeType, LinkType, NodeType, TypeArcPerm, TypeArcPos, TypeConst, TypeNodeStruct
from sc.core.keywords import Labels, TypeAttrs

import neo4j


def get_key_safe(d: object, key: str) -> any:
    try:
        return d[key]
    except KeyError:
        return None


class ElementID:

    @staticmethod
    def from_string(s: str):
        values = s.split(":")
        assert len(values) == 2
        return ElementID(values[1], values[0])

    def __init__(self, label, identity: int) -> None:
        self._label = label
        self._identity = identity

    def __eq__(self, o: object) -> bool:
        return self._identity == o._identity and self._label == o._label

    def __ne__(self, o: object) -> bool:
        return self._identity != o._identity or self._label != o._label

    @property
    def full_id(self) -> str:
        return str(self._identity) + ":" + self._label

    @property
    def identity(self):
        return self._identity

    @property
    def label(self) -> str:
        return self._label

    def __repr__(self) -> str:
        return f"ElementID({self._identity}:{self._label})"


class Element:

    def __init__(self, id: ElementID, type: BaseType) -> None:
        self._id = id
        self._type = type

    @property
    def id(self) -> ElementID:
        return self._id

    @property
    def type(self) -> BaseType:
        return self._type

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id: {self._id}, type: {self._type})"

    def __eq__(self, o: object) -> bool:
        return (self._id == o._id
                and self._type == o._type)


class Node(Element):
    def __init__(self, node: neo4j.graph.Node) -> None:
        assert isinstance(node, neo4j.graph.Node)

        label, = node.labels
        assert label == Labels.SC_NODE

        id = ElementID(label, node.id)

        type_const_value = get_key_safe(node, TypeAttrs.CONST)
        if type_const_value is not None:
            type_const_value = TypeConst[type_const_value]

        type_struct_value = get_key_safe(node, TypeAttrs.NODE_STRUCT)
        if type_struct_value is not None:
            type_struct_value = TypeNodeStruct[type_struct_value]

        type = NodeType(const=type_const_value,
                        struct=type_struct_value)
        super().__init__(id, type)


class Edge(Element):
    def __init__(self, edge: neo4j.graph.Relationship) -> None:
        assert isinstance(edge, neo4j.graph.Relationship)
        assert edge.type == Labels.SC_EDGE

        id = ElementID(edge.type, edge.id)

        type_const_value = get_key_safe(edge, TypeAttrs.CONST)
        if type_const_value is not None:
            type_const_value = TypeConst[type_const_value]

        type = EdgeType(const=type_const_value)

        super().__init__(id, type)


class Link(Element):
    def __init__(self, node: neo4j.graph.Node) -> None:
        assert isinstance(node, neo4j.graph.Node)

        label, = node.labels
        assert label == Labels.SC_LINK

        id = ElementID(label, node.id)

        type_const_value = get_key_safe(node, TypeAttrs.CONST)
        if type_const_value is not None:
            type_const_value = TypeConst[type_const_value]

        type = LinkType(const=type_const_value)

        super().__init__(id, type)


class Arc(Element):
    def __init__(self, edge: neo4j.graph.Relationship) -> None:
        assert isinstance(edge, neo4j.graph.Relationship)
        assert edge.type == Labels.SC_ARC

        id = ElementID(edge.type, edge.id)

        type_const_value = get_key_safe(edge, TypeAttrs.CONST)
        if type_const_value is not None:
            type_const_value = TypeConst[type_const_value]

        is_arc_member_value = get_key_safe(
            edge, TypeAttrs.ARC_MEMBER)
        if is_arc_member_value is None:
            is_arc_member_value = False

        type_arc_pos_value = get_key_safe(edge, TypeAttrs.ARC_POS)
        if type_arc_pos_value is not None:
            type_arc_pos_value = TypeArcPos[type_arc_pos_value]

        type_arc_perm_value = get_key_safe(edge, TypeAttrs.ARC_PERM)
        if type_arc_perm_value is not None:
            type_arc_perm_value = TypeArcPerm[type_arc_perm_value]

        type = ArcType(const=type_const_value,
                       arc_pos=type_arc_pos_value,
                       arc_perm=type_arc_perm_value,
                       is_member=is_arc_member_value)

        super().__init__(id, type)
