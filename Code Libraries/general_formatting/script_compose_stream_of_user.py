import json

in_file = open("wf__session_content.json", "r")
data_session = json.load(in_file)
in_file.close()

def sort_by_timestamp(list):
    return list['timestamp']

new_stream = []
for session in data_session :

	timestamps=[]

	user_id = session["id"];
	langauge = session["language"];

	if (session["events"] != []):

		action_event=[] 	# store all the actions with a timestamps
		question_event=[] 	# store all the other actions, i.e. the questions

		# divide the events in the two types above
		for event in session["events"] :
			if "timestamp" in event :
				# skip broken event without a value for timestamp
				if event["timestamp"] != None :
					action_event.append(event)
			else :
				question_event.append(event)

		# sort the event by timestamp
		action_event.sort(key=lambda x: x["timestamp"])

		#print(action_event)
		if action_event != [] :
			print("action_event not empty")
			tmp=action_event[0]["timestamp"]
			for ev in action_event :
				if ev["timestamp"] < tmp:
					print("not sorted")
				tmp = ev["timestamp"]
		else :
			print("action_event empty")


		if action_event != [] and action_event != None:

			# keep track of info that can be extracted by the order of the actions
			current_x = ""
			current_y = ""
			current_floor = 1
			current_exhib = -1

			# from the action sorted by timestamp
			for event in action_event:

				# event type 1 is a movement, so we need to update x,y and floor
				if event["type"] == 1:
					current_x = event["x"]
					current_y = event["y"]
					current_floor = event["floorId"]

				# event type 2 is "start listening to exhibit explanation" so we update the current exhib
				if event["type"] == 2:
					current_exhib = event["exhibitId"]

				# event type 3 is "stopped listening to exhibit explanation" so we update the current exhib
				if event["type"] == 2:
					current_exhib = -1

				new_event = {
					'id' : user_id,
					'language' : langauge,
					'timestamp' : event["timestamp"],
					'x' : current_x,
					'y' : current_y,
					'floorId' : current_floor,
					'exhibitId' : current_exhib
				}

				new_stream.append(new_event)

out_file = open("FINAL__event_stream.json", "w")
out_file.write(json.dumps(new_stream, indent=2))
out_file.close()
			
