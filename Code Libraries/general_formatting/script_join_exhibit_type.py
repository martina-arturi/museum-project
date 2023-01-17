import json


in_file = open("wf__exhibit_formatted2.json", "r")
data_exhibit = json.load(in_file)
in_file.close()

in_file = open("wf__exhibit_type.json", "r")
data_type = json.load(in_file)
in_file.close()

# join the exhibit dataset and the exhibit type dataset


new_exhibit = []
for exhib in data_exhibit : 
	for t in data_type :
		if exhib["type"] == str(t["id"]) : 
			exhib["type"] = t["type"]
			
	new_exhibit.append(exhib)


out_file = open("wf__exhibit_with_also_type.json", "w")
out_file.write(json.dumps(new_exhibit, indent=2))
out_file.close()