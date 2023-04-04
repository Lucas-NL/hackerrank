   for i in range(0, int(0.5*len(s))):
        if s[i] != s[end - i]:
            if s[i] == s[end -1 - i] and s[i] != s[i + 2]:
                exc_ind = end - i
                print(exc_ind, s[exc_ind])
                return exc_ind, s[exc_ind]
            elif s[end - i] == s[i+1] and s[end - i] != s[end - 2]:
                exc_ind = i
                print(exc_ind, s[exc_ind])
                return exc_ind, s[exc_ind]

    return -1    
    
    
    # tem um bug bizarro aqui qnd eu tento mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm
