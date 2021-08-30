from typing import overload
from sc.transaction.write.commands.base import Command

class CreateNodeCommand(Command):
  
  def __init__(self, name):
    super().__init__()
    self.name = name

  def _generate_impl(self) -> str:
    return "CREATE ({}:sc_node)".format(self.name)
