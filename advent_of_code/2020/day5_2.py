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
    return int(row * 8 + col)


input = open("inputs/day5.txt", "r").read().split("\n")[:-1]
seats = [seat_id(bpass) for bpass in input]
part2_seats = [seat - 1 for seat in sorted(seats)[1:-1] if seat - 1 not in seats]
# although part2_seats returns correctly, the answer placed in the response was the second index
print("Your seat ID", part2_seats[0])
