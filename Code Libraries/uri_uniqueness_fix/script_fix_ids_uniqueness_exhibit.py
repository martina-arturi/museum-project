import json

in_file = open("FINAL__exhibit.json", "r")
data = json.load(in_file)
in_file.close()


new_values = []
for v in data :
	
	new_v = {
		"id" : "exhibit_" + v["id"],
		"name" : v["name"],
		"floor" : "floor_"+v["floor"],
		"location_x" : v["location_x"],
		"location_y" : v["location_y"],
		"room" : "room_"+v["room"],
		"authors" : v["authors"]
	}

	new_values.append(new_v)


out_file = open("FINAL_2_exhibit.json", "w")
out_file.write(json.dumps(new_values, indent=2))
out_file.close()
			
