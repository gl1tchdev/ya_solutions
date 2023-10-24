from collections import Counter

with open('input.txt', 'r') as r, open('output.txt', 'w') as w:
    game_data = r.readline().split()
    count_first_player = int(game_data[0])
    count_second_player = int(game_data[1])
    changes = int(game_data[2])

    first_player = [int(s) for s in r.readline().split()]
    second_player = [int(s) for s in r.readline().split()]

    for i in range(changes):
        change_data = r.readline().split()
        deck = first_player if change_data[1] == 'A' else second_player
        if int(change_data[0]) == 1:
            deck.append(int(change_data[2]))
        else:
            deck.remove(int(change_data[2]))
        other_deck = second_player if change_data[1] == 'A' else first_player
        c_deck = Counter(deck)
        c_oth_deck = Counter(other_deck)
        diff_one = (c_deck - c_oth_deck)
        diff_two = (c_oth_deck - c_deck)
        diff = list(diff_one.elements()) + list(diff_two.elements())
        w.write(f'{len(diff)} ')