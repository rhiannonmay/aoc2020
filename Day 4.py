#part 1

with open('Input 4.txt') as fp:
    lines = [f.strip() for f in fp]

curr_passport = {}
all_passports = []
valid_passports = []
req_keys =[
    "byr", # (Birth Year)
    "iry", # (Issue Year)
    "eyr", # (Expiration Year)
    "hgt", # (Height)
    "hcl", # (Hair Color)
    "ecl", # (Eye Color)
    "pid", # (Passport ID)
]

key_count = 0

for line in lines:
    if line != "":
        temp_line = line.split(" ")
        temp_dict = {item.split(":")[0]:item.split(":")[1] for item in temp_line}
        for key, value in temp_dict.items():
            curr_passport[key] = value
    else:
        if all(field in curr_passport for field in req_keys):
            valid_passports.append(curr_passport)
        curr_passport = {}
        all_passports.append(curr_passport)
all_passports.append(curr_passport)

len(all_passports), len(valid_passports)

