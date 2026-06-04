"""Zomboid RCON: https://github.com/jmwhitworth/zomboid_rcon"""

from .BaseRconClient import BaseRconClient
from .CommandResult import CommandResult
from .ZomboidRcon import ZomboidRcon

ZomboidRCON = ZomboidRcon  # Backwards compatibility alias

__title__ = "zomboid_rcon"
__version__ = "2.0.0"
