input = open("./aoc-inputs/aoc-2020-day4-input.txt", "r").read()
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
    passwords_info = [pass_info.split(":") for pass_info in passport]
    passports.append(passwords_info)

# Step 5: create a list with all the keys
all_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
valid_passports = 0
# Step 6: check if there are 8 keys present (all the 8 keys)
for passport in passports:
    all_keys_present_list = [pass_info[0] in all_keys for pass_info in passport]

    # 8 keys are present
    cond1 = sum(1 for key_exists in all_keys_present_list if key_exists) > 7

    if cond1:
        valid_passports += 1
    else:
        # less than 8 keys are present
        # Step 7: if Step 6 is not true, check if there are 7 keys present and if cid is present - passport invalid if not and valid if yes
        cond2 = sum(1 for key_exists in all_keys_present_list if key_exists) == 7
        # if cid is in present the keys
        cond3 = "cid" in [key_value[0] for key_value in passport]
        if cond2 and not cond3:
            valid_passports += 1
# Step 8: count valid passports and return the result
print("total valid passports:", valid_passports)
