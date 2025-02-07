input = open("inputs/day6.txt", "r").read().split("\n\n")
data = [item.split("\n") for item in input]
all_group_answers = [["".join(item)][0] for item in data]
duplicate_strings = [
    "".join([c for c in group_answer if group_answer.count(c) > 1])
    for group_answer in all_group_answers
]
yes_answers = [len(set(list(item))) for item in duplicate_strings]
result = sum(yes_answers)
print(result)
breakpoint()
