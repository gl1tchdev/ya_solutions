from collections import defaultdict

order_cost: defaultdict[int] = defaultdict(int)
order_duration: defaultdict[int] = defaultdict(int)

with open('input.txt', 'r') as r, open('output.txt', 'w') as w:
    orders_count = int(r.readline())
    for _ in range(orders_count):
        data = [int(s) for s in r.readline().split()]
        order_cost[data[0]] += data[2]
        order_duration[data[1]] += data[1] - data[0]
    query_count = int(r.readline())
    for _ in range(query_count):
        data = tuple(int(s) for s in r.readline().split())
        if data[2] == 1:
            result = sum(value for key, value in order_cost.items() if data[0] <= key <= data[1])
        else:
            result = sum(value for key, value in order_duration.items() if data[0] <= key <= data[1])
        w.write(f'{result} ')