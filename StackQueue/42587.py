from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    for idx, val in enumerate(priorities):
        queue.append((val, idx))
    
    while queue:
        cur = queue.popleft()
        if queue and max(queue)[0] > cur[0]:
            queue.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                break
    
    return answer