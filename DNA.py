import random
from pprint import pprint
import os
import time
from rich.console import Console


class virus:
    
    def __init__(self,DNAinput = ""):
        self.DNA_rand = 0
        self.DNA_let = ""
        if len(DNAinput) >= 49:
            self.DNA = DNAinput
        else:
            self.DNA = ""
            for i in range(0, 50):
                self.DNA_rand = random.randint(0,3)
                if self.DNA_rand == 0:
                    self.DNA_let = "A"
                    self.DNA += self.DNA_let
                elif self.DNA_rand == 1:
                    self.DNA_let = "G"
                    self.DNA += self.DNA_let
                elif self.DNA_rand == 2:
                    self.DNA_let = "T"
                    self.DNA += self.DNA_let
                elif self.DNA_rand == 3:
                    self.DNA_let = "C"
                    self.DNA += self.DNA_let
        self.DNA = str(self.DNA)
    def getDNA(self):
        return self.DNA

    def replicate(self):
        rep = random.randint(1,100)
        DNA_let_list = ["A", "C", "T", "G"]
        if rep > 94:
            mutate_num = random.randint(0,49)
            random.shuffle(DNA_let_list)
            randomLetter = DNA_let_list[0]
            DNA_list = list(self.DNA)
            
            DNA_list[mutate_num] = randomLetter
            
            mutated_DNA = "".join(DNA_list)
            x = virus(mutated_DNA)
            return x
        elif rep <= 94:
            x = virus(self.DNA)
            return x
def find_mutation(virus1,virus2):
    DNA1 = virus1
    DNA2 = virus2

    DNA1_list = list(DNA1)
    DNA2_list = list(DNA2)
    newList = []
    for i in range(0,50):
        if DNA1_list[i] != DNA2_list[i]:
            newList.append("^")
        else:
            newList.append(" ")
    differenceString = "".join(newList)
    differenceNum = differenceString.count("^")
    return differenceString, differenceNum

def DNAProcess():
    repeat = True
    while repeat == True:
        name = input("Name of virus: ")
        my_virus = virus()
        original_virus = my_virus
        print(f"Original DNA sequence: {original_virus.getDNA()}")
        N = int(input("How many times to replicate? "))
        for i in range(0, N):
            my_virus = my_virus.replicate()
            new_virus_sequence = my_virus.getDNA()
            print(f"Replica [  {i}] DNA sequence: {new_virus_sequence}")
        print(f"Comparing latest {name} virus to the original {name}.")
        print(original_virus.getDNA())
        print(my_virus.getDNA())
        differenceString, differenceNum = find_mutation(original_virus.getDNA(),my_virus.getDNA())
        print(differenceString)
        if differenceNum == 0:
            print("No mutations detected")
        elif differenceNum <= 5:
            print(f"{differenceNum} mutations -- virus is the same.")
        elif differenceNum > 5:
            print(f"{differenceNum} mutations -- a *new* virus has been created.")
        yn = input("Try again? ").upper()
        if yn == "Y":
            repeat = True
        else:
            repeat = False

    pass

def DNACombination():
    while True:
        my_list = ["A", "C", "T", "G"]
        rand = random.Random()

        list2 = []

        n = int(input("Size of the DNA Strings?: "))
        while len(list2) < (4 ** n):
            temp = ""
            while len(temp) < n:
                temp += random.choice(my_list)
            if temp not in list2:
                list2.append(temp)
                temp = ""
            else:
                temp = ""
        

        list2.sort()
        console = Console()

        for item in list2:
            console.print(f"[blue]•[/blue] {item}")

        yn = input("Try again? ").upper()
        if yn == "Y":
            True
        else:
            break

def menu2(selected_option):
    os.system("clear" if os.name == "posix" else "cls") 

    print("╔══════════════════════════════╗")
    print(f"║            Menu              ║")
    print("╠══════════════════════════════╣")
    print(f"║ 1. {'[X]' if selected_option == 1 else '[ ]'} Generate DNA Combos   ║")
    print(f"║ 2. {'[X]' if selected_option == 2 else '[ ]'} DNA Combination       ║")
    print(f"║ 3. {'[X]' if selected_option == 3 else '[ ]'} Quit                  ║")
    print("╚══════════════════════════════╝")
    

def menu3():
    selected_option = 1

    while True:
        menu2(selected_option)
        time.sleep(0.1)

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            selected_option = 1
            menu2(selected_option)  
            DNAProcess()
        elif choice == "2":
            selected_option = 2
            menu2(selected_option)  
            DNACombination()
        elif choice == "3":
            selected_option = 3
            menu2(selected_option)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    menu3()

if __name__ == "__main__":
    main()