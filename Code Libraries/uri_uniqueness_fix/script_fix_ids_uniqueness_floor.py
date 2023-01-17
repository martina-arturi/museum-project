import json

in_file = open("FINAL__floors.json", "r")
data = json.load(in_file)
in_file.close()


new_values = []
for v in data :
	
	new_v = {
	    "id": "floor_" + str(v["id"]),
	    "name": v["name"],
	    "museum" : "museum_" + str(v["museum"])
	}

	new_values.append(new_v)


out_file = open("FINAL_2_floors.json", "w")
out_file.write(json.dumps(new_values, indent=2))
out_file.close()
			
