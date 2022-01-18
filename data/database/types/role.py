from enum import Enum, auto


class RoleType(Enum):
    owner = auto()
    admin = auto()
    member = auto()
