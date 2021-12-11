
class Node:
  def __init__(self, name, line):
    """Constructor

    Args:
        name (String): Name of the vertex
        line (String): Station line name
    """
    self.next_node = None
    self.prev_node = None
    self.name      = name
    self.line      = line
    self.edges     = []
    self.route     = []
    self.distance  = 0
  def set_edges(self, edges):
    """Appends edges to the vertex for easy control of the information

    Args:
        edges (List)
    """
    self.edges.append(edges)
  def set_next_node(self, node):
    """Method to set the next of the doubly linked list

    Args:
        node (Node): Node type object for next
    """
    self.next_node = node
  def set_prev_node(self, node):
    """Method to set the previous of the doubly linked list

    Args:
        node (Node): Node type object for previous
    """
    self.prev_node = node
  def get_id(self):
    """Method for returning ID

    Returns:
        Address: Address of the object
    """
    return self.id
  def get_name(self):
    """Returns the name of the object

    Returns:
        String: Name of the station
    """
    return self.name

