def solution(participant, completion):
    hashMap = dict()
    
    for part in participant:
        if part not in hashMap:
            hashMap[part] = 0
        hashMap[part] += 1
    
    for comp in completion:
        hashMap[comp] -= 1
    
    for miss in hashMap:
        if hashMap[miss] == 1:
            return miss