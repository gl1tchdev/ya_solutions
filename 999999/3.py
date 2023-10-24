with open('input.txt', 'r') as r, open('output.txt', 'w') as w:
    N, M, Q = r.readline().split()
    columns = r.readline().split()
    column_indexes = dict(zip(columns, range(len(columns))))
    table = []
    for _ in range(int(N)):
        values = [int(s) for s in r.readline().split()]
        table.append(values)
    temp = []
    for _ in range(int(Q)):
        column, operand, value = r.readline().split()
        target = table if not temp else temp
        targets = []
        for row in target:
            column_index = column_indexes[column]
            q_eval = f'{row[column_index]} {operand} {int(value)}'
            result = eval(q_eval)
            if not result:
                targets.append(row)
        for t in targets:
            target.remove(t)
    total = sum(sum(row) for row in target)
    w.write(str(total))