from pokemon import *
import random
from typing import List

class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    pokedex = ArrayR(len(PokeType))


    def __init__(self):
        raise NotImplementedError

    def choose_manually(self):
        pokeNum = input("Enter the number of your Pokemon")
        self.team = ArrayR(len(pokeNum))

        for count in range(0,self.POKE_LIST.__len__()):
            print(count+1+": \n"+self.POKE_LIST)
        for i in range(0,pokeNum):
            choice = input("Choose your "+i+"th Pokemon")
            self.team.__setitem__(i,self.POKE_LIST[choice+1])
                
    def choose_randomly(self) -> None:
        all_pokemon = get_all_pokemon_types()
        self.team_count = 0
        for i in range(self.TEAM_LIMIT):
            rand_int = random.randint(0, len(all_pokemon)-1)
            self.team[i] = all_pokemon[rand_int]()
            self.team_count += 1

    def regenerate_team(self) -> None:
        raise NotImplementedError
    
    def special(self) -> None:
        raise NotImplementedError

    def __getitem__(self, index: int):
        return self.team[index]

    def __len__(self):
        return self.len(self.team)

    def __str__(self):
        return self.team[0:]+"\n"

class Trainer:

    def __init__(self, name) -> None:
        self.name = name
        

    def pick_team(self, method: str) -> None:
        userinput = input("[R]Random team\n[M]Manual team")

        if userinput == "M" or "m":
            PokeTeam.choose_manually
        elif userinput == "R" or "r":
            PokeTeam.choose_randomly
        else:
            raise Exception("Not an option")     
            

    def get_team(self) -> PokeTeam:
        raise self.__str__

    def get_name(self) -> str:
        raise self.name

    def register_pokemon(self, pokemon: Pokemon) -> None:
        
        for i in range(PokeTeam.pokedex.__len__):
            if PokeTeam.pokedex[i]!=pokemon.get_poketype:
                PokeTeam.pokedex.__setitem__(pokemon.get_poketype)
        

    

    def get_pokedex_completion(self) -> float:
        counter =0
        for i in range(PokeTeam.pokedex.__len__):
            if PokeTeam.pokedex[i] in PokeType:
                counter+=1

        return round(counter/15,2)

    def __str__(self) -> str:       
        return "Trainer <"+Trainer.get_name+"> Pokedex Completion: <"+Trainer.get_pokedex_completion*100+">%"

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())


    