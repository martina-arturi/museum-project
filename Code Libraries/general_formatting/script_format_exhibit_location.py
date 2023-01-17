import json

in_file = open("FINAL__exhibit.json", "r")
data_exhib = json.load(in_file)
in_file.close()

# extract the location values from location to location_x and location_y

new_exhib = []
for ex in data_exhib :
	
	new_ex = {
		"id" : ex["id"],
		"name" : ex["name"],
		"floor" : ex["floor"],
		"location_x" : ex["location"]["x"],
		"location_y" : ex["location"]["y"],
		"type" : ex["type"],
		"room" : ex["room"],
		"authors" : ex["authors"]
	}

	new_exhib.append(new_ex)


out_file = open("FINAL_2_exhibit.json", "w")
out_file.write(json.dumps(new_exhib, indent=2))
out_file.close()
			
