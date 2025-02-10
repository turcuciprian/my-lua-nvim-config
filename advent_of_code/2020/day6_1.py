input = open("inputs/day6.txt", "r").read().split("\n\n")
data = [item.split("\n") for item in input]
result = [len(set(["".join(item)][0])) for item in data]
print(sum(result))
