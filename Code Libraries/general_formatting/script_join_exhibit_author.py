import json


in_file = open("wf__exhibit_new.json", "r")
data_exhibit = json.load(in_file)
in_file.close()

in_file = open("authors.json", "r")
data_authors = json.load(in_file)
in_file.close()

# join the exhibit dataset and the author dataset

new_exhibit = []
for exhib in data_exhibit : 
	bol = False
	for auth in data_authors : 
		if exhib["id"] == str(auth["id"]) : 
			bol = True
			exhib["author"] = auth["Author"]

	if not bol :
		exhib["author"] = "Unkown"
	new_exhibit.append(exhib)


out_file = open("wf__exhibit_with_authors.json", "w")
out_file.write(json.dumps(new_exhibit, indent=2))
out_file.close()