def solution(msg):
    mylist = {}
    answer = []
    index = 1
    for i in range(ord("A") , ord("Z") +1 ) :
        mylist[chr(i)] = index
        index +=1
        
    
    now = msg[0]
    start = 0
    while True :
        if(start >= len(msg)) : break
        
        checkStart = start
        checkNow = msg[checkStart]
        
        while True :
            if mylist.get(checkNow) != None :
                checkStart += 1
                start +=1
                if(checkStart < len(msg)):
                    checkNow += msg[checkStart] 
                elif checkStart == len(msg) : 
                    answer.append(mylist.get(checkNow))
                    break
            elif mylist.get(checkNow) == None:
                answer.append(mylist[checkNow[:-1]])
                mylist[checkNow] = len(mylist) + 1
                break;
        
        
    
    
    return answer