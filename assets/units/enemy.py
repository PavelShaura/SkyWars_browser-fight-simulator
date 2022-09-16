from random import randint

from assets.units import BaseUnit


class Enemy(BaseUnit):

    def attack(self, target: BaseUnit) -> str:
        """Computer Attack logic

        if skill don't used - calculate random chance and use special skill
        else use usual attack
        """

        if not self.skill_used:
            use_skill = randint(0, 9)
            if use_skill == 0:
                return self.use_skill(target)

        return super().attack(target)
