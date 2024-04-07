from pokemon import *
import random
from typing import List
from battle_mode import BattleMode

from data_structures.aset import ASet
from data_structures.referential_array import ArrayR
from data_structures.stack_adt import ArrayStack
from data_structures.queue_adt import *
from data_structures.array_sorted_list import *


class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self):
        self.team = ArrayR(self.TEAM_LIMIT)
        self.team_count = 0

    def choose_manually(self):
        team_count = int(input("Enter the number of your Pokemon: "))
        self.team = ArrayR(team_count)
        if team_count > self.TEAM_LIMIT:
            print("Invaild number")
            self.choose_manually()
        else:    
            count = 0
            for i in self.POKE_LIST:
                print(str(count)+": "+i().get_name())
                count+=1
        
            for i in range(team_count):
                member = int(input("choose your pokemon: "))
                self.team.__setitem__(i,self.POKE_LIST[member])
                

    def choose_randomly(self) -> None:
        all_pokemon = get_all_pokemon_types()
        self.team_count = 0
        for i in range(self.TEAM_LIMIT):
            rand_int = random.randint(0, len(all_pokemon)-1)
            self.team[i] = all_pokemon[rand_int]()
            self.team_count += 1

    def regenerate_team(self) -> None:
        raise NotImplementedError
    
    def assign_team(self, criterion: str = None) -> None:
        tempSorted = ArraySortedList(self.team.__len__())
        if criterion == self.CRITERION_LIST[0]:  #health
            for i in range(self.team__len__()):
                tempSorted.add(ListItem(self.team[i].value(),self.team[i].value().get_health()))
            self.team = tempSorted

        elif criterion == self.CRITERION_LIST[1]:  #defense
            for i in range(self.team__len__()):
                tempSorted.add(ListItem(self.team[i].value(),self.team[i].value().get_defense()))
            self.team = tempSorted

        elif criterion == self.CRITERION_LIST[2]:  #batte_power
            for i in range(self.team__len__()):
                tempSorted.add(ListItem(self.team[i].value(),self.team[i].value().get_battle_power()))
            self.team = tempSorted

        elif criterion == self.CRITERION_LIST[3]:  #speed
            for i in range(self.team__len__()):
                tempSorted.add(ListItem(self.team[i].value(),self.team[i].value().get_speed()))
            self.team = tempSorted

        elif criterion == self.CRITERION_LIST[4]:  #level
            for i in range(self.team__len__()):
                tempSorted.add(ListItem(self.team[i].value(),self.team[i].value().get_level()))
            self.team = tempSorted

    
    def assemble_team(self, battle_mode: BattleMode) -> None:
        if battle_mode == BattleMode.SET:
            tempStack = ArrayStack(self.team.__len__())
            for i in range(self.team.__len__()):
                tempStack.push(self.team[i])
            self.team = tempStack   

        elif battle_mode == BattleMode.ROTATE:
            tempQueue = CircularQueue(self.team.__len__())
            for i in range(self.team.__len__()):
                tempQueue.append(self.team[i])
            self.team = tempQueue

        


    def special(self, battle_mode: BattleMode) -> None:
            if battle_mode == BattleMode.SET:
                tempS = ArrayStack(self.team.__len()//2)
                tempQ = CircularQueue(self.team.__len__())
                
                #push first 3 items(6th,5th,4th selected) in a temperory stack (tempS) (by popping self.team)
                for i in range(tempS.__len__()):
                    tempS.push(self.team.pop())

                #append remaining 3items in self.team to a temperory queue (tempQ) (by popping self.team)
                for i in range(tempQ.__len__()//2):
                    tempQ.serve(self.team.pop())

                #append first 3 items(6th,5th,4th selected) to temperory queue (tempQ) (by popping tempS)
                for i in range(tempS.__len__()):
                    tempQ.append(tempS.pop())
                
                #push all items in tempQ back to self.team (by serving tempQ)
                for i in range(tempQ.__len__()):
                    self.team.push(tempQ.serve())    

                
            elif battle_mode == BattleMode.ROTATE:
                temp = ArrayStack(self.team.__len__()//2)

                #append first 3 items to the back of the queue (by serving self.team)
                for i in range(0,self.team.__len__()//2): 
                    self.team.append(self.team.serve())

                #push bottom 3 items of self.team in a temperory stack (by serving self.team)
                for i in range(0,self.team.__len()//2):
                    temp.push(self.team.serve())

                #append those 3 item back to self.team-> [1,2,3,6,5,4] (by popping temp)
                for i in range(0,temp.__len__()):
                    self.team.append(temp.pop())

            #elif battle_mode == BattleMode.OPTIMISE:
                



                    
        

    def __getitem__(self, index: int):
        return self.team.__getitem__(index)

    def __len__(self):
        return self.team.__len__()

    def __str__(self):
        return self.team[0:]+"\n"

class Trainer:

    def __init__(self, name) -> None:
        self.TrainerName = name
        self.TrainerTeam = PokeTeam()
        self.pokedex = ASet(15)
        

    def pick_team(self, method: str) -> None:
        if method == "Manual":
            self.TrainerTeam.choose_manually()
        elif method == "Random":
            self.TrainerTeam.choose_randomly()
        else:
            raise Exception("Not an option")     
            

    def get_team(self) -> PokeTeam:
        return self.TrainerTeam.team

    def get_name(self) -> str:
        return self.TrainerName

    def register_pokemon(self, pokemon: Pokemon) -> None:
        self.pokedex.add(pokemon.get_poketype())
        

    def get_pokedex_completion(self) -> float:
        return round(self.pokedex.__len__()/15,2)

    def __str__(self) -> str:       
        return "Trainer "+self.get_name()+" Pokedex Completion: "+str(int(self.get_pokedex_completion()*100))+"%"

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    t.TrainerTeam.assemble_team(BattleMode.SET)
    t.TrainerTeam.special(BattleMode.SET)
    print(t)
    print(t.get_team())


    