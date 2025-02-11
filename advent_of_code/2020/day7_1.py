data = open("inputs/day7.txt", "r").read().split("\n")[:-1]
data_list = [item.split("bags contain") for item in data]
rows = [{item[0]: item[1].split(",")} for item in data_list]
rows_formatted = [
    [
        {
            key: [
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
