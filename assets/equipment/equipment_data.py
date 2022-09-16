from dataclasses import dataclass, field


@dataclass
class EquipmentData:
    """Weapons and armors storage"""
    weapons: list = field(default_factory=list)
    armor: list = field(default_factory=list)
