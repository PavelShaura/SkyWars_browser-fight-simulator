from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from assets.units import BaseUnit


class BaseSkill(ABC):
    """Base class for special skills"""
    name: str = ""
    damage: float = 0
    stamina_required: float = 0
    user: BaseUnit
    target: BaseUnit

    @abstractmethod
    def _skill_effect(self):
        pass

    def use(self, user: BaseUnit, target: BaseUnit):
        """Use special skill if user has enough stamina"""
        self.user = user
        self.target = target

        if self.user.stamina_points_ < self.stamina_required:
            return (f"{self.user.name} решился воспользоваться {self.user.unit_class.skill.name}, "
                    f"однако, не хватило выносливости.")
        return self._skill_effect()
