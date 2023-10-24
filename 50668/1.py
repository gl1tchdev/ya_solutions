from collections import Counter

with open('../input.txt', 'r') as r, open('../output.txt', 'w') as w:
    candidates = int(r.readline())
    for i in range(candidates):
        data = r.readline()
        data = data.split(',')
        letters_in_name = Counter(data[0] + data[1] + data[2])
        letters_count = len(letters_in_name.keys())
        first_letter_number = ord(data[0][0].lower()) & 31
        sum_in_date = sum([int(s) for s in (data[3] + data[4])])
        total = letters_count + (sum_in_date * 64) + (first_letter_number * 256)
        total_converted = str(hex(total))
        result = total_converted[len(total_converted) - 3:]
        w.write(f'{result.upper()} ')