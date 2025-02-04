input = open("part1_input.txt", "r").read()


def generate_splits(boarding_pass: str):
    return [list(boarding_pass)[:-3], list(boarding_pass)[-3:]]


def process_row_character(character, x=0, y=127):
    new_value = y - ((y - x) // 2)

    if character == "F":
        return (x, new_value)

    if character == "B":
        return (new_value, y)
    return (0, 0)


def process_col_character(character, x=0, y=7):
    new_value = y - ((y - x) // 2)

    if character == "L":
        return (x, new_value)

    if character == "R":
        return (new_value, y)
    return (0, 0)


input_arr = input.split("\n")[:-1]
boarding_passes = [generate_splits(bpass) for bpass in input_arr]

all_seats = []
for bpass in boarding_passes:
    seat_id=0
    # Row
    row = 0
    col = 0
    x = 0
    y = 127
    for fb in bpass[0]:
        x, y = process_row_character(fb, x, y)
        if y == x + 1:
            if fb == "F":
                row = x
            else:
                row = y
    # Column
    x = 0
    y = 7
    for fb in bpass[1]:
        x, y = process_col_character(fb, x, y)
        if y == x + 1:
            if fb == "L":
                col = x
            else:
                col = y
    # Column
    seat_id = (row * 8) + col
    all_seats.append(seat_id)

print("hightest seat ID:", max(all_seats))

# x=0 - y=127
# F - 0:127-(127-0)/2
# F - x:y-(y-x)/2
# x = x | y= y-(y-x)/2

# B - 127-(127-0)/2: 127
# B - y-(y-x)/2: y
# x=y-(y-x)/2 | y=y

# x = 0 | y=7
# R - ceil((7-0)/2):7
# R - ceil((y-x)/2):y
# R - x=ceil((y-x)/2) | y = y

# L- 0:ceil((7-0)/2)
# L - x:ceil((y-x)/2)
# L - x=x | y = ceil((y-x)/2)
