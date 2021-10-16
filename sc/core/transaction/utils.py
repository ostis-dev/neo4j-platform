import neo4j


from sc.core.types import BaseType
from sc.core.element import Element, Edge, Arc, Link, Node
from sc.core.keywords import Labels


def _get_label_from_type(type: BaseType) -> Labels:
    if type.is_node():
        return Labels.SC_NODE
    elif type.is_arc():
        return Labels.SC_ARC
    elif type.is_edge():
        return Labels.SC_EDGE
    elif type.is_link():
        return Labels.SC_LINK
    else:
        raise TypeError(f"Unsupported type {type}")


def _parse_output_element(item) -> Element:
    if isinstance(item, neo4j.graph.Relationship):
        if item.type == Labels.SC_EDGE:
            return Edge(item)
        elif item.type == Labels.SC_ARC:
            return Arc(item)
        else:
            raise TypeError(
                f"Unsupported type of relations `{item.type}`")

    elif isinstance(item, neo4j.graph.Node):
        label, = item.labels
        if label == Labels.SC_NODE:
            return Node(item)
        elif label == Labels.SC_LINK:
            return Link(item)
        else:
            raise TypeError(
                f"Unsupported type of nodes `{item.type}`")
