import json

# script to convert exhibit_type data from csv to a json

in_file = open("exhibit_type.csv", "r")
data = in_file.read()
in_file.close()

# really badly read scan the csv
rows = data.split('\n')
splitted_rows = []
for row in rows: 
	splitted_rows.append(row.split(';'))

well_formatted_list = []
for r in splitted_rows :
	if len(r) > 1 :

		dictionary = {  "id":r[0], 
					    "type":r[1]}

		well_formatted_list.append(dictionary)


dumped = json.dumps(well_formatted_list, indent=2)

out_file = open("wf__exhibit_type.json", "w")
out_file.write(dumped)
out_file.close()