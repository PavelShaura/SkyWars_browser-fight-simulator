from assets.skills import BaseSkill


class Uglybreath(BaseSkill):
    """Special skill"""
    name: str = 'Гадкий выдох'
    damage: float = 15.0
    stamina_required: float = 5.0

    def _skill_effect(self) -> str:
        """Decrease target health and decrease user stamina"""
        self.target.health_points_ -= self.damage
        self.user.stamina_points_ -= self.stamina_required
        return f'{self.user.name} использует {self.user.unit_class.skill.name} и наносит {self.damage} урона сопернику.'
