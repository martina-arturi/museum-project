import json

# script to convert floor data from csv to a json

in_file = open("floor.csv", "r")
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
					    "name":r[1], 
	    			    "scale": r[2]}

		well_formatted_list.append(dictionary)


dumped = json.dumps(well_formatted_list, indent=2)

out_file = open("wf__floors.json", "w")
out_file.write(dumped)
out_file.close()