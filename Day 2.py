import csv

# part 1
with open('Input 2.csv') as data:
    reader = csv.reader(data, delimiter=" ") #delimiter = what separates values

    solutions= 0
    for row in reader:
        quantity, letter, pw = row[0], row[1][0], row[2]

        print(quantity, letter,pw)


        i = quantity.index('-')
        lower = quantity[:i]
        upper = quantity[i+1:]

        count = 0 
        for character in pw:
            if character == letter:
                count += 1

        if count >= lower or count <= upper:
            solutions += 1

print(solutions)

