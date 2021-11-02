class KeynodeNames:
    SC_NODE = "sc_node"
    SC_LINK = "sc_link"
    SC_EDGE = "sc_edge"
    SC_ARC = "sc_arc"

    CORE_TYPES = [SC_NODE, SC_LINK, SC_EDGE, SC_ARC]

    SC_CONST = "sc_const"
    SC_VAR = "sc_var"

    CONST_TYPES = [SC_CONST, SC_VAR]

    SC_NODE_STRUCT = "sc_node_struct"
    SC_NODE_TUPLE = "sc_node_tuple"
    SC_NODE_ROLE = "sc_node_role"
    SC_NODE_NO_ROLE = "sc_node_no_role"
    SC_NODE_CLASS = "sc_node_class"
    SC_NODE_ABSTRACT = "sc_node_abstract"
    SC_NODE_MATERIAL = "sc_node_material"

    NODE_TYPES = [
        SC_NODE_STRUCT, SC_NODE_TUPLE, SC_NODE_ROLE,
        SC_NODE_NO_ROLE, SC_NODE_CLASS, SC_NODE_ABSTRACT,
        SC_NODE_MATERIAL]

    SC_ARC_PERM = "sc_arc_perm"
    SC_ARC_TEMP = "sc_arc_temp"

    ARC_PERM_TYPES = [SC_ARC_PERM, SC_ARC_TEMP]

    SC_ARC_POS = "sc_arc_pos"
    SC_ARC_NEG = "sc_arc_neg"
    SC_ARC_FUZ = "sc_arc_fuz"

    ARC_POS_TYPES = [SC_ARC_POS, SC_ARC_NEG, SC_ARC_FUZ]

    # common keynodes
    NREL_SYS_IDTF = "nrel_system_identifier"
