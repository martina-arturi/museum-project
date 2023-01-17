import json

# script to convert device_session data from csv to a json

in_file = open("device_session.csv", "r")
data = in_file.read()
in_file.close()

rows = data.split('\n')
splitted_rows = []
for row in rows: 
	splitted_rows.append(row.split(';'))


session_row = []
for r in splitted_rows :
	if len(r) == 9 :
		dictionary = {"id":				r[0], 
					  "device_id":		r[1], 
					  "creation_date": 	r[2], 
					  "date_start":		r[3], 
					  "date_end":		r[4], 
					  "position_count": r[5],
					  "exhibit_count":  r[6],
					  "quiz_count":  	r[7],
					  "locale":  		r[8]}
		session_row.append(dictionary)

out_file = open("wf__device_session.json", "w")
out_file.write(json.dumps(session_row, indent=2))

out_file.close()
		