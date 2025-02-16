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
            BAG_CLEANER.sub("", bag.strip()).split(" ", 1)[1]
            for bag in inner_bags.split(", ")
        ]


# Recursive function to check if a bag contains "shiny gold"
def contains_shiny_gold(bag):
    return "shiny gold" in BAG_RULES[bag] or any(
        contains_shiny_gold(inner) for inner in BAG_RULES[bag]
    )


# Timing the execution
print("Calculating...")
start_time = time.perf_counter()

# Count how many bags can contain "shiny gold"
result = sum(contains_shiny_gold(bag) for bag in BAG_RULES)

# Print results
end_time = time.perf_counter()
elapsed = end_time - start_time
print(f"Result: {result}")
print(f"Took: {elapsed:.4f} seconds")
