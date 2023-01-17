import json


in_file = open("wf__exhibit_with_authors.json", "r")
data_exhibit = json.load(in_file)
in_file.close()

# change the keys of exhibit to be more readable

new_exhibit = []
for exhib in data_exhibit : 
	new_val = {
		'id' : exhib["id"],
		'name' : exhib["name"],
		'floor' : exhib["floor_id"],
		'type' : exhib["type_id"],
		'location' : exhib["icon_pos_str"],
		'room' : exhib["parent_id"],
		'authors' : [ exhib['author'] ]
	}
	new_exhibit.append(new_val)


out_file = open("wf__exhibit_formatted2.json", "w")
out_file.write(json.dumps(new_exhibit, indent=2))
out_file.close()