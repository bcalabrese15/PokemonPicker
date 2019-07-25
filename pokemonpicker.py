input = input("Please input file location: ")
file = open(input, "r")
for line in file:
	print(line)