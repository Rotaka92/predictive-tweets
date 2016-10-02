import urllib
import itertools

output = []
name = []
weight = []
rows = 0

f = open('FLORIDA.csv', 'rU' ) #open the file in read universal mode
for line in f:
	if rows == 1000:
		break
	cells = line.split(",")
	output.append(cells[13].replace(' ', '')) #since we want only 14th column
	name.append(cells[0].replace(' ', ''))
	weight.append(cells[8].replace(' ', ''))
	print output[-1]
	rows = rows + 1
output.pop(0) #take out column title
name.pop(0) #take out column title
weight.pop(0)
f.close()


name = map(str.upper,name) #makes the names uppercase

print name
for x in range(rows-1):
	List = output[x]
	Names = name[x]
	Weight = weight[x]
	print x
	print "'" + List + "'"
	if List != "" and List != " ":
		urllib.urlretrieve(List, "pics/" + Names + "," + Weight + ".jpg")
