CREATE 
  (link:$sc_link {content: "$nrel_sys_idtf", is_url: false, type: "str"}),
  (node:$sc_node),
  (node)-[edge:$sc_edge]->(link)
WITH edge, node
CREATE
  (edge_sock:$sc_edge_sock {edge_id: id(edge)}),
  (node)-[:sc_edge]->(edge_sock)
RETURN null
