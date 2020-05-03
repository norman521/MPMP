# (n(n-1))/2 + 1
from tile import Tile
import random


def nth_triangle_number(n):
    return int(n*(n+1)/2)


def first_number_on_nth_row(n):
    return int((n*(n-1))/2 + 1)


number_empty = 0

while number_empty != 1:
    tiles = []
    total_rows = 4

    def generate_row(row_number):
        first_number_on_row = first_number_on_nth_row(row_number)
        for value_index in range(row_number):
            tiles.append(
                Tile(row_number,
                     first_number_on_row + value_index,
                     value_index,
                     False))

    for n in range(1, total_rows + 1):
        generate_row(n)

    def get_empty_neighbours(tile):
        neighbours_values = tile.get_neighbours(total_rows)
        empty_neighbours = []
        for single_tile in tiles:
            if (single_tile.get_value() in neighbours_values
                    and single_tile.is_empty):
                empty_neighbours.append(single_tile)
        return empty_neighbours

    def get_non_empty_neighbours(tile):
        neighbours_values = tile.get_neighbours(total_rows)
        non_empty_neighbours = []
        for single_tile in tiles:
            if (single_tile.get_value() in neighbours_values
                    and not single_tile.is_empty):
                non_empty_neighbours.append(single_tile)
        return non_empty_neighbours

    def get_end_tile(start_tile):
        row_doubled = start_tile.row * 2
        non_empty_neighbours = get_non_empty_neighbours(start_tile)
        potential_end_tiles = []
        end_tiles = []
        for neighbour in non_empty_neighbours:
            # print("Non empty neighbours: " + str(neighbour.value))
            for potential_end_tile in get_empty_neighbours(neighbour):
                potential_end_tiles.append(potential_end_tile)
        for end_tile in potential_end_tiles:
            if((start_tile.row + 2 <= total_rows
                and end_tile.value == start_tile.value + row_doubled + 1)
               or (start_tile.row + 2 <= total_rows
                   and end_tile.value == start_tile.value + row_doubled + 3)
               or (start_tile.value_index + 2 < start_tile.row
                   and end_tile.value == start_tile.value + 2)
               or (start_tile.value_index - 2 >= 0
                   and end_tile.value == start_tile.value - 2)
               or (start_tile.row - 2 > 0
                   and end_tile.value == start_tile.value - row_doubled + 3
                   and start_tile.value_index < start_tile.row - 2)
               or (start_tile.row - 2 > 0
                   and end_tile.value == start_tile.value - row_doubled + 1)):
                end_tiles.append(end_tile)
        if end_tiles:
            end_tile = random.choice(end_tiles)
            return end_tile

    def find_jumped_tile(start_tile, end_tile):
        row_doubled = 2 * start_tile.row
        # print("start tile: " + str(start_tile.value))
        # print("end tile: " + str(end_tile.value))
        if(start_tile.row + 2 <= total_rows
                and end_tile.value == start_tile.value + row_doubled + 1):
            return_value = start_tile.value + start_tile.row
            # diagonal down left
        elif(start_tile.row + 2 <= total_rows
                and end_tile.value == start_tile.value + row_doubled + 3):
            return_value = start_tile.value + start_tile.row + 1
            # diagnonal down right
        elif(start_tile.value_index + 2 < start_tile.row
                and end_tile.value == start_tile.value + 2):
            return_value = start_tile.value + 1
            # straight right
        elif(start_tile.value_index - 2 >= 0
                and end_tile.value == start_tile.value - 2):
            return_value = start_tile.value - 1
            # straight left
        elif(start_tile.row - 2 > 0
                and end_tile.value == start_tile.value - row_doubled + 3):
            return_value = start_tile.value - start_tile.row + 1
            # diagonal up right
        elif(start_tile.row - 2 > 0
                and end_tile.value == start_tile.value - row_doubled + 1):
            return_value = start_tile.value - start_tile.row
            # diagnonal up left
        return return_value

    def get_tile_by_value(value):
        for tile in tiles:
            if tile.value == value:
                return tile

    non_empty_neighbours = get_non_empty_neighbours(tiles[0])
    # print(str(len(non_empty_neighbours)))

    for neighbour in non_empty_neighbours:
        empty_neighbours = get_empty_neighbours(neighbour)

    # print(str(len(empty_neighbours)))
    random_start_tile = random.choice(tiles)
    # random_start_tile = get_tile_by_value(4)
    random_start_tile.set_is_empty(True)
    # print("Empty tile: " + str(random_start_tile.value))
    number_empty = len(tiles) - 1
    solution = []
    solution_printed = False
    for x in range(100):

        potential_start_tiles = []
        for tile in tiles:
            if not tile.is_empty:
                potential_start_tiles.append(tile)
        start_tile = random.choice(potential_start_tiles)
        # start_tile = get_tile_by_value(9)
        # print("start tile: " + str(start_tile.value))
        end_tile = get_end_tile(start_tile)
        if end_tile is not None:
            jumped_tile_value = find_jumped_tile(start_tile, end_tile)
            get_tile_by_value(start_tile.value).set_is_empty(True)
            get_tile_by_value(jumped_tile_value).set_is_empty(True)
            get_tile_by_value(end_tile.value).set_is_empty(False)
            number_empty = number_empty - 1
            solution.append("empty: " + str(random_start_tile.value)
                            + " start: " + str(start_tile.value)
                            + " jumped tile: " + str(jumped_tile_value)
                            + " end: " + str(end_tile.value))
            # for tile in tiles:
            #     tile.print_tile()
        if number_empty == 1 and not solution_printed:
            for step in solution:
                print(step)
                solution_printed = True
        # random_start_tile.set_is_empty(False)
    # for tile in tiles:
    #     print(str(tile.get_row()) + ": "
    #           + str(tile.get_value()) + ": "
    #           + str(tile.get_neighbours(total_rows)))
