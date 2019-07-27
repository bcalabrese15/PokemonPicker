import json

input = input("Please input file location: ")
with open(input) as f:
	data = json.load(f)
for item in data["pokemon"]:
	if input in item["type"]:
		print(item["name"])