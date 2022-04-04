def solution(clothes):
    answer = 1
    
    passionDict = {}
    
    for wear in clothes:
        if wear[1] not in passionDict:
            passionDict[wear[1]] = []
        passionDict[wear[1]].append(wear[0])
    for val in passionDict.values():
        answer = answer * (len(val) + 1)
    
    return answer - 1