import json

in_file = open("FINAL_2_event_stream.json", "r")
data_session = json.load(in_file)
in_file.close()

# convert the type of x and y inside event stream to float

new_stream = []
for event in data_session :

	new_event = {
		'id' 		: event["id"],
		'user_id' 	: event["user_id"],
		'language' 	: event["language"],
		'timestamp' : event["timestamp"],
		'x' 		: float(event["x"]) if event["x"] != "" else -1,
		'y' 		: float(event["y"]) if event["y"] != "" else -1,
		'floorId' 	: event["floorId"],
		'exhibitId' : event["exhibitId"]
	}
		
	
	new_stream.append(new_event)

out_file = open("FINAL_3_event_stream.json", "w")
out_file.write(json.dumps(new_stream, indent=2))
out_file.close()
			
