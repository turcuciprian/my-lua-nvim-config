import re
import time


# Read and parse input
with open("inputs/day8.txt", "r") as f:
    data = f.read().strip().split("\n")

data = [item.split(" ") for item in data]
data = [[item[0], [item[1][:1], int(item[1][1:])]] for item in data]

indexes_visited = [0]
acc_final_value = 0


def follow_the_rule(index):
    global acc_final_value

    row = data[index]
    increment_value: str = row[1][0]
    rule = row[0]
    increment = True if increment_value == "+" else False

    ammount = int(row[1][1])
    # ACC
    if rule.lower() == "acc":
        acc_final_value = (
            acc_final_value + ammount if increment else acc_final_value - ammount
        )
        index += 1
    # JMP
    if rule.lower() == "jmp":
        index = index + ammount if increment else index - ammount
        if index > len(data):
            index = index - len(data)
        if index < 0:
            index = len(data) + index
        # index += ammount
    # NOP
    if rule.lower() == "nop":
        index += 1
        if index > len(data):
            index = 0

    if index in indexes_visited:
        return acc_final_value

    print(acc_final_value)

    indexes_visited.append(index)

    return follow_the_rule(index)


try:
    print(follow_the_rule(0))
except:
    print("error")
