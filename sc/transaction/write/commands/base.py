class Command:

  def __init__(self):
    pass

  def generate(self) -> str:
    return self._generate_impl()

  def _generate_impl(self) -> str:
    raise NotImplemented("Override _generate_impl function in the {} command".format(self.__class__))
