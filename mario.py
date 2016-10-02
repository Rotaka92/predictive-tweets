import urllib
import itertools

img = []
firstName = []
lastName = []
weight = []
rows = 0

f = open('FLORIDA.csv', 'rU' ) # open the file in read universal mode
for line in f:
	if rows == 10:
		break
	cells = line.split(",")
	img.append(cells[13].replace(' ', '')) # since we want only 14th column
	firstName.append(cells[0].replace(' ', ''))
	lastName.append(cells[2].replace(' ', ''))
	weight.append(cells[8].replace(' ', ''))
	rows = rows + 1

img.pop(0) # take out column title
firstName.pop(0) # take out column title
lastName.pop(0)
weight.pop(0)
f.close()


firstName = map(str.lower, firstName) # makes the names uppercase
lastName = map(str.lower, lastName) # makes the names uppercase

for x in range(rows-1):
        print firstName[x] + " " + lastName[x]
