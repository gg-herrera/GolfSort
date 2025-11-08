from termcolor import colored
from playsound import playsound
def printout(text : str) -> None:
    playsound('./sounds/click0.wav')
    print(colored(f"[+] {text}", 'blue'))

def printwar(text : str) -> None:
    warning = AudioSegment('./sounds/warning.wav')
    play(warning)
    print(colored(f"[!] {text}", 'light_yellow'))

def printerr(text : str) -> None:
    error = AudioSegment('./sounds/error.wav')
    play(error)
    print(colored(f"[-] {text}", 'red'))

def divideToPairs(ls: list[int], rs: list[int]) -> list[list[int]]:
    pairs = []
    printout("setting pairs...")
    left, right = 0, len(rs) - 1

    while left < len(ls) and right >= 0:
        pair = [ls[left], rs[right]]
        printout(f"creating pair with {[ls[left], [rs[right]]]}")
        pair.sort()
        printout(f"sorting pairs...")
        pairs.append(pair)
        left += 1
        right -= 1
    

    while left < len(ls):
        if left + 1 < len(ls):
            pair = [ls[left], ls[left + 1]]
            printout(f"splitting pairs with {[ls[left], ls[left + 1]]}")
            pair.sort()
            pairs.append(pair)
            left += 2
        else:
            pairs.append([ls[left]])
            printout(f"setting an alone number with {[ls[left]]}")
            left += 1

    while right >= 0:
        if right - 1 >= 0:
            pair = [rs[right - 1], rs[right]]
            printout(f"splitting pairs with {[rs[right], rs[right + 1]]}")
            pair.sort()
            pairs.append(pair)
            right -= 2
        else:
            printout(f"setting an alone number with {[rs[right]]}")
            pairs.append([rs[right]])
            right -= 1
    printout("Returning pairs...")
    return pairs

def bubbleGolfSort(pairs: list[list[int]]) -> list[list[int]]:
    def key(pair: list) -> any:
        if isinstance(pair, list):
            s = sum(pair)
            mn = min(pair)
            mx = max(pair)
            return (s, mn, mx)
        else:
            return (pair, pair, pair)
    
    for i in range(len(pairs)):
        swapped = False
        for j in range(0, len(pairs) - i - 1):
            if key(pairs[j]) > key(pairs[j+1]):
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                swapped = True
        if not swapped:
            break
    return pairs

def golfsort(unsorted_list: list[int]) -> list[int]:
        
    if len(unsorted_list) <= 1:
        return unsorted_list.copy()
    
    working_list = unsorted_list.copy()
    leftSide, rightSide = [], []
    
    mid = len(working_list) // 2
    
    while len(leftSide) < mid:
        leftSide.append(working_list.pop(0))
    
    while len(rightSide) < mid:
        rightSide.append(working_list.pop(-1))
    
    if len(working_list) > 0:
        if sum(leftSide) >= sum(rightSide):
            leftSide.append(working_list[0])
        else:
            rightSide.append(working_list[0])
    pairs = divideToPairs(leftSide, rightSide)
    bubbleGolfSort(pairs)
    
    result = [x for pair in pairs for x in pair]
    
    if all(result[i] <= result[i+1] for i in range(len(result)-1)):
        return result
    
    if count_inversions(result) >= count_inversions(unsorted_list):
        return sorted(unsorted_list)
    
    return golfsort(result)

def count_inversions(lst: list[int]) -> int:
    inversions = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                inversions += 1
    return inversions
