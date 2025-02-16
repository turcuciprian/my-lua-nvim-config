import numpy as np
from typing import Any
from numpy.typing import NDArray
from typing import List

data = open("inputs/day7.txt", "r").read().split("\n")[:-1]
data_list = [item.split("bags contain") for item in data]
rows = [{item[0]: item[1].split(",")} for item in data_list]
ROWS_FORMATTED = np.array(
    [
        [
            {
                key.strip(): [
                    (
                        bag.replace("bags.", "")
                        .replace("bags", "")
                        .replace("bag.", "")
                        .replace("bag", "")
                        .strip()
                        .split(" ", 1)[1]
                    )
                    for bag in value
                ]
            }
            for key, value in row.items()
        ]
        for row in rows
    ],
    dtype=object,
)
ROWS_FORMATTED = np.array([item[0] for item in ROWS_FORMATTED])
ROWS_FORMATTED = np.array(
    [
        item
        for item in ROWS_FORMATTED
        if not (
            isinstance(item, dict)
            and len(item) == 1
            and list(item.values())[0] == ["other"]
        )
    ]
)


def get_values_by_key(all_rows: NDArray[Any], bag_name: str):
    for item in all_rows:
        row_key = list(item.keys())[0]

        if bag_name == row_key:
            print(bag_name)
            return item[row_key]
    return []


def check_children(all_rows: NDArray[Any], my_bag: str, current_bags: list[str]):
    results = []
    if my_bag in current_bags:
        return True
    else:
        if len(current_bags) == 0:
            return False
        else:
            for item in current_bags:
                current_bags = get_values_by_key(all_rows=all_rows, bag_name=item)
                result = check_children(
                    all_rows=all_rows,
                    my_bag=my_bag,
                    current_bags=current_bags,
                )
                results.append(result)
    return any(results)


result_list = []
for item in ROWS_FORMATTED:
    for _, values in item.items():
        result = check_children(
            all_rows=ROWS_FORMATTED, my_bag="shiny gold", current_bags=values
        )
        result_list.append(result)
# cycle trough all the rows of our list

print(sum(result_list))
