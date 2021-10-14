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
        ARC_MEMBER = 5

    def __init__(self, kind, typeConst: TypeConst = TypeConst.UNKNOWN):
        self._kind = kind

        assert isinstance(typeConst, TypeConst)
        self._typeConst = typeConst

    @property
    def typeConst(self) -> TypeConst:
        return self._typeConst

    def isConst(self) -> bool:
        return self._typeConst == TypeConst.CONST

    def isVar(self) -> bool:
        return self._typeConst == TypeConst.VAR

    @property
    def kind(self):
        return self._kind

    def __eq__(self, o: object) -> bool:
        return self._kind == o._kind and self._typeConst == o._typeConst

    def __repr__(self) -> str:
        return f"BaseType(kind: {self._kind.name})"

    def isConnector(self) -> bool:
        return (self._kind == BaseType.Kind.ARC or
                self._kind == BaseType.Kind.EDGE or
                self._kind == BaseType.Kind.ARC_MEMBER)

    def _toAttrs(self) -> dict:
        return { TypeAttrs.CONST: self._typeConst.name }


class UnknownType(BaseType):

    def __init__(self):
        super().__init__(BaseType.Kind.UNKNOWN)


class NodeType(BaseType):

    def __init__(self,
                 typeConst: TypeConst = TypeConst.UNKNOWN,
                 typeStruct: TypeNodeStruct = TypeNodeStruct.UNKNOWN):
        super().__init__(BaseType.Kind.NODE, typeConst)

        assert isinstance(typeStruct, TypeNodeStruct)

        self._typeStruct = typeStruct

    @property
    def typeStruct(self) -> TypeNodeStruct:
        return self._typeStruct

    def __repr__(self) -> str:
        return f"NodeType(const: {self.typeConst}, struct: {self.typeStruct})"

    def __eq__(self, o: object) -> bool:
        return (super().__eq__(o) and
                self.typeConst == o.typeConst and
                self.typeStruct == o.typeStruct)

    def _toAttrs(self) -> dict:
        res = super()._toAttrs()
        res.update({ TypeAttrs.NODE_STRUCT: self._typeStruct.name })
        return res


class LinkType(BaseType):

    def __init__(self, typeConst: TypeConst = TypeConst.UNKNOWN):
        super().__init__(BaseType.Kind.LINK, typeConst)

    def __repr__(self) -> str:
        return f"LinkType(const: {self.typeConst})"


class EdgeType(BaseType):

    def __init__(self, typeConst: TypeConst = TypeConst.UNKNOWN):
        super().__init__(BaseType.Kind.EDGE, typeConst)

    def __repr__(self) -> str:
        return f"EdgeType(const: {self.typeConst})"


class ArcType(BaseType):

    def __init__(self, typeConst: TypeConst = TypeConst.UNKNOWN):
        super().__init__(BaseType.Kind.ARC, typeConst=typeConst)

    def __repr__(self) -> str:
        return f"ArcType(const: {self.typeConst})"


class ArcMemberType(BaseType):

    def __init__(self,
                 typeConst: TypeConst = TypeConst.UNKNOWN,
                 typeArcPos: TypeArcPos = TypeArcPos.UNKNOWN,
                 typeArcPerm: TypeArcPerm = TypeArcPerm.UNKNOWN):
        super().__init__(BaseType.Kind.ARC_MEMBER, typeConst)

        assert isinstance(typeArcPos, TypeArcPos)
        assert isinstance(typeArcPerm, TypeArcPerm)

        self._typeArcPos = typeArcPos
        self._typeArcPerm = typeArcPerm

    @property
    def typeArcPos(self) -> TypeArcPos:
        return self._typeArcPos

    @property
    def typeArcPerm(self) -> TypeArcPerm:
        return self._typeArcPerm

    def __eq__(self, o: object) -> bool:
        return (super().__eq__(o) and
                self.typeArcPos == o.typeArcPos and
                self.typeArcPerm == o.typeArcPerm)

    def __repr__(self) -> str:
        return f"ArcMemberType(const: {self.typeConst}, pos: {self.typeArcPos}, perm: {self.typeArcPerm})"

    def _toAttrs(self) -> dict:
        res = super()._toAttrs()
        res.update({ TypeAttrs.ARC_PERM: self._typeArcPerm.name })
        res.update({ TypeAttrs.ARC_POS: self._typeArcPos.name })
        return res
