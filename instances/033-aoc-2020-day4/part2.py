def validate_key(keyValue):
    if len(keyValue) != 2:
        return False

    key = keyValue[0]
    value = keyValue[1]
    if key == "byr":
        return len(value) == 4 and 1920 <= int(value) <= 2002

    if key == "iyr":
        return len(value) == 4 and 2010 <= int(value) <= 2020

    if key == "eyr":
        return len(value) == 4 and 2020 <= int(value) <= 2030

    if key == "hgt":
        hgt_cond = False
        if "cm" in value:
            height = value.split("cm")[0]
            hgt_cond = height.isdigit() and 150 <= int(height) <= 193
        if "in" in value:
            height = value.split("in")[0]
            hgt_cond = height.isdigit() and 59 <= int(height) <= 76

        # len and sum comparison

        has_match = [True for flag in ["cm", "in"] if flag in value]
        return (sum(has_match) == 1) and hgt_cond

    if key == "hcl":
        hcl_cond = (
            sum([1 for char in value[1:] if char in list("abcdef0123456789")]) == 6
        )
        return value[0] == "#" and hcl_cond

    if key == "ecl":
        return (
            sum(
                [
                    1
                    for flag in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    if flag in value
                ]
            )
            == 1
        )

    if key == "pid":
        return len(value) == 9 and value.isdigit()

    if key == "cid":
        return True
    
    return False


input = open("input.txt", "r").read()
# Step 1: split text into array of passports
passports_raw = input.split("\n\n")

# Step 2: remove new lines from pasport data
passports_raw = [passport.replace("\n", " ") for passport in passports_raw]

# Step 3: split each key-value from passport data separated by space
passports_list = [passport.split(" ") for passport in passports_raw]

# Step 4: split key/value passport information into sub list
# passports = [pass_info for pass_info in passport for passport in passports_list]
passports = []

for passport in passports_list:
    passport_info = [pass_info.split(":") for pass_info in passport]
    passports.append(passport_info)

# Step 5: create a list with all the keys
all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
valid_passports = 0
# Step 6: check if there are 8 keys present (all the 8 keys)
for passport in passports:
    breakpoint()
    all_keys_present_list = [True for pass_info in passport if pass_info[0] in all_keys]

    # 8 keys are present
    cond1 = sum(1 for key_exists in all_keys_present_list if key_exists) >= 7

    sum_validated_passports = sum(
        [1 for key_value in passport if validate_key(key_value)]
    )
    all_keys_are_valid = sum_validated_passports == len(passport)
    if cond1:
        if all_keys_are_valid:
            valid_passports += 1
    else:
        # less than 8 keys are present
        # Step 7: if Step 6 is not true, check if there are 7 keys present and if cid is present - passport invalid if not and valid if yes
        cond2 = sum(1 for key_exists in all_keys_present_list if key_exists) == 7
        # if cid is in present the keys
        cond3 = "cid" in [key_value[0] for key_value in passport]

        if cond2 and not cond3:
            if all_keys_are_valid:
                valid_passports += 1
print("valid passports:",valid_passports)
