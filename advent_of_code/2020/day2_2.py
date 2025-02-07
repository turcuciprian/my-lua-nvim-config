def pharse_columns(keys_list):
    keys_list[0] = [int(item) for item in keys_list[0].split("-")]
    keys_list[1] = keys_list[1].replace(":", "")
    return keys_list


input = open("inputs/day2.txt", "r").read().split("\n")
input_arr = [pharse_columns(row.split(" ")) for row in input]

number_of_good_passwords = 0
for item in input_arr:
    A, B = item[0]
    char = item[1]
    all_chars = list(item[2])

    if (all_chars[A - 1] == char and all_chars[B - 1] != char) or (
        all_chars[A - 1] != char and all_chars[B - 1] == char
    ):
        number_of_good_passwords += 1

print(
    "day 2.1 problem returns a total number of valid passwords of:",
    number_of_good_passwords,
)
