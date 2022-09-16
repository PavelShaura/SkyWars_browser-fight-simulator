from assets.skills import BaseSkill


class FuriousKick(BaseSkill):
    """Special skill"""
    name: str = 'Пинок ярости'
    damage: float = 12.0
    stamina_required: float = 6.0

    def _skill_effect(self):
        """Decrease target health and decrease user stamina"""
        self.target.health_points_ -= self.damage
        self.user.stamina_points_ -= self.stamina_required
        return f'{self.user.name} применяет {self.user.unit_class.skill.name} и наносит {self.damage} урона сопернику.'
