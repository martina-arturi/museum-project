import json

in_file = open("FINAL__rooms.json", "r")
data_rooms = json.load(in_file)
in_file.close()

# map the dimension object inside the room entity to sinlge properties that correspond to a coordinate of a point.

new_rooms = []
for room in data_rooms :
	if room["dimension"] != None :
		new_r = {
			"id" : room["id"],
			"name" : room["name"],
			"floor_id" : room["floor_id"],
			"theme" : room["theme"],
			"x1" : room["dimension"][0]["x"],
			"y1" : room["dimension"][0]["y"],
			"x2" : room["dimension"][1]["x"],
			"y2" : room["dimension"][1]["y"],
			"x3" : room["dimension"][2]["x"],
			"y3" : room["dimension"][2]["y"],
			"x4" : room["dimension"][3]["x"],
			"y4" : room["dimension"][3]["y"],
			"museum" : room["museum"]
		}
		new_rooms.append(new_r)

	else : 
		new_r = {
			"id" : room["id"],
			"name" : room["name"],
			"floor_id" : room["floor_id"],
			"theme" : room["theme"],
			"x1" : -1,
			"y1" : -1,
			"x2" : -1,
			"y2" : -1,
			"x3" : -1,
			"y3" : -1,
			"x4" : -1,
			"y4" : -1,
			"museum" : room["museum"]
		}
		new_rooms.append(new_r)


out_file = open("FINAL_2_rooms.json", "w")
out_file.write(json.dumps(new_rooms, indent=2))
out_file.close()
			
