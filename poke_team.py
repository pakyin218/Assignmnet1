from pokemon import *
import random
from typing import List

from data_structures.aset import ASet
from data_structures.referential_array import ArrayR


class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
   


    def __init__(self):
        self.team = ArrayR(self.TEAM_LIMIT)
        

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
    

    def assemble_team(self):
        raise NotImplementedError
    

    def special(self) -> None:
        raise NotImplementedError

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
        userinput = input("Random team\nManual team\n")

        if userinput == "Manual":
            self.TrainerTeam.choose_manually()
        elif userinput == "Random":
            self.TrainerTeam.choose_randomly()
        else:
            raise Exception("Not an option")     
            

    def get_team(self) -> PokeTeam:
        return self.TrainerTeam.team

    def get_name(self) -> str:
        return self.TrainerName

    def register_pokemon(self, pokemon: Pokemon) -> None:
        
        for i in range(self.pokedex.__len__()):
            if self.pokedex.__contains__(pokemon.get_poketype())==False:
                self.pokedex.add(pokemon.get_poketype())

    def get_pokedex_completion(self) -> float:
        counter=0
        for i in range(self.pokedex.__len__()):
            counter+=1
        return round(counter/15,2)

    def __str__(self) -> str:       
        return "Trainer <"+self.get_name()+"> Pokedex Completion: <"+str(self.get_pokedex_completion()*100)+">%"

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Manual")
    print(t)
    print(t.get_team())


    