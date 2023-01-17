import json


in_file = open("wf__exhibit.json", "r")
data = json.load(in_file)
in_file.close()

rooms = []
exhibits = []
for exhib in data : 
	if exhib["type_id"] != "1" :
		exhibits.append(exhib)
	else :
		rooms.append(exhib)


out_file = open("wf__rooms.json", "w")
out_file.write(json.dumps(rooms, indent=2))
out_file.close()

out_file = open("wf__exhibit_new.json", "w")
out_file.write(json.dumps(exhibits, indent=2))
out_file.close()