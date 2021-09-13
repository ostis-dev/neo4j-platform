class ElementID:

  @staticmethod
  def from_string(s: str):
    values = s.split(":")
    assert len(values) == 2
    return ElementID(values[1], values[0])

  def __init__(self, label, id: int) -> None:
    self._label = label
    self._id = id

  @property
  def full_id(self):
    return str(self._id) + ":" + self._label

  @property
  def id(self):
    return self._id

  @property
  def label(self):
    return self._label

  def __repr__(self) -> str:
    return f"ElementID({self.full_id})"