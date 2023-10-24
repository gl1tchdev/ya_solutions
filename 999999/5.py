def find_similarity(arr1: list, arr2: list):
    total = 0
    counter = min(len(arr1), len(arr2))
    for i in range(counter + 1):
        a1_slice = arr1[:i]
        a2_slice = arr2[:i]
        if a1_slice == a2_slice:
            current = len(a1_slice)
            total = max(current, total)
    return total


arrs = []
summary = 0
is_even = lambda i: (i % 2) == 0
with open('input.txt', 'r') as r, open('output.txt', 'w') as w:
    arr_count = int(r.readline().replace('\n', ' ')) * 2
    for i in range(arr_count):
        input_data = r.readline().split()
        if is_even(i):
            continue
        data = [int(s) for s in input_data]
        arrs.append(data)
    for i in range(0, len(arrs)):
        for k in range(i, len(arrs)):
            if i == k:
                continue
            summary += find_similarity(arrs[i], arrs[k])
    w.write(f'{summary}')
