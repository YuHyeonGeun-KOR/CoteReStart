from collections import deque
def solution(m, musicinfos):
    answer = "(None)"
    length = -1
    for musicinfo in musicinfos :
        info = musicinfo.split(",")
        start = info[0].split(':')
        end = info[1].split(':')
        playTime = (int(end[0]) * 60  + int(end[1])) - (int(start[0]) * 60 + int(start[1]))
        name = info[2]
        melody = list(info[3])
        
        totalMelody = []
        index = 0
        count = 0
        
        origin = []
        while True :
            if index >= len(m) :
                break
            
            now = m[index]
            if index < len(m) -1 and m[index+1] == "#":
                now += m[index + 1]
                index +=1
            index +=1
            
            
            origin.append(now)
            
            
        index = 0
        
        while True :
            if index >= len(melody) :
                index = 0
            if count == playTime :  break;
            
            now = melody[index]
            if index < len(melody) -1 and melody[index+1] == "#":
                now += melody[index + 1]
                index +=1
            index +=1
            
            
            totalMelody.append(now)
            count +=1
            
        for i in range(len(totalMelody)) :
            endindex = 0
            if totalMelody[i] == origin[0]:
                mCount = 0
                for j in range(len(origin)):
                    if(i + j) >= len(totalMelody) : break;
                    
                    if totalMelody[i+j] == origin[j] : 
                        mCount +=1
                    else : 
                        break
                if mCount == len(origin) and length < playTime:
                    answer = name
                    length = playTime
                    
        
            
    return answer