from sc.core.transaction import (
    TransactionNamesRead,
    TransactionNamesWrite,
    TransactionRead,
    TransactionWrite,
    FixedParameter,
    AssignParameter,
)
from sc.core.types import (
    ArcType,
    LinkType,
    NodeType,
    TypeArcPerm,
    TypeArcPos,
    TypeConst,
    TypeNodeStruct,
)

from .. import memory

NodeConst = NodeType(const=TypeConst.CONST)
NodeClass = NodeType(const=TypeConst.CONST, struct=TypeNodeStruct.CLASS)
NodeNoRole = NodeType(const=TypeConst.CONST, struct=TypeNodeStruct.NO_ROLE)
LinkConst = LinkType(const=TypeConst.CONST)
ArcMemberConstPosPerm = ArcType(
    const=TypeConst.CONST,
    arc_pos=TypeArcPos.POS,
    arc_perm=TypeArcPerm.PERM,
    is_member=True,
)


def create_user_in_memory(user_id: int):
    tr = TransactionNamesRead(memory.driver)
    class_user = tr.resolve_by_system_identifier("user")
    nrel_user_id = tr.resolve_by_system_identifier("nrel_user_id")
    result = tr.run()

    try:
        class_user = result[class_user]
    except KeyError:
        tr = TransactionWrite(memory.driver)
        class_user = tr.create_node(NodeClass, alias="user")
        result = tr.run()
        class_user = result[class_user]
        tr = TransactionNamesWrite(memory.driver)
        tr.set_system_identifier(class_user, "user")
        tr.run()

    try:
        nrel_user_id = result[nrel_user_id]
    except KeyError:
        tr = TransactionWrite(memory.driver)
        nrel_user_id = tr.create_node(NodeNoRole, alias="nrel_user_id")
        result = tr.run()
        nrel_user_id = result[nrel_user_id]
        tr = TransactionNamesWrite(memory.driver)
        tr.set_system_identifier(nrel_user_id, "nrel_user_id")
        tr.run()

    tr = TransactionWrite(memory.driver)
    user_instance = tr.create_node(NodeConst, alias="user_instance")
    _ = tr.create_edge(class_user, user_instance, ArcMemberConstPosPerm)
    link = tr.create_link_with_content(LinkConst, content=user_id, is_url=False)
    edge = tr.create_edge(user_instance, link, ArcMemberConstPosPerm)
    _ = tr.create_edge(nrel_user_id, edge, ArcMemberConstPosPerm)
    result = tr.run()


def check_user_in_memory(user_id: int) -> bool:
    tr = TransactionNamesRead(memory.driver)
    class_user = tr.resolve_by_system_identifier("user")
    nrel_user_id = tr.resolve_by_system_identifier("nrel_user_id")
    results = tr.run()

    try:
        class_user = results[class_user]
        nrel_user_id = results[nrel_user_id]
    except KeyError:
        return False

    tr = TransactionRead(memory.driver)
    _class_user, _cls_edge, _user_instance = tr.triple_faa(
        FixedParameter(class_user, "class_user"),
        AssignParameter(ArcMemberConstPosPerm, "cls_edge"),
        AssignParameter(NodeConst, "user_instance"),
    )
    _, _link_edge, _link = tr.triple_faa(
        _user_instance,
        AssignParameter(ArcMemberConstPosPerm, "link_edge"),
        AssignParameter(LinkConst, "link"),
    )
    _nrel_user_id, _, _ = tr.triple_faf(
        FixedParameter(nrel_user_id, "nrel_user_id"),
        AssignParameter(ArcMemberConstPosPerm),
        _link_edge,
    )
    # results = tr.run()
    # result = results[0]
    # link = result[_link]

    # for result in results:
    #     link = result[_link]
    #     if link.content == user_id:
    #         return True

    return False


def create_user_in_memory_if_not_exist(user_id: int):
    if not check_user_in_memory(user_id):
        create_user_in_memory(user_id)
