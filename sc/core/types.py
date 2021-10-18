from enum import Enum

from sc.core.keywords import TypeAttrs


class TypeNodeStruct(Enum):
    UNKNOWN = 0
    TUPLE = 1
    STRUCT = 2
    ROLE = 3
    NO_ROLE = 4
    CLASS = 5
    ABSTRACT = 6
    MATERIAL = 7


class TypeConst(Enum):
    UNKNOWN = 0
    CONST = 1
    VAR = 2


class TypeArcPos(Enum):
    UNKNOWN = 0
    POS = 1
    NEG = 2
    FUZ = 3


class TypeArcPerm(Enum):
    UNKNOWN = 0
    TEMP = 1
    PERM = 2


class BaseType:

    class Kind(Enum):
        UNKNOWN = 0
        NODE = 1
        LINK = 2
        EDGE = 3
        ARC = 4

    def __init__(self, kind, const: TypeConst = TypeConst.UNKNOWN):
        self._kind = kind

        assert isinstance(const, TypeConst)
        self._type_const = const

    @property
    def type_const(self) -> TypeConst:
        return self._type_const

    def is_const(self) -> bool:
        return self._type_const == TypeConst.CONST

    def is_var(self) -> bool:
        return self._type_const == TypeConst.VAR

    def is_unknown(self) -> bool:
        return self._kind == BaseType.Kind.UNKNOWN

    def is_node(self) -> bool:
        return self._kind == BaseType.Kind.NODE

    def is_link(self) -> bool:
        return self._kind == BaseType.Kind.LINK

    def is_edge(self) -> bool:
        return self._kind == BaseType.Kind.EDGE

    def is_arc(self) -> bool:
        return self._kind == BaseType.Kind.ARC

    @property
    def kind(self):
        return self._kind

    def __eq__(self, o: object) -> bool:
        return self._kind == o._kind and self._type_const == o._type_const

    def __repr__(self) -> str:
        return f"BaseType(kind: {self._kind.name})"

    def is_connector(self) -> bool:
        return (self._kind == BaseType.Kind.ARC or
                self._kind == BaseType.Kind.EDGE)

    def _to_attrs(self) -> dict:
        return {TypeAttrs.CONST: self._type_const.name} if self._type_const != TypeConst.UNKNOWN else {}


class UnknownType(BaseType):

    def __init__(self):
        super().__init__(BaseType.Kind.UNKNOWN)


class NodeType(BaseType):

    def __init__(self,
                 const: TypeConst = TypeConst.UNKNOWN,
                 struct: TypeNodeStruct = TypeNodeStruct.UNKNOWN):
        super().__init__(BaseType.Kind.NODE, const)

        assert struct is None or isinstance(struct, TypeNodeStruct)

        self._type_struct = struct

    @property
    def type_struct(self) -> TypeNodeStruct:
        return self._type_struct

    def __repr__(self) -> str:
        return f"NodeType(const: {self.type_const}, struct: {self.type_struct})"

    def __eq__(self, o: object) -> bool:
        return (super().__eq__(o)
                and self.type_const == o.type_const
                and self.type_struct == o.type_struct)

    def _to_attrs(self) -> dict:
        res = super()._to_attrs()
        if self._type_struct != TypeNodeStruct.UNKNOWN:
            res.update({TypeAttrs.NODE_STRUCT: self._type_struct.name})
        return res


class LinkType(BaseType):

    def __init__(self, const: TypeConst = TypeConst.UNKNOWN):
        super().__init__(BaseType.Kind.LINK, const)

    def __repr__(self) -> str:
        return f"LinkType(const: {self.type_const})"


class EdgeType(BaseType):

    def __init__(self, const: TypeConst = TypeConst.UNKNOWN):
        super().__init__(BaseType.Kind.EDGE, const)

    def __repr__(self) -> str:
        return f"EdgeType(const: {self.type_const})"


class ArcType(BaseType):

    def __init__(self,
                 const: TypeConst = TypeConst.UNKNOWN,
                 arc_pos: TypeArcPos = TypeArcPos.UNKNOWN,
                 arc_perm: TypeArcPerm = TypeArcPerm.UNKNOWN,
                 is_member: bool = None):
        super().__init__(BaseType.Kind.ARC, const=const)

        assert isinstance(arc_pos, TypeArcPos)
        assert isinstance(arc_perm, TypeArcPerm)

        self._type_arc_pos = arc_pos
        self._type_arc_perm = arc_perm
        self._is_member = is_member

    @property
    def type_arc_pos(self) -> TypeArcPos:
        return self._type_arc_pos

    @property
    def type_arc_perm(self) -> TypeArcPerm:
        return self._type_arc_perm

    @property
    def is_member(self) -> bool:
        return self._is_member

    def __eq__(self, o: object) -> bool:
        return (super().__eq__(o)
                and self._type_arc_pos == o._type_arc_pos
                and self._type_arc_perm == o._type_arc_perm
                and self._is_member == o._is_member)

    def __repr__(self) -> str:
        result = f"ArcType(const: {self._type_const}"
        result += f", pos: {self._type_arc_pos}" if self._type_arc_pos is not None else ""
        result += f", perm: {self._type_arc_perm}" if self._type_arc_perm is not None else ""
        result += f", member: {self._is_member}" if self._is_member is not None else ""
        result += ")"

        return result

    def _to_attrs(self) -> dict:
        res = super()._to_attrs()
        if self._type_arc_perm is not None and self._type_arc_perm != TypeArcPerm.UNKNOWN:
            res.update({TypeAttrs.ARC_PERM: self._type_arc_perm.name})
        if self._type_arc_pos is not None and self._type_arc_pos != TypeArcPos.UNKNOWN:
            res.update({TypeAttrs.ARC_POS: self._type_arc_pos.name})
        if self._is_member is not None:
            res.update({TypeAttrs.ARC_MEMBER: self._is_member})

        return res
