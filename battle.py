from __future__ import annotations
from poke_team import Trainer, PokeTeam
from typing import Tuple
from battle_mode import BattleMode


from data_structures.stack_adt import Stack
from data_structures.queue_adt import CircularQueue

class Battle:

    def __init__(self, trainer_1: Trainer, trainer_2: Trainer, battle_mode: BattleMode, criterion = "health") -> None:
        self.t1 = trainer_1
        self.t2 = trainer_2
        self.bm = battle_mode
        self.criterion = criterion

    def commence_battle(self) -> Trainer | None:
        if self.bm == BattleMode.SET:
            print
        elif self.bm == BattleMode.ROTATE:
            print
        else:
            print
        

    def _create_teams(self, battle_mode: BattleMode , criterion: None) -> None:
        if battle_mode == BattleMode.SET:

            t1.pick_team("Random")
            t2.pick_team("Random")

        elif battle_mode == BattleMode.ROTATE:

            t1.pick_team("Random")
            t2.pick_team("Random")

        elif battle_mode == BattleMode.OPTIMISE:
            t1.pick_team("Random")
            t2.pick_team("Random")    


        raise NotImplementedError

    def set_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def rotate_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def optimise_battle(self) -> PokeTeam | None:
        raise NotImplementedError


if __name__ == '__main__':
    t1 = Trainer('Ash')
    t1.pick_team("random")

    t2 = Trainer('Gary')
    t2.pick_team('random')
    b = Battle(t1, t2, BattleMode.ROTATE)
    winner = b.commence_battle()

    if winner is None:
        print("Its a draw")
    else:
        print(f"The winner is {winner.get_name()}")
