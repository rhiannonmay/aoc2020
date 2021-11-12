#part 1

with open('Input 4.txt') as fp:
    data = [f.strip() for f in fp]

def part1 (data):
    curr_passport = {}
    all_passports = []
    valid_passport_count = 0
    req_fields =[
        "byr", # (Birth Year)
        "iry", # (Issue Year)
        "eyr", # (Expiration Year)
        "hgt", # (Height)
        "hcl", # (Hair Color)
        "ecl", # (Eye Color)
        "pid", # (Passport ID)
    ]
    key_count = 0
    current = 0 

    for line in data:
        if line == " ":
            if current == len(req_fields):
                valid_passport_count += 1

    for field in line.split():
            key, value = field.split(":")
            if key in req_fields:
                current += 1
    return valid_passport_count
    
print("Solution:  ", part1(data))


#        if line == " ":
#            valid_passport_count.append(curr_passport)
#        curr_passport = {}
#        all_passports.append(curr_passport)
#all_passports.append(curr_passport)
