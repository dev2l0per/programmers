from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for i in range(len(progresses)):
        queue.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    cnt = 0
    top = queue[0]
    while queue:
        cur = queue.popleft()
        if cur > top:
            top = cur
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
        if not queue:
            answer.append(cnt)
    
    return answer