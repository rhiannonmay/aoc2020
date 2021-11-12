import csv

#part 1

with open('Input 2.csv') as data:
    reader = csv.reader(data, delimiter=" ") #delimiter = what separates values

solutions= 0
for row in reader:
        quantity, letter, password = row[0], row[1][0], row[2]

        print(quantity, letter,password)


        i = quantity.index('-')
        lower = int(quantity[:i])
        upper = int(quantity[i+1:])

        count = 0 
        for character in password:
            if character == letter:
                count += 1

if count >= lower and count <= upper:
            solutions += 1

print(solutions)



#part 2

import csv

with open('Input 2.csv') as data:
    reader = csv.reader(data, delimiter=" ") 

    solutions= 0
    for row in reader:
        quantity, letter, password = row[0], row[1][0], row[2]

        print(quantity, letter,password)


        i = quantity.index('-')
        lower = int(quantity[:i])
        upper = int(quantity[i+1:])

        count = 0
        first = password[lower-1] == letter
        last = password[upper-1] == letter

        if (first and not last) or (last and not first):
            solutions += 1

print(solutions)


#git is stupid