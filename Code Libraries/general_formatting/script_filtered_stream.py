import json

in_file = open("FINAL__event_stream.json", "r")
data_session = json.load(in_file)
in_file.close()

# filter the stream of actions removing the ones in which the user didn't move or take any other action


event_id = 1
old_user_id = "-1"
old_x = "-1"
old_y = "-1"
old_exhibit = -2
old_floor = -1

new_stream = []
for event in data_session :

	# if we change user we add the event
	if old_user_id != event["user_id"] :

		old_user_id = event["user_id"]
		old_x 		= event["x"]
		old_y 		= event["y"]
		old_exhibit = event["exhibitId"]
		old_floor 	= event["floorId"]

		new_event = {
			'id' 		: event_id,
			'user_id' 	: event["user_id"],
			'language' 	: event["language"],
			'timestamp' : event["timestamp"],
			'x' 		: event["x"],
			'y' 		: event["y"],
			'floorId' 	: event["floorId"],
			'exhibitId' : event["exhibitId"]
		}
		
		event_id += 1
		new_stream.append(new_event)

	else : 

		# we add the event only if there is a change in location, exhibit or floor
		if old_x != event["x"] or old_y != event["y"] or old_exhibit != event["exhibitId"] or old_floor != event["floorId"] :
			old_user_id = event["user_id"]
			old_x 		= event["x"]
			old_y 		= event["y"]
			old_exhibit = event["exhibitId"]
			old_floor 	= event["floorId"]

			new_event = {
				'id' 		: event_id,
				'user_id' 	: event["user_id"],
				'language' 	: event["language"],
				'timestamp' : event["timestamp"],
				'x' 		: event["x"],
				'y' 		: event["y"],
				'floorId' 	: event["floorId"],
				'exhibitId' : event["exhibitId"]
			}
			
			event_id += 1
			new_stream.append(new_event)

print(event_id)
out_file = open("FINAL_2_event_stream.json", "w")
out_file.write(json.dumps(new_stream, indent=2))
out_file.close()
			
