# 1 = face up, 0 = face down
import random
import sys

min_counter = sys.maxsize
min_route = ""
all_down = "0000"
number_of_cards = 4

for loop_counter in range(100000):

    def flip_card(cards, n):
        new_card = ""
        for letter_index in range(len(cards)):
            if letter_index != n:
                new_card += cards[letter_index]
            else:
                if cards[letter_index] == "0":
                    new_card += "1"
                else:
                    new_card += "0"
        return new_card

    options = []

    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    options.append(str(w) + str(x) + str(y) + str(z))

    options.remove(all_down)
    counter = 0
    route = ""

    while len(options) > 0:
        for x in range(len(options)):
            card = options.pop(0)
            card_index = random.randint(0, number_of_cards - 1)
            route += str(card_index)
            options.append(flip_card(card, card_index))
            options = list(dict.fromkeys(options))
            if all_down in options:
                options.remove(all_down)
            counter += 1

    if counter < min_counter:
        min_counter = counter
        min_route = route

print(min_counter)
print(min_route)
