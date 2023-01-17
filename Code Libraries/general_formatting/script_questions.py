import json

# script to convert questions data from csv to a json, keeping only the question

in_file = open("questions.json", "r")
data = json.load(in_file)
in_file.close()

questions = data["questionList"]

list_id_question = []
for q in questions : 
	dictionary = {"id":q["id"], "question":q["question"]}
	list_id_question.append(dictionary)


out_file = open("wf__just_question_with_id.json", "w")
out_file.write(json.dumps(list_id_question, indent=2))

out_file.close()