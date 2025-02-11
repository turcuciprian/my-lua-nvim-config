data = open("inputs/day7.txt", "r").read().split("\n")[:-1]
data_list = [item.split("bags contain") for item in data]
rows = [{item[0]: item[1].split(",")} for item in data_list]
rows_formatted = [
    [
        {
            key.strip(): [
                (
                    bag.replace("bags.", "")
                    .replace("bags.", "")
                    .replace("bags", "")
                    .replace("bag.", "")
                    .replace("bag.", "")
                    .strip()
                    .split(" ", 1)[1]
                )
                for bag in value
            ]
        }
        for key, value in row.items()
    ]
    for row in rows
]
my_bag = "shiny gold"
# return all the first level parent bags that can contain my_bag + all False list items that do not
bags_containing_my_bag = [
    [key if my_bag in value else False for key, value in item[0].items()][0]
    for item in rows_formatted
]
# filter the Falses out and just remain with the first level parents
result = ([ item for item in bags_containing_my_bag if item is not False])
breakpoint()
