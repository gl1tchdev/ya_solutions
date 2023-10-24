from collections import defaultdict


def str_to_dict(st: str) -> defaultdict:
    out = defaultdict(int)
    for s in st:
        out[s] += 1
    return out


with open('input.txt', 'r') as r, open('output.txt', 'w') as w:
    first = r.readline().replace('\n', ' ')
    second = r.readline().replace('\n', ' ')
    result = str_to_dict(first) == str_to_dict(second)
    w.write(f'{int(result)}')
