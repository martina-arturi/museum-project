import json

in_file = open("FINAL__rooms.json", "r")
data = json.load(in_file)
in_file.close()


new_values = []
for v in data :
	
	new_v = {
	    "id": "room_" + v["id"],
	    "name": v["name"],
	    "floor_id": "floor_" + v["floor_id"],
	    "theme": v["theme"],
	    "x1": v["x1"],
	    "y1": v["y1"],
	    "x2": v["x2"],
	    "y2": v["y2"],
	    "x3": v["x3"],
	    "y3": v["y3"],
	    "x4": v["x4"],
	    "y4": v["y4"],
	    "museum": "museum_" + str(v["museum"])
  	}

	new_values.append(new_v)


out_file = open("FINAL_2_room.json", "w")
out_file.write(json.dumps(new_values, indent=2))
out_file.close()
			
