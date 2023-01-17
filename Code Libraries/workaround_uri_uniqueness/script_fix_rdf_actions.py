from rdflib import Graph, Literal, RDF, URIRef
from rdflib import Namespace

file_name = "Actions"


# read rooms ids from the rdf
g_r = Graph()
g_r.parse("RDF__Rooms_fixed.ttl")

room_ids = []

for s, p, o in g_r.triples((None,RDF.type,URIRef("https://knowdive.disi.unitn.it/etype#Room"))):
	val = "" + s
	id_room = val.replace("http://localhost:8080/source/room/","")
	room_ids.append(id_room)

# read the file and split it into entities
inp = open("RDF_2_"+file_name+".ttl", "r")
file_data = inp.read()
inp.close()
entities = file_data.split("\n\n")

# variable to store the resulting file
out_string = ""

# for each entity found fix the types
for entity in entities :

	# parse the graph of the given entity
	g = Graph()
	g.parse(data=entity, format="nt")

	# fix floor ids
	for subj, pred, obj in g.triples((None,RDF.type,URIRef("https://knowdive.disi.unitn.it/etype#Floor"))):

		# retrieve the id
		val = "" + subj
		id_floor = val.replace("http://localhost:8080/source/action/","")

		# remove previous triplet
		g.remove((subj,pred,obj))

		newSubj = URIRef("http://localhost:8080/source/floor/"+id_floor)

		# search for all the triples that have as subject the object to modify
		for s, p, o in g.triples((None,None,subj)):
			pred_string = ("" + p).replace("https://knowdive.disi.unitn.it/etype#","")

			if pred_string == 'in':
				g.set((s,p,newSubj))

			
		# add new one
		g.add((newSubj,pred,obj))

	# fix exhibit ids
	for subj, pred, obj in g.triples((None,RDF.type,URIRef("https://knowdive.disi.unitn.it/etype#Exhibit"))):

		# retrieve the id
		val = "" + subj
		id_exhibit = val.replace("http://localhost:8080/source/action/","")

		if id_exhibit in room_ids :
			id_exhibit = "-1"

		# remove previous triplet
		g.remove((subj,pred,obj))

		newSubj = URIRef("http://localhost:8080/source/exhibit/"+id_exhibit)

		# search for all the triples that have as subject the object to modify
		for s, p, o in g.triples((None,None,subj)):
			pred_string = ("" + p).replace("https://knowdive.disi.unitn.it/etype#","")

			if pred_string == 'involves':
				g.set((s,p,newSubj))

			
		# add new one
		g.add((newSubj,pred,obj))

	# fix exhibit ids
	for subj, pred, obj in g.triples((None,RDF.type,URIRef("https://knowdive.disi.unitn.it/etype#Visitor"))):

		# retrieve the id
		val = "" + subj
		id_visitor = val.replace("http://localhost:8080/source/action/","")

		# remove previous triplet
		g.remove((subj,pred,obj))

		newSubj = URIRef("http://localhost:8080/source/visitor/"+id_visitor)

		# search for all the triples that have as subject the object to modify
		for s, p, o in g.triples((None,None,subj)):
			pred_string = ("" + p).replace("https://knowdive.disi.unitn.it/etype#","")

			if pred_string == 'is_done_by':
				g.set((s,p,newSubj))

			
		# add new one
		g.add((newSubj,pred,obj))



	v = g.serialize(format="nt")
	out_string += v + "\n"




out = open("RDF_2_"+file_name+"_fixed.ttl", "w")
out.write(out_string)
out.close()