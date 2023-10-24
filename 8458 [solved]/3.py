def solution():
    with open('../input.txt', 'r') as r, open('../output.txt', 'w') as w:
        arr_len = int(r.readline())
        index = last_num = num = 0
        while index != arr_len:
            num = int(r.readline())
            if (not index) or (num != last_num):
                w.write(f'{num}\n')
                last_num = num
            index += 1
print('Вывод ', solution())