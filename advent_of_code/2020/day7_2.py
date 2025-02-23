import re
import time


# Read and parse input
with open("inputs/day7.txt", "r") as f:
    data = f.read().strip().split("\n")

# Precompile regex for bag cleaning
BAG_CLEANER = re.compile(r"\s*bags?\.?\s*")

# Parse the input into a dictionary for fast lookups
BAG_RULES = {}
for line in data:
    outer_bag, inner_bags = line.split(" bags contain ")
    if "no other bags" in inner_bags:
        BAG_RULES[outer_bag] = []
    else:
        BAG_RULES[outer_bag] = [
            BAG_CLEANER.sub("", bag.strip()).split(" ", 1)
            for bag in inner_bags.split(", ")
        ]

total_bags_count = 0


def recursive_contains(bag):
    parent_bag_count = int(bag[0])
    parent_bag_value = bag[1]
    if parent_bag_count > 0:
        result = 0

        result = sum(
            [
                int(child_bag[0]) + int(child_bag[0]) * recursive_contains(child_bag)
                for child_bag in BAG_RULES[parent_bag_value]
            ]
        )

        return result  # return total_bags_count
    else:
        return 1


# Timing the execution
print("Calculating...")
start_time = time.perf_counter()

# Count how many bags can contain "shiny gold"
result = recursive_contains(["1", "shiny gold"])

# Print results
end_time = time.perf_counter()
elapsed = end_time - start_time
print(f"\nResult: {result} \n")
print(f"Took: {elapsed:.9f} seconds")
