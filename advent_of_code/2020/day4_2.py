def validate_key(keyValue):
    if len(keyValue) != 2:
        return False

    key = keyValue[0]
    value = keyValue[1]

    if key == "byr":
        return len(value) == 4 and value.isdigit() and 1920 <= int(value) and int(value) <= 2002

    if key == "iyr":
        return len(value) == 4 and value.isdigit() and 2010 <= int(value) and int(value) <= 2020

    if key == "eyr":
        return len(value) == 4 and value.isdigit() and 2020 <= int(value) and int(value) <= 2030

    if key == "hgt":
        hgt_cond = False
        if "cm" in value:
            height = value.split("cm")[0]
            hgt_cond = height.isdigit() and 150 <= int(height) and int(height) <= 193
        if "in" in value:
            height = value.split("in")[0]
            hgt_cond = height.isdigit() and 59 <= int(height) and int(height) <= 76

        # len and sum comparison

        has_match = [True for flag in ["cm", "in"] if flag in value]
        return (all(has_match)) and hgt_cond

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



input = open("inputs/day4.txt", "r").read()
# Step 1: split text into array of passports
passports_raw = input.split("\n\n")

# Step 2: remove new lines from pasport data
passports_raw = [passport.replace("\n", " ") for passport in passports_raw]

# Step 3: split each key-value from passport data separated by space
passports_list = [passport.strip().split(" ") for passport in passports_raw]

# Step 4: split key/value passport information into sub list
# passports = [pass_info for pass_info in passport for passport in passports_list]
passports = [[kvp.split(":") for kvp in passport] for passport in passports_list]

# Step 5: create a list with all the keys
all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
valid_passports = 0
for passport in passports:
    all_keys_present_list = [True for pass_info in passport if pass_info[0] in all_keys]

    # 8 keys are present
    cond1 = len(all_keys_present_list)==8

    sum_validated_passports = sum(
        [1 for key_value in passport if validate_key(key_value)]
    )

    validated_passports_match_length = sum_validated_passports == len(passport)
    all_keys_are_valid = validated_passports_match_length

    #
    # COND1 - 8 keys are present
    #

    if cond1:
        if all_keys_are_valid:
            valid_passports += 1
    else:
        # Step 7: check length of passport information items
        cond2 = sum(1 for key_exists in all_keys_present_list if key_exists) == 7

        key_items = list(set([key_value[0] for key_value in passport]))

        # if cid is in present the keys
        cond3 = (key_items.count("cid")) == 1


        #
        # COND2 - 7 keys & COND3 cid is present
        #
        if cond2 and not cond3 :
            if validated_passports_match_length:
                valid_passports += 1
print("valid passports:", valid_passports)
