from .settings import settings
from sc.memory import Memory

memory = Memory(settings.get_path_to_sc_config())
