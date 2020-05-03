options = []
new_options = ["1", "0"]

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                options.append(str(w) + str(x) + str(y) + str(z))


def add_options_layer(options_list):
    new_list = []
    for x in range(len(options_list)):
        new_list.append("1" + options_list[x])
        new_list.append("0" + options_list[x])
    return new_list


def create_options_list(depth):
    for x in range(depth):
        global new_options
        new_options = add_options_layer(new_options)


create_options_list(3)
options.sort()
print(options)
new_options.sort()
print(new_options)
