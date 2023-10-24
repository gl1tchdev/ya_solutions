class Event:
    def __init__(self, day, hour, minute, rocket_id, status):
        self.timestamp = 60 * (24 * int(day) + int(hour)) + int(minute)
        self.rocket_id = int(rocket_id)
        self.status = status

    def __lt__(self, other):
        return self.timestamp < other.timestamp


events = []
with open('../input.txt', 'r') as r, open('../output.txt', 'w') as w:
    count = int(r.readline())
    general_data = []
    for _ in range(count):
        input_data = r.readline()
        data: list = input_data.replace('\n', '').split(' ')
        if data[-1] == 'B':
            continue
        event = Event(*data)
        events.append(event)
    events.sort()
    rockets = {event.rocket_id: [[], 0] for event in events}
    for event in events:
        rockets[event.rocket_id][0].append(event.timestamp)
    result = []
    for rocket_id, data_list in rockets.items():
        total = 0
        for i in range(len(data_list[0]) - 1, -1, -2):
            total += data_list[0][i] - data_list[0][i - 1]
        rockets[rocket_id][1] = total
    sorted_rockets = sorted(rockets.items())
    for rocket in sorted_rockets:
        w.write(str(rocket[1][1]) + ' ')