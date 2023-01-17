import json

in_file = open("FINAL__users_info.json", "r")
data = json.load(in_file)
in_file.close()


new_values = []
for v in data :
	
	new_v = {
	    "id": "visitor_" + v["id"],
	    "gender": v["gender"],
	    "eta": v["eta"],
	    "provenience": v["provenience"],
	    "hobbies": v["hobbies"],
	    "name": v["name"],
	    "surname": v["surname"],
	    "occupation": v["occupation"]
  	}

	new_values.append(new_v)


out_file = open("FINAL_2_visitors.json", "w")
out_file.write(json.dumps(new_values, indent=2))
out_file.close()
			
