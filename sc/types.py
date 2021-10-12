from enum import Enum


class TypeSemantic(Enum):
    UNKNOWN = 0
    NODE = 1
    LINK = 2
    EDGE = 3
    ARC = 4
    ARC_MEMBER = 5


class TypeNode(Enum):
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


class Type:

    def __init__(self,
                 typeSem: TypeSemantic,
                 typeConst: TypeConst = None,
                 typeNode: TypeNode = None,
                 typeArcPos: TypeArcPos = None,
                 typeArcPerm: TypeArcPerm = None):

        self._sem = typeSem
        self._node = typeNode
        self._const = typeConst
        self._arcPos = typeArcPos
        self._arcPerm = typeArcPerm

        self.__check_valid()

    @staticmethod
    def UNKNOWN():
        return Type(typeSem=TypeSemantic.UNKNOWN)

    @staticmethod
    def NODE(typeConst: TypeConst = TypeConst.UNKNOWN,
             typeNode: TypeNode = TypeNode.UNKNOWN):

        assert isinstance(typeConst, TypeConst)
        assert isinstance(typeNode, TypeNode)
        return Type(typeSem=TypeSemantic.NODE,
                    typeConst=typeConst,
                    typeNode=typeNode)

    @staticmethod
    def LINK(typeConst: TypeConst = TypeConst.UNKNOWN):
        assert isinstance(typeConst, TypeConst)
        return Type(typeSem=TypeSemantic.LINK,
                    typeConst=typeConst)

    @staticmethod
    def EDGE(typeConst: TypeConst = TypeConst.UNKNOWN):
        assert isinstance(typeConst, TypeConst)
        return Type(typeSem=TypeSemantic.EDGE,
                    typeConst=typeConst)

    @staticmethod
    def ARC(typeConst: TypeConst = TypeConst.UNKNOWN,
            typeArcPos: TypeArcPos = TypeArcPos.UNKNOWN,
            typeArcPerm: TypeArcPerm = TypeArcPerm.UNKNOWN):

        assert isinstance(typeConst, TypeConst)
        assert isinstance(typeArcPos, TypeArcPos)
        assert isinstance(typeArcPerm, TypeArcPerm)
        return Type(typeSem=TypeSemantic.ARC,
                    typeConst=typeConst,
                    typeArcPos=typeArcPos,
                    typeArcPerm=typeArcPerm)

    @staticmethod
    def ARC_MEMBER():
        return Type(typeSem=TypeSemantic.ARC_MEMBER,
                    typeConst=TypeConst.CONST,
                    typeArcPos=TypeArcPos.POS,
                    typeArcPerm=TypeArcPerm.PERM)

    def __check_valid(self):

        if self._sem is None:
            raise TypeError("You should specify semantic type or use Unknown")

        if self.isArc():
            if self._arcPerm is None:
                raise TypeError(
                    "You should specify permanency flag 'typeArcPerm'")

            if self._arcPos is None:
                raise TypeError(
                    "You should specify positivity flag 'typeArcPos'")

        if self.isNode() or self.isLink() or self.isEdge():
            if self._arcPerm is not None:
                raise TypeError(
                    "You can't use 'typeArcPerm' with node/link/edge type")
            if self._arcPos is not None:
                raise TypeError(
                    "You can't use 'typeArcPos' with node/link/edge type")

        if self.isConnector():
            if self._node is not None:
                raise TypeError("You can't use 'typeNode' with connectors")

        if self.isLink():
            if self._node is not None:
                raise TypeError("You can't use 'typeNode' with link type")

        if self.isArcMember():
            if self._arcPerm != TypeArcPerm.PERM:
                raise TypeError("ArcMember should be permanent")
            if self._arcPos != TypeArcPos.POS:
                raise TypeError("ArcMember should be positive")
            if self._const != TypeConst.CONST:
                raise TypeError("ArcMember should be constant")

    def isConst(self) -> bool:
        return self._const == TypeConst.CONST

    def isVar(self) -> bool:
        return self._const == TypeConst.VAR

    def isNode(self) -> bool:
        return self._sem == TypeSemantic.NODE

    def isLink(self) -> bool:
        return self._sem == TypeSemantic.LINK

    def isEdge(self) -> bool:
        return self._sem == TypeSemantic.EDGE

    def isArc(self) -> bool:
        return self._sem == TypeSemantic.ARC

    def isArcMember(self) -> bool:
        return self._sem == TypeSemantic.ARC_MEMBER

    def isConnector(self) -> bool:
        return self.isArcMember() or self.isArc() or self.isEdge()

    def __repr__(self) -> str:

        def name(attr) -> str:
            return attr.name.capitalize() if attr is not None else "None"

        if self.isNode():
            return f"{self._sem.name.capitalize()}(const: {name(self._const)}, node: {name(self._node)})"
        elif self.isLink() or self.isEdge():
            return f"{self._sem.name.capitalize()}(const: {name(self._const)})"
        elif self.isArc() or self.isArcMember():
            return f"{self._sem.name.capitalize()}(const: {name(self._const)}, pos: {name(self._arcPos)}, perm: {name(self._arcPerm)})"

        return f"{self._sem.name}"
