from typing import overload
from sc.commands.command import Command

class CreateNodeCommand(Command):
  
  def __init__(self, name):
    super().__init__()
    self.name = name

  def _generate_impl(self) -> str:
    return "CREATE ({}:sc_node)".format(self.name)
