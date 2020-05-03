# 1 = face up, 0 = face down
import random
import sys

min_counter = sys.maxsize
min_route = ""
min_routes = []
depth = 5
total_loops = 1000000000
all_down = ""
for x in range(depth):
    all_down += "0"


for loop_counter in range(total_loops):
    if loop_counter % (total_loops / 100000) == 0:
        print(loop_counter * 100 / total_loops)

    options = ["1", "0"]

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

    def add_options_layer(options_list):
        new_list = []
        for x in range(len(options_list)):
            new_list.append("1" + options_list[x])
            new_list.append("0" + options_list[x])
        return new_list

    def create_options_list(depth):
        for x in range(depth):
            global options
            options = add_options_layer(options)

    create_options_list(depth - 1)

    options.remove(all_down)
    options.sort()
    counter = 0
    route = ""

    while options and counter < pow(2, depth):
        card_index = random.randint(0, depth - 1)
        route += str(card_index)
        other_new_list = []
        for option in options:
            other_new_list.append(flip_card(option, card_index))
        if all_down in other_new_list:
            other_new_list.remove(all_down)
        options = other_new_list

        counter += 1

    if counter <= min_counter:
        min_counter = counter
        min_route = route
        min_routes.append(route)

print("Counter: " + str(min_counter))
print("Min route: " + min_route)
min_routes = list(dict.fromkeys(min_routes))
min_routes.sort()
print("START OF MIN ROUTES")
for route in min_routes:
    if pow(2, depth) - 1 == len(route):
        with open('MPMP/upsideDownCard/answersForFiveCards.txt', 'a') as f:
            f.write(route + "\n")
