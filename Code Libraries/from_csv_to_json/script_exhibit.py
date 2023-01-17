import json

# script to convert exhibit data from csv to a json

in_file = open("exhibit.csv", "r")
data = in_file.read()
in_file.close()

# really badly read scan the csv
rows = data.split('\n')
splitted_rows = []
for row in rows: 
	splitted_rows.append(row.split(';'))


session_row = []
for r in splitted_rows :
	if len(r) > 1 :
		dictionary = {"id":				r[0], 
					  "name":			r[1], 
					  "floor_id": 		r[2], 
					  "type_id":		r[3], 
					  "polygon_str":	r[4], 
					  "icon_pos_str": 	r[5],
					  "parent_id": 		r[6]}
		session_row.append(dictionary)

out_file = open("wf__exhibit.json", "w")
out_file.write(json.dumps(session_row, indent=2))

out_file.close()
		