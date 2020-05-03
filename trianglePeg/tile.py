class Tile:
    def __init__(self, row, value, value_index, is_empty):
        self.row = row
        self.value = value
        self.value_index = value_index
        self.is_empty = is_empty

    def get_value(self):
        return self.value

    def set_is_empty(self, is_empty):
        self.is_empty = is_empty

    def get_row(self):
        return self.row

    def print_tile(self):
        print("Row: "
              + str(self.row)
              + " Value: "
              + str(self.value)
              + " Empty: "
              + str(self.is_empty))

    def get_neighbours(self, total_rows):
        neighbours = []
        row_above_first_value = int(((self.row - 1)*((self.row - 1)-1))/2 + 1)
        row_below_first_value = int(((self.row + 1)*((self.row + 1)-1))/2 + 1)
        if(self.value_index - 1 >= 0):
            neighbours.append(self.value - 1)
        if(self.value_index + 1 < self.row):
            neighbours.append(self.value + 1)
        if(self.row - 1 > 0 and self.value_index - 1 >= 0):
            neighbours.append(row_above_first_value + self.value_index - 1)
        if(self.row - 1 > 0 and self.value_index < self.row - 1):
            neighbours.append(row_above_first_value + self.value_index)
        if(self.row + 1 <= total_rows and self.value_index >= 0):
            neighbours.append(row_below_first_value + self.value_index)
        if(self.row + 1 <= total_rows and self.value_index + 1 <= self.row):
            neighbours.append(row_below_first_value + self.value_index + 1)
        neighbours.sort()
        return neighbours
