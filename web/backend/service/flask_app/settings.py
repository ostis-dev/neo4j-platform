from ..config import Config
import os

settings = Config(os.environ.get("CONFIG_PATH"))
