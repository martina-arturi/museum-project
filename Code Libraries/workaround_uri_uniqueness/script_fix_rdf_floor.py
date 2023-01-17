from rdflib import Graph, Literal, RDF, URIRef
from rdflib import Namespace

n = Namespace("http://localhost:8080/source/")


# read the file and split it into entities
inp = open("RDF_2_Floors.ttl", "r")
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
	
	for subj, pred, obj in g:

		# fix museum type
		if obj == URIRef("https://knowdive.disi.unitn.it/etype#Museum") and pred == RDF.type :

			# retrieve the id
			val = "" + subj
			id_museum = val.replace("http://localhost:8080/source/floor/","")

			# remove previous triplet
			g.remove((subj,pred,obj))

			newSubj = URIRef("http://localhost:8080/source/museum/"+id_museum)

			# search for all the triples that have as subject the object to modify
			for s, p, o in g.triples((None,None,subj)):
				g.set((s,p,newSubj))

			
			# add new one
			g.add((newSubj,pred,obj))

	v = g.serialize(format="nt")
	out_string += v + "\n"




out = open("RDF__Floors_fixed.ttl", "w")
out.write(out_string)
out.close()