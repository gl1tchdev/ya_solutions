from collections import Counter

def solution(J: str, S: str):
    counter_J = Counter(J)
    counter_S = Counter(S)
    total_count = 0
    for key, value in counter_S.items():
        if key in counter_J.keys():
            total_count += value
    return total_count
    

print(solution('ab', 'aabbccd'))