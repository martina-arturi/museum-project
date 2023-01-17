from rdflib import Graph, Literal, RDF, URIRef
from rdflib import Namespace

file_name = "Exhibit"

# read the file and split it into entities
inp = open("RDF_2_"+file_name+".ttl", "r")
file_data = inp.read()
inp.close()
entities = file_data.split("\n\n")

# variable to store the resulting file
out_string = ""

# for each entity found fix the types
for entity in entities :

	in_predicate = None

	# parse the graph of the given entity
	g = Graph()
	g.parse(data=entity, format="nt")

	# fix floor ids
	for subj, pred, obj in g.triples((None,RDF.type,URIRef("https://knowdive.disi.unitn.it/etype#Floor"))):

		# retrieve the id
		val = "" + subj
		id_floor = val.replace("http://localhost:8080/source/exhibit/","")

		# remove previous triplet
		g.remove((subj,pred,obj))

		newSubj = URIRef("http://localhost:8080/source/floor/"+id_floor)

		# search for all the triples that have as subject the object to modify
		for s, p, o in g.triples((None,None,subj)):
			pred_string = ("" + p).replace("https://knowdive.disi.unitn.it/etype#","")

			if pred_string == 'in':
				if in_predicate == None :
					in_predicate = p
				g.remove((s,p,o))
				
		g.add((s,in_predicate,newSubj))
			
		# add new one
		g.add((newSubj,pred,obj))

	# fix room ids
	for subj, pred, obj in g.triples((None,RDF.type,URIRef("https://knowdive.disi.unitn.it/etype#Room"))):

		# retrieve the id
		val = "" + subj
		id_room = val.replace("http://localhost:8080/source/exhibit/","")

		# remove previous triplet
		g.remove((subj,pred,obj))

		newSubj = URIRef("http://localhost:8080/source/room/"+id_room)

		for s, p, o in g.triples((None,None,subj)):
			pred_string = ("" + p).replace("https://knowdive.disi.unitn.it/etype#","")

			if pred_string == 'in':
				if in_predicate == None :
					in_predicate = p
				g.remove((s,p,o))

		g.add((s,in_predicate,newSubj))
			
		# add new one
		g.add((newSubj,pred,obj))


	v = g.serialize(format="nt")
	out_string += v + "\n"




out = open("RDF__"+file_name+"_fixed.ttl", "w")
out.write(out_string)
out.close()