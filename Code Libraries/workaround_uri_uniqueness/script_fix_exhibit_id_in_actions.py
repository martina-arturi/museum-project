from rdflib import Graph, Literal, RDF, URIRef
from rdflib import Namespace

file_name = "actions"


# read rooms ids from the rdf
g_r = Graph()
g_r.parse("RDF__rooms.ttl")

room_ids = []

for s, p, o in g_r.triples((None,RDF.type,URIRef("https://knowdive.disi.unitn.it/etype#Room"))):
	val = "" + s
	id_room = "exhibit_" + val.replace("http://localhost:8080/source/room_","")
	room_ids.append(id_room)

print(room_ids)

# read the file and split it into entities
inp = open("RDF__"+file_name+".ttl", "r")
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

	# fix exhibit ids
	for subj, pred, obj in g.triples((None,RDF.type,URIRef("https://knowdive.disi.unitn.it/etype#Exhibit"))):

		# retrieve the id
		val = "" + subj
		id_exhibit = val.replace("http://localhost:8080/source/","")

		if id_exhibit in room_ids :

			print(id_exhibit + " is a room actually")

			id_exhibit = "exhibit_-1"

			# remove previous triplet
			g.remove((subj,pred,obj))

			newSubj = URIRef("http://localhost:8080/source/"+id_exhibit)

			# add new one
			g.add((newSubj,pred,obj))

			# search for all the triples that have as subject the object to modify
			for s, p, o in g.triples((None,None,subj)):
				pred_string = ("" + p).replace("https://knowdive.disi.unitn.it/etype#","")

				if pred_string == 'involves':
					g.set((s,p,newSubj))


	v = g.serialize(format="nt")
	out_string += v + "\n"




out = open("RDF__"+file_name+"_fixed.ttl", "w")
out.write(out_string)
out.close()