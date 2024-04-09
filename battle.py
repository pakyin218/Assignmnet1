from __future__ import annotations
from poke_team import Trainer, PokeTeam
from typing import Tuple
from battle_mode import BattleMode
import math
from data_structures.stack_adt import ArrayStack
from data_structures.queue_adt import CircularQueue


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
        

    def _create_teams(self, battle_mode: BattleMode) -> None:
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
            t1.TrainerTeam.assign_team(BattleMode.OPTIMISE)
            t2.TrainerTeam.assign_team(BattleMode.OPTIMISE)    


        

    def set_battle(self) -> PokeTeam | None:
        endcondition = False
        p1 = self.t1.get_team().team.pop()
        p2 = self.t2.get_team().team.pop()

        while endcondition == False:
            round = 1
            attack_damage = 0
            

            print("--------------------------------\n")
            print("\tRound"+str(round)+"\n")
            print("--------------------------------\n")

            #register pokemon before round start
            self.t1.register_pokemon(p1)
            self.t1.register_pokemon(p2)
            self.t2.register_pokemon(p1)
            self.t2.register_pokemon(p2)

            #check speed then attack/defend
            if p1.get_speed() > p2.get_speed(): #p1 is faster than p2
                attack_damage= math.ceil(p1.attack(p2)*(self.t1.get_pokedex_completion()/self.t2.get_pokedex_completion()))
                p2.defend(attack_damage)
                if p2.get_health()<=0:
                    p1.level_up()
                    p2 = self.t2.get_team().team.pop()
                    #End round
                else:
                    #slower speed pokemon(p2) retort back p2att p1def
                    attack_damage= math.ceil(p2.attack(p1)*(self.t2.get_pokedex_completion()/self.t1.get_pokedex_completion()))
                    p1.defend(attack_damage)
                    if p1.get_health()<=0:
                        p2.level_up()
                        p1 = self.t1.get_team().team.pop()
                        #End round

            elif p2.get_speed() > p1.get_speed(): #p2 is faster than p1
                attack_damage= math.ceil(p2.attack(p1)*(self.t2.get_pokedex_completion()/self.t1.get_pokedex_completion()))
                p1.defend(attack_damage)
                if p1.get_health()<=0:
                    p2.level_up()
                    p1 = self.t1.get_team().team.pop()
                    #End round
                else:
                    #slower speed pokemon(p1) retort back p1att p2def
                    attack_damage= math.ceil(p1.attack(p2)*(self.t1.get_pokedex_completion()/self.t2.get_pokedex_completion()))
                    p2.defend(attack_damage)
                    if p2.get_health()<=0:
                        p1.level_up()
                        p2 = self.t2.get_team().team.pop()
                        #End Round   

            elif p1.get_speed() == p2.get_speed() : #same speed
                attack_damage= math.ceil(p1.attack(p2)*(self.t1.get_pokedex_completion()/self.t2.get_pokedex_completion()))
                p2.defend(attack_damage)
                attack_damage= math.ceil(p2.attack(p1)*(self.t2.get_pokedex_completion()/self.t1.get_pokedex_completion()))
                p1.defend(attack_damage)

                if p1.get_health()<=0 and p2.get_health()<=0: #both die
                    p2 = self.t2.get_team().team.pop()
                    p1 = self.t1.get_team().team.pop()

                elif p1.get_health()<=0 and p2.get_health()>0: #p1 die and p2 alive
                    p2.level_up()
                    p1 = self.t1.get_team().team.pop()

                elif p2.get_health()>0 and p2.get_health()<=0: #p1 alive and p2 die
                    p1.level_up()
                    p2 = self.t2.get_team().team.pop()

                elif p1.get_health()>0 and p2.get_health()>0: #both alive -> both reduce 1 damage    
                    p1.defend(1)
                    p2.defend(1)
                    if p1.get_health()<=0 and p2.get_health()>0: #p1 die and p2 alive by 1 damage
                        p2.level_up()
                        p1 = self.t1.get_team().team.pop()
                    elif p2.get_health()>0 and p2.get_health()<=0: #p1 alive and p2 die by 1 damage
                        p1.level_up()
                        p2 = self.t2.get_team().team.pop()
                    elif p1.get_health()<=0 and p2.get_health()<=0: #both die by 1 damage
                        p1 = self.t1.get_team().team.pop()
                        p2 = self.t2.get_team().team.pop()   
                        


            
            print("--------------------------------\n")
            print("\t\tEnd of Round"+str(round)+"\n")
            print("--------------------------------\n")
            round +=1
            #check if any triners' pokemon all faint out
            if self.t1.TrainerTeam.__len__()==0 or self.t2.TrainerTeam.__len__() == 0:
                endcondition == True


    def rotate_battle(self) -> PokeTeam | None:
        endcondition = False
        p1 = self.t1.get_team().team.serve()
        p2 = self.t2.get_team().team.serve()
        while endcondition == False:
            round = 1
            attack_damage = 0

            print("--------------------------------\n")
            print("\t     Round"+str(round)+"\n")
            print("--------------------------------\n")
            self.t1.register_pokemon(p1)
            self.t1.register_pokemon(p2)
            self.t2.register_pokemon(p1)
            self.t2.register_pokemon(p2)
            if p1.get_speed() > p2.get_speed(): #p1 is faster than p2
                attack_damage= math.ceil(p1.attack(p2)*(self.t1.get_pokedex_completion()/self.t2.get_pokedex_completion()))
                p2.defend(attack_damage)
                if p2.get_health()<=0: #p2 Die after p1 attack
                    p1.level_up()
                    p2 = self.t2.get_team().team.serve()
                    self.t1.get_team().team.append(p1) 
                elif p2.get_health>0: #p2 alive after p1 attack

                    #slower speed pokemon(p2) retort back p2att p1def
                    attack_damage= math.ceil(p2.attack(p1)*(self.t2.get_pokedex_completion()/self.t1.get_pokedex_completion()))
                    p1.defend(attack_damage)
                    if p1.get_health()<=0:
                        p2.level_up()
                        p1 = self.t1.get_team().team.serve()
                        self.t2.get_team().team.append(p2)
                    elif p1.get_health()>0:
                        self.t1.get_team().team.append(p1)
                        self.t2.get_team().team.append(p2)

            elif p2.get_speed() > p1.get_speed(): #p2 is faster than p1
                attack_damage= math.ceil(p2.attack(p1)*(self.t2.get_pokedex_completion()/self.t1.get_pokedex_completion()))
                p1.defend(attack_damage)
                if p1.get_health()<=0:
                    p2.level_up()
                    p1 = self.t1.get_team().team.serve()
                    self.t2.get_team().team.append(p2)
                    
                else:
                    #slower speed pokemon(p1) retort back p1att p2def
                    attack_damage= math.ceil(p1.attack(p2)*(self.t1.get_pokedex_completion()/self.t2.get_pokedex_completion()))
                    p2.defend(attack_damage)
                    if p2.get_health()<=0:
                        p1.level_up()
                        p2 = self.t2.get_team().team.serve()
                        self.t1.get_team().team.append(p1)
                    elif p2.get_health()>0:
                        
                        self.t2.get_team().team.append(p2)
                        self.t1.get_team().team.append(p1)
                          
            elif p1.get_speed() == p2.get_speed() : #same speed
                attack_damage= math.ceil(p1.attack(p2)*(self.t1.get_pokedex_completion()/self.t2.get_pokedex_completion()))
                p2.defend(attack_damage)
                attack_damage= math.ceil(p2.attack(p1)*(self.t2.get_pokedex_completion()/self.t1.get_pokedex_completion()))
                p1.defend(attack_damage)

                if p1.get_health()<=0 and p2.get_health()<=0: #both die
                    p2 = self.t2.get_team().team.serve()
                    p1 = self.t1.get_team().team.serve()

                elif p1.get_health()<=0 and p2.get_health()>0: #p1 die and p2 alive
                    p2.level_up()
                    p1 = self.t1.get_team().team.serve()
                    self.t2.get_team().team.append(p2)

                elif p2.get_health()>0 and p2.get_health()<=0: #p1 alive and p2 die
                    p1.level_up()
                    p2 = self.t2.get_team().team.serve()
                    self.t1.get_team().team.append(p1)

                elif p1.get_health()>0 and p2.get_health()>0: #both alive -> both reduce 1 damage    
                    p1.defend(1)
                    p2.defend(1)
                    if p1.get_health()<=0 and p2.get_health()>0: #p1 die and p2 alive by 1 damage
                        p2.level_up()
                        p1 = self.t1.get_team().team.serve()
                        self.t2.get_team().team.append(p2)

                    elif p2.get_health()>0 and p2.get_health()<=0: #p1 alive and p2 die by 1 damage
                        p1.level_up()
                        p2 = self.t2.get_team().team.serve()
                        self.t1.get_team().team.append(p1)

                    elif p1.get_health()<=0 and p2.get_health()<=0: #both die by 1 damage
                        p1 = self.t1.get_team().team.serve()
                        p2 = self.t2.get_team().team.serve() 

                    elif p1.get_health()>0 and p2.get_health()>0: #both alive by 1 damage
                        self.t1.get_team().team.append(p1)
                        self.t2.get_team().team.append(p2)

            print("--------------------------------\n")
            print("\t\tEnd of Round"+str(round)+"\n")
            print("--------------------------------\n")
            round +=1
            #check if any triners' pokemon all faint out
            if self.t1.TrainerTeam.__len__()==0 or self.t2.TrainerTeam.__len__() == 0:
                endcondition == True    

        

    def optimise_battle(self) -> PokeTeam | None:
        raise NotImplementedError


if __name__ == '__main__':
    t1 = Trainer('Ash')
    t1.pick_team("Random")

    t2 = Trainer('Gary')
    t2.pick_team('Random')
    b = Battle(t1, t2, BattleMode.ROTATE)
    winner = b.commence_battle()

    if winner is None:
        print("Its a draw")
    else:
        print(f"The winner is {winner.get_name()}")
