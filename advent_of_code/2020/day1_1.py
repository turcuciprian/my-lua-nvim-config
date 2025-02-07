input = open("./inputs/day1.txt", "r").read().split("\n")

for index in range(len(input)):
    current_number = int(input[index])
    for summed_nr in input[index:]:
        sum = int(summed_nr) + int(current_number)
        if sum == 2020:
            print(current_number, summed_nr)
            print(int(current_number) * int(summed_nr))
            break
print("done")
