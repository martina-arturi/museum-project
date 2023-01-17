import json

in_file = open("FINAL__event_stream.json", "r")
data = json.load(in_file)
in_file.close()


new_values = []
for v in data :
	
	new_v = {
	    "id": "action_" + str(v["id"]),
	    "user_id": "visitor_" + v["user_id"],
	    "language": v["language"],
	    "timestamp": v["timestamp"],
	    "x": v["x"],
	    "y": v["y"],
	    "floorId": "floor_" + str(v["floorId"]),
	    "exhibitId": "exhibit_" + str(v["exhibitId"])
    }

	new_values.append(new_v)


out_file = open("FINAL_2_event_stream.json", "w")
out_file.write(json.dumps(new_values, indent=2))
out_file.close()
			
