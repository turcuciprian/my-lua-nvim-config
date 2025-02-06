input = open("./aoc-inputs/aoc-2020-day6-input.txt", "r").read().split("\n\n")
data = [item.split("\n") for item in input]
test = [len(set(["".join(item)][0])) for item in data]
print(sum(test))
