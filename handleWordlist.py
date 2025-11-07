def handleWordlist(wordlist : list[str], modifywordlist : list[str]) -> list[int]:
    alpha_dict = {
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7,
        'i' : 8,
        'j' : 9,
        'k' : 10,
        'l' : 11,
        'm' : 12,
        'n' : 13,
        'o' : 14,
        'p' : 15,
        'q' : 16,
        'r' : 17,
        's' : 18,
        't' : 19,
        'u' : 20,
        'v' : 21,
        'w' : 22,
        'x' : 23,
        'y' : 24,
        'z' : 25
    }
    
    for i in wordlist:
        k = list(i)
        for j in k:
            for a in alpha_dict:
                if j == a:
                    k[k.index(a)] = str(alpha_dict[j])
                    break
        
        for format in k:
            if format.isdigit():
                k[k.index(format)] = int(format)
                
        modifywordlist[wordlist.index(i)] = k
        
        
    return modifywordlist