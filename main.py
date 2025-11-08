from termcolor import colored
import random
import inquirer
import time
import os

def tobool(*args: str) -> bool:
    for item in args:
        if item.title() == "True":
            return True
        elif item.title() == "False":
            return False
        elif item.isspace() or item == '':
            return False
        elif item.isdigit():
            return True
        else:
            return False
    return False
def whitespaces(value: str) -> str:
    if not value.isspace():
        return value.replace(" ", '')
    else:
        raise ValueError("The value is empty!")
def islitbool (value) -> bool:
    if value.title() == "True": return True
    elif value.title() == "False": return False
    else: return False

def isbool(value):
    if value.title() == "True" or value.title() == "False":
        return True
    else:
        return False
def isfloat(value):
    try:
        value = str(value).split(".")
        if len(value[1]) < 1:
            return False
        else:
            return True
    except (ValueError, IndexError):
        return False
    
def smartdeconstruction(*args: str) -> list:
    e_list = []
    for sargs in args:
        if len(sargs) > 1:
            sargs = sargs.split(',')
        else:
            sargs = list(sargs)
        for i in sargs:
            if " " in i:
                i = whitespaces(i)
            if isfloat(i):
                i = float(i)
                e_list.append(i)
            elif i.isdigit():
                e_list.append(int(i))
            elif islitbool(i):
                e_list.append(tobool(i))
            else:
                e_list.append(i)
    return e_list

def randomnumlist(length : int) -> list[int]:
    random_list = []
    for _ in range(length):
        random_list.append(random.randint(1, 255))
    return random_list

def randomWordList(length : int) -> list[str]:
    with open('wordlist.txt', 'r') as file:
        return random.sample(file.read().split('\n'), length)
        
def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    option = inquirer.List(
        name="choose",
        message="Select the type of list to sort:",
        choices=['Numbers','Numbers [1k]', 'Words [COMMING SOON]', 'Custom [COMMING SOON]']
    )
    option = inquirer.prompt([option])
    if option['choose'] == 'Numbers':
        random_list = randomnumlist(100)
        
        print(colored(f"Unsorted List is -> {random_list}", 'yellow'))    
        
        from golf import golfsort
        start = time.time()
        
        finalList = golfsort(random_list)
        
        end = time.time()
    
    elif option['choose'] == 'Numbers [1k]':
        random_list = randomnumlist(1000)
        
        print(colored(f"Unsorted List is -> {random_list}", 'yellow'))    
        
        from golf import golfsort
        start = time.time()
        
        finalList = golfsort(random_list)
        
        end = time.time()
        
        
    elif option['choose'] == 'Words':
        from handleWordlist import handleWordlist
        
        random_list = randomWordList(100)
        
        print(colored(f"Unsorted List is -> {random_list}", 'yellow'))    
        
        from golf import golfsort
        
        start = time.time()
        
        finalList = golfsort(random_list)
        
        end = time.time()
        
    else:
        random_list = smartdeconstruction(input(colored("Enter your custom vector items separated by commas -> ", 'yellow')))
        from golf import golfsort
                
        start = time.time()
                
        finalList = golfsort(random_list)
                
        end = time.time()

    print(colored(f"Sorted List is -> {finalList}", 'green'))
    print(colored(f"Time taken to sort is -> {(end - start):.10f} seconds", 'cyan'))
if  __name__ == "__main__":
    main()
