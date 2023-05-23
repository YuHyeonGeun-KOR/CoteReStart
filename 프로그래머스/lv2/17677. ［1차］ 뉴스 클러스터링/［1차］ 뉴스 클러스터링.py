def solution(str1, str2):
    answer = 0
    check = set()
    checkOne = []
    checkTwo  = []
    checker = ""
    for s in str1:
        if s.isalpha():
            checker += s.lower()
        else :
            checker = ""
            continue
            
        if len(checker) == 2:
            check.add(checker)
            checkOne.append(checker)
            checker = checker[1:]
    checker = ""
    for s in str2:
        if s.isalpha():
            checker += s.lower()
        else :
            checker = ""
            continue
            
        if len(checker) == 2:
            check.add(checker)
            checkTwo.append(checker)
            checker = checker[1:]
    
    minSet = 0
    maxSet = 0
    print(checkOne ,checkTwo )
    for s in check:
        mincheck = min(checkOne.count(s) , checkTwo.count(s))
        if mincheck != 0:
            minSet += mincheck
        
        maxcheck = max(checkOne.count(s) , checkTwo.count(s))
        if maxcheck != 0:
            maxSet += maxcheck
    print(minSet , maxSet)
    result = 0
    
    if maxSet == 0:
        return 65536
    else:
        return int((minSet / maxSet) * 65536)