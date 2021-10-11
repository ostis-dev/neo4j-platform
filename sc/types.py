from enum import Enum

class Type:
  
  CONST = 0x20
  VAR = 0x40

  ARC_POS = 0x80
  ARC_NEG = 0x100
  ARC_FUZ = 0x200

  ARC_TEMP = 0x400
  ARC_PERM = 0x800

  NODE_TUPLE = 0x1000
  NODE_STRUCT = 0x2000
  NODE_ROLE = 0x4000
  NODE_NO_ROLE = 0x8000
  NODE_CLASS = 0x10000
  NODE_ABSTRACT = 0x20000
  NODE_MATERIAL = 0x40000

  UNKNOWN = 0
  NODE = 0x1
  LINK = 0x2
  EDGE = 0x4
  ARC = 0x8
  ARC_MEMBER = ARC | ARC_POS | CONST | ARC_PERM

  _SEMANTIC_FLAGS = NODE | LINK | ARC  | EDGE
  _CONNECTOR_FLAGS = ARC | EDGE
  _CONST_FLAGS = CONST | VAR
  _ARC_POS_FLAGS = ARC_POS | ARC_NEG | ARC_FUZ
  _ARC_PERM_FLAGS = ARC_TEMP | ARC_PERM
  _NODE_FLAGS = NODE_TUPLE | NODE_STRUCT | NODE_ROLE | NODE_NO_ROLE | NODE_CLASS | NODE_ABSTRACT | NODE_MATERIAL
  
  def __init__(self, flags: int):
    self._flags = flags
    
    def _check_one_flag(flag):
      # check if value is power of 2
      return (flag == 0) or ((flag & (flag - 1)) == 0)

    def _check_only_flags(flags):
      return (self._flags & (~flags)) == 0

    if (self._flags & Type._SEMANTIC_FLAGS == 0) and ((~Type._CONST_FLAGS) & self._flags) != 0:
      raise TypeError("You should specify semantic type or use Unknown")

    if self.isConnector() and self.isNode():
      raise TypeError("This is not possible to use Node and Arc | Edge flags in one type")
    if self.isConnector() and self.isLink():
      raise TypeError("This is not possible to use Link and Arc | Edge flags in one type")

    if not _check_one_flag(self._flags & Type._CONST_FLAGS):
      raise TypeError("You have specified more than one constancy flag")

    if self.isConnector():
      if not _check_one_flag(self._flags & Type._ARC_POS_FLAGS):
        raise TypeError("You have specified more than one arc positivity flag")

      if not _check_one_flag(self._flags & Type._ARC_PERM_FLAGS):
        raise TypeError("You have specified more than one arc permanency flag")

      if not _check_one_flag(self._flags & Type._CONNECTOR_FLAGS):
        raise TypeError("You have specified more than one semantic type for an edge/arc")

      if not self.isEdge():
        if not _check_only_flags(Type._CONST_FLAGS | Type._ARC_PERM_FLAGS | Type._ARC_POS_FLAGS | Type.ARC | Type.ARC_MEMBER):
          raise TypeError("You should use only arc related flags for arc type")
      else:
        if not _check_only_flags(Type.EDGE | Type._CONST_FLAGS):
          raise TypeError("Edge type can only use constancy flags")

    if self.isNode():
      if not _check_one_flag(self._flags & Type._NODE_FLAGS):
        raise TypeError("You have specified more than one node flag")

      if not _check_only_flags(Type.NODE | Type._NODE_FLAGS | Type._CONST_FLAGS):
        raise TypeError("You can use only _NodeFlags for Node type")

    if self.isLink():
      if not _check_only_flags(Type.LINK | Type._CONST_FLAGS):
        raise TypeError("Link type can only use constancy flags")


  def isConst(self) -> bool:
    return self.hasFlag(Type.CONST)

  def isVar(self) -> bool:
    return self.hasFlag(Type.VAR)

  def isNode(self) -> bool:
    return self.hasFlag(Type.NODE)

  def isLink(self) -> bool:
    return self.hasFlag(Type.LINK)

  def isEdge(self) -> bool:
    return self.hasFlag(Type.EDGE)

  def isArc(self) -> bool:
    return self.hasFlag(Type.ARC)

  def isArcMember(self) -> bool:
    return self._flags == Type.ARC_MEMBER

  def isConnector(self) -> bool:
    return self.hasFlag(Type._CONNECTOR_FLAGS)

  def hasFlag(self, flag) -> bool:
    return (self._flags & flag) > 0

# predefined types

def Unknown():
  return Type(Type.UNKNOWN)

def UnknownConst():
  return Type(Type.CONST)

def UnknownVar():
  return Type(Type.VAR)

# ----- Nodes -----
def Node():
  return Type(Type.NODE)

def NodeConst():
  return Type(Type.NODE | Type.CONST)

def NodeConstTuple():
  return Type(Type.NODE | Type.CONST | Type.NODE_TUPLE)

def NodeConstStruct():
  return Type(Type.NODE | Type.CONST | Type.NODE_STRUCT)
  
def NodeConstRole():
  return Type(Type.NODE | Type.CONST | Type.NODE_ROLE)

def NodeConstNoRole():
  return Type(Type.NODE | Type.CONST | Type.NODE_NO_ROLE)
  
def NodeConstClass():
  return Type(Type.NODE | Type.CONST | Type.NODE_CLASS)

def NodeConstAbstract():
  return Type(Type.NODE | Type.CONST | Type.NODE_ABSTRACT)
  
def NodeConstMaterial():
  return Type(Type.NODE | Type.CONST | Type.NODE_MATERIAL)

# -----
def NodeVar():
  return Type(Type.NODE | Type.VAR)

def NodeVarTuple():
  return Type(Type.NODE | Type.VAR | Type.NODE_TUPLE)

def NodeVarStruct():
  return Type(Type.NODE | Type.VAR | Type.NODE_STRUCT)
  
def NodeVarRole():
  return Type(Type.NODE | Type.VAR | Type.NODE_ROLE)

def NodeVarNoRole():
  return Type(Type.NODE | Type.VAR | Type.NODE_NO_ROLE)
  
def NodeVarClass():
  return Type(Type.NODE | Type.VAR | Type.NODE_CLASS)

def NodeVarAbstract():
  return Type(Type.NODE | Type.VAR | Type.NODE_ABSTRACT)
  
def NodeVarMaterial():
  return Type(Type.NODE | Type.VAR | Type.NODE_MATERIAL)

# ----- Links -----
def Link():
  return Type(Type.LINK)

def LinkConst():
  return Type(Type.LINK | Type.CONST)

def LinkVar():
  return Type(Type.LINK | Type.VAR)

# ----- Edges -----
def Edge():
  return Type(Type.EDGE)

def EdgeConst():
  return Type(Type.EDGE | Type.CONST)

def EdgeVar():
  return Type(Type.EDGE | Type.VAR)

# ----- Arcs -----
def Arc():
  return Type(Type.ARC)

def ArcConst():
  return Type(Type.ARC | Type.CONST)

def ArcVar():
  return Type(Type.ARC | Type.VAR)