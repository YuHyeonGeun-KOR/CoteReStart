def solution(files):
    answer = []
    fileList = []
    cnt = 0
    for f in files :
        index = 0
        head = ""
        num = ""
        tail = ""
        fList = list(f)
        for i in range(len(fList)):
            if not fList[i].isdigit():
                head += fList[i]
            else:
                index = i
                break
                
        for i in range(index , len(fList)):
            if fList[i].isdigit():
                num += fList[i]
            else:
                index = i
                break
                
        for i in range(index , len(fList)):
            tail += fList[i]
            
        print(head , num , tail)
        fileList.append([head.lower() , int(num) , tail ,cnt ,f])
        cnt +=1        
    
    ## [head, number , tail , 순서 , 원본문자열]
    
    fileList.sort(key = lambda x : (x[0] , x[1]  , x[3]))
    
    for result in fileList:
        answer.append(result[4])
    return answer