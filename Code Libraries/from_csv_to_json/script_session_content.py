
import csv
import json

# script to convert session_content data from csv to a json, unwrapping the inner jsons

in_file = open("session_content_formatted.csv", "r")
data = in_file.read()
in_file.close()

# really badly read scan the csv
rows = data.split('\n')
splitted_rows = []
for row in rows: 
  splitted_rows.append(row.split(';'))

splitted_rows.pop(0)

well_formatted_list = []
for r in splitted_rows :
	if len(r) > 1 :
		beacons_json = json.loads(r[2].replace("None", "null").replace("\'", "\""))

		events_json = json.loads(r[4].replace("'","\""))

		dictionary = {"id":r[0], 
									"build_version":r[1], 
									"content_id": r[3], 
									"language" : r[5], 
									"iosVersion" : r[6],
									"beacons" : beacons_json, 
									"events": events_json}

		well_formatted_list.append(dictionary)


dumped = json.dumps(well_formatted_list, indent=2)

out_file = open("wf__session_content.json", "w")
out_file.write(dumped)
out_file.close()

	 