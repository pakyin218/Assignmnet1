from __future__ import annotations
from poke_team import Trainer, PokeTeam
from typing import Tuple
from battle_mode import BattleMode

class Battle:

    def __init__(self, trainer_1: Trainer, trainer_2: Trainer, battle_mode: BattleMode, criterion = "health") -> None:
        self.t1 = trainer_1
        self.t2 = trainer_2
        self.bm = battle_mode
        self.criterion = criterion

    def commence_battle(self) -> Trainer | None:
        if self.bm == BattleMode.SET:
            self._create_teams(BattleMode.SET)
            self.set_battle()

            if t1.TrainerTeam.__len__() == 0:
                print("The winner is "+t2.get_name())
            elif t2.TrainerTeam.__len__() == 0:
                print("The winner is "+t1.get_name())    
            else:
                print("draw")    
        elif self.bm == BattleMode.ROTATE:
            self._create_teams(BattleMode.ROTATE)
            self.rotate_battle()
            
            if t1.TrainerTeam.__len__() == 0:
                print("The winner is "+t2.get_name())
            elif t2.TrainerTeam.__len__() == 0:
                print("The winner is "+t1.get_name())    
            else:
                print("draw") 
        elif self.bm == BattleMode.OPTIMISE:
            self._create_teams(BattleMode.OPTIMISE)
            self.optimise_battle()

            if t1.TrainerTeam.__len__() == 0:
                print("The winner is "+t2.get_name())
            elif t2.TrainerTeam.__len__() == 0:
                print("The winner is "+t1.get_name())    
            else:
                print("Its a draw") 
        

    def _create_teams(self, battle_mode: BattleMode , criterion: None) -> None:
        if battle_mode == BattleMode.SET:
            t1.pick_team("Random")
            t2.pick_team("Random")
            t1.TrainerTeam.assemble_team(BattleMode.SET)
            t2.TrainerTeam.assemble_team(BattleMode.SET)

        elif battle_mode == BattleMode.ROTATE:
            t1.pick_team("Random")
            t2.pick_team("Random")
            t1.TrainerTeam.assemble_team(BattleMode.ROTATE)
            t2.TrainerTeam.assemble_team(BattleMode.ROTATE)

        elif battle_mode == BattleMode.OPTIMISE:
            t1.pick_team("Random")
            t2.pick_team("Random")
            t1.TrainerTeam.assign_team(BattleMode.OPTIMISE,criterion)
            t2.TrainerTeam.assign_team(BattleMode.OPTIMISE,criterion)    


        

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
