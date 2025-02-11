input = open("inputs/day6.txt", "r").read().split("\n\n")
data = [item.strip().split("\n") for item in input]
all_group_answers = [[len(item), ["".join(item)][0]] for item in data]
duplicate_strings = [
    "".join([c for c in group_answer[1] if group_answer[1].count(c) == group_answer[0]])
    for group_answer in all_group_answers
]
multiple = [len(set(item)) for item in duplicate_strings]
result = sum(multiple)
print(result)
