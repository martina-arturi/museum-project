import json

in_file = open("wf__session_content.json", "r")
data_session = json.load(in_file)
in_file.close()

in_file = open("wf__questions.json", "r")
data_question = json.load(in_file)
in_file.close()

questionList = data_question["questionList"]

from1_answers = []
from2_answers = []

for q in questionList :
	if q["id"] == 3:
		for a in q["answerList"] :
			from1_answers.append({
				"id" : a["id"],
				"a" : a["answerTranslation"]["en"]
				})
	if q["id"] == 4:
		for a in q["answerList"] :
			from2_answers.append({
				"id" : a["id"],
				"a" : a["answerTranslation"]["en"]
				})

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

		if question_event != [] : 
			answer_q_1 = -1
			answer_q_2 = -1
			answer_q_3 = -1
			answer_q_4 = -1

			for q in question_event:
				if q["questionId"] == 1 :
					answer_q_1 = q["answerId"]

				if q["questionId"] == 2 :
					answer_q_2 = q["answerId"]

				if q["questionId"] == 3 :
					answer_q_3 = q["answerId"]

				if answer_q_3 == 1 and q["questionId"] == 4:
					answer_q_4 = q["answerId"]

			answer_gender = ""
			if answer_q_1 == 1 : 
				answer_gender = "Male"
			else :
				answer_gender = "Female"

			answer_eta = ""
			if answer_q_2 == 1 : 
				answer_eta = "14-25"
			if answer_q_2 == 2 : 
				answer_eta = "26-35"
			if answer_q_2 == 3 : 
				answer_eta = "36-45"
			if answer_q_2 == 4 : 
				answer_eta = "46-54"
			if answer_q_2 == 5 : 
				answer_eta = "55-64"
			if answer_q_2 == 6 : 
				answer_eta = "65 and over"

			answer_from = ""
			if answer_q_3 == 1 :
				for a in from2_answers:
					if a["id"] == answer_q_4 :
						answer_from = a["a"]
			else :
				for a in from1_answers:
					if a["id"] == answer_q_3 :
						answer_from = a["a"]

			if answer_from == "" :
				answer_from = "Unknown"
				
			new_event = {
					'id' : user_id,
					'gender' : answer_gender,
					'eta' : answer_eta,
					'provenience' : answer_from,
					'hobbies' : "unknown",
					'name' : "unknown",
					'surname' : "unknown",
					'occupation' : "unknown"
				}

			new_stream.append(new_event)


out_file = open("FINAL__users_info.json", "w")
out_file.write(json.dumps(new_stream, indent=2))
out_file.close()
			
