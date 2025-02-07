def seat_id(boarding_pass):
    convert = (
        boarding_pass.replace("F", "0")
        .replace("B", "1")
        .replace("R", "1")
        .replace("L", "0")
    )
    row = int(
        convert[:-3], 2
    )  # extract the first 8 characters and convert them from binary to int  - 2 is for base 2
    col = int(
        convert[-3:], 2
    )  # extract the last 3 characters and convert them from binary to int

    return row * 8 + col


input = open("inputs/day5.txt", "r").read().split("\n")[:-1]
seats = [seat_id(bpass) for bpass in input]
print("hightest seat $ is:", max(seats))
