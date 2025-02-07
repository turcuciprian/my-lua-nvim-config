def pharse_columns(keys_list):
    keys_list[0] = [int(item) for item in keys_list[0].split("-")]
    keys_list[1] = keys_list[1].replace(":", "")
    return keys_list


input = open("inputs/day2.txt", "r").read().split("\n")
input_arr = [pharse_columns(row.split(" ")) for row in input]
# 9-10 x: pxcbpxxwkqjttx
# task 1
number_of_good_passwords = 0
for item in input_arr:
    min, max = item[0]
    char = item[1]
    all_chars = list(item[2])
    number_of_chars = all_chars.count(char)
    is_password_good = min <= number_of_chars & number_of_chars <= max
    if is_password_good:
        number_of_good_passwords += 1
print(
    "day 2.0 problem returns a total number of valid passwords of:",
    number_of_good_passwords,
)
