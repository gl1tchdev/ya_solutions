import heapq

with open('input.txt', 'r') as r:
    cities_count = int(r.readline().replace('\n', ' '))
    cities = []
    for _ in range(cities_count):
        data = [int(s) for s in r.readline().split()]
        cities.append(tuple(data))
    max_route = int(r.readline().replace('\n', ' '))
    FROM, TO = [int(s) - 1 for s in r.readline().split()]


def distance(city1: tuple, city2: tuple) -> int:
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])


def find_neighbours(current: tuple, cities: list[tuple], max_distance: int = max_route) -> iter:
    return (city for city in cities if city != current and distance(current, city) <= max_distance)


start_point = cities[FROM]
end_point = cities[TO]
infinity = float('inf')


def dijkstra(start: tuple, end: tuple, cities: list[tuple]) -> int:
    distances = {city: infinity for city in cities}
    distances[start] = 0

    pq = [(0, start)]
    visited = set()

    while pq:
        cur_dist, cur_city = heapq.heappop(pq)
        if cur_city == end:
            return cur_dist
        if cur_city in visited:
            continue
        for neighbour in find_neighbours(cur_city, cities):
            if neighbour in visited:
                continue
            n_d = cur_dist + 1
            if n_d < distances[neighbour]:
                heapq.heappush(pq, (cur_dist + 1, neighbour))
                visited.add(cur_city)
                distances[cur_city] = n_d
    return -1


with open('output.txt', 'w') as w:
    result = dijkstra(start_point, end_point, cities)
    w.write(f'{result}')
