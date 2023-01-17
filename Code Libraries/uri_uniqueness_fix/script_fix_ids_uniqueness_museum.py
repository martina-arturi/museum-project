import json

in_file = open("FINAL__museum.json", "r")
data = json.load(in_file)
in_file.close()


new_values = []
for v in data :
	
	new_v = {
	    "name" : v["name"],
		"latitude" : v["latitude"],
		"longitude" : v["longitude"],
		"theme" : v["theme"],
		"id" : "museum_" + str(v["id"])
  	}

	new_values.append(new_v)


out_file = open("FINAL_2_museum.json", "w")
out_file.write(json.dumps(new_values, indent=2))
out_file.close()
			
