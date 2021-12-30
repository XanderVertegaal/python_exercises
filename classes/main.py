# Do not modify these lines
__winc_id__ = "04da020dedb24d42adf41382a231b1ed"
__human_name__ = "classes"

# Add your code after this line
from typing import Literal


def exception_raiser(exception):
    raise exception


class Player:
    def __init__(self, name: str, speed: float, endurance: float, accuracy: float):
        self.name = name
        self.speed = speed if 0 <= speed <= 1 else exception_raiser(ValueError)
        self.endurance = (
            endurance if 0 <= endurance <= 1 else exception_raiser(ValueError)
        )
        self.accuracy = accuracy if 0 <= accuracy <= 1 else exception_raiser(ValueError)

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        player_obj = self.__dict__
        highest_value = max([self.speed, self.endurance, self.accuracy])
        for key in ["speed", "endurance", "accuracy"]:
            if player_obj[key] == highest_value:
                return (key, highest_value)


class Commentator:
    def __init__(self, name: str):
        self.name = name

    def sum_player(self, player: Player) -> float:
        return player.speed + player.endurance + player.accuracy

    def compare_players(
        self,
        player1: Player,
        player2: Player,
        attribute: Literal["speed", "endurance", "accuracy"],
    ) -> str:
        if player1.__dict__[attribute] > player2.__dict__[attribute]:
            return player1.name
        if player1.__dict__[attribute] < player2.__dict__[attribute]:
            return player2.name

        if player1.strength()[1] > player2.strength()[1]:
            return player1.name
        if player1.strength()[1] < player2.strength()[1]:
            return player2.name

        if self.sum_player(player=player1) > self.sum_player(player=player2):
            return player1.name
        if self.sum_player(player=player1) < self.sum_player(player=player2):
            return player2.name

        else:
            return "These two players might as well be twins!"


marco = Player(name="Marco", speed=0.5, endurance=0.4, accuracy=0.6)
tessa = Player(name="Tessa", speed=0.5, endurance=0.3, accuracy=0.8)

ray = Commentator(name="Ray Hudson")
print(ray.compare_players(player1=marco, player2=tessa, attribute="speed"))
