from collections import defaultdict

def solution(genres, plays):
    answer = []
    hashTable = defaultdict(list)
    genreTable = defaultdict(int)
    
    for i in range(len(genres)):
        hashTable[genres[i]].append((i, plays[i]))
        genreTable[genres[i]] += plays[i]
    sortedGenreTable = sorted(genreTable.items(), key = lambda x: x[1], reverse=True)
    
    for genre, total in sortedGenreTable:
        hashTable[genre].sort(key = lambda x: x[1], reverse=True)
        for idx, play in enumerate(hashTable[genre]):
            if idx >= 2:
                break
            answer.append(play[0])
    
    return answer