with open('input.txt', 'r') as r, open('output.txt', 'w') as w:
    start = r.readline().strip()
    start_input = [int(s) for s in start.split(' ')] # y m d h m s
    end = r.readline().strip()
    end_input = [int(s) for s in end.split(' ')]
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_seconds_start = (start_input[0] * 365 + sum(days_in_month[:start_input[1] - 1]) + start_input[2]) * 86400 + start_input[3] * 3600 + start_input[4] * 60 + start_input[5]
    total_seconds_end = (end_input[0] * 365 + sum(days_in_month[:end_input[1] - 1]) + end_input[2]) * 86400 + end_input[3] * 3600 + end_input[4] * 60 + end_input[5]
    delta = total_seconds_end - total_seconds_start
    num = delta / 86400
    days = round(num // 1)
    seconds = round((num % 1) * 86400)
    w.write(f'{days} {seconds}')