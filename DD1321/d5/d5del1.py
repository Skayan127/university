# Rayan Alnakar, rayana@kth.se
# Project d5, DD1321 "Tillämpad programmering och datalogi"
# 2021-02-22
# Använde Youtube som huvudkälla för att bekanta mig med binära träd och tog till mig av deras förklaringar.

import os
if os.stat("output.txt").st_size==1:
	open('output.txt', 'w').close()



class Node:
	def __init__(self,nyckel = None,data = None):
		self.vanster_barn = None
		self.hoger_barn = None
		self.nyckel = nyckel
		self.data = data

class Bintree:
	def __init__(self):
		self.root = None

	def store(self,nyckel,data):
		if self.root == None:
			self.root = Node(nyckel,data)
		else:
			self._rekstore(nyckel,data,self.root)

	def _rekstore(self,nyckel,data,akt_nod):
		if nyckel<akt_nod.nyckel:
			if akt_nod.vanster_barn == None:
				akt_nod.vanster_barn = Node(nyckel,data)
				akt_nod.vanster_barn.foralder = akt_nod
			else:
				self._rekstore(nyckel,data,akt_nod.vanster_barn)
		elif nyckel>akt_nod.nyckel:
			if akt_nod.hoger_barn == None:
				akt_nod.hoger_barn = Node(nyckel,data)
				akt_nod.hoger_barn.foralder = akt_nod
			else:
				self._rekstore(nyckel,data,akt_nod.hoger_barn)
		else:
			pass #print("Noden finns redan!")



	def __contains__(self, nyckel):
		if self.root != None:
			return self._contains(nyckel,self.root)
		else:
			#raise KeyError(nyckel)
			return False
	

	def _contains(self,nyckel,akt_nod):
		if nyckel == akt_nod.nyckel:
			return True
		elif nyckel<akt_nod.nyckel and akt_nod.vanster_barn != None:
			return self._reksearch(nyckel,akt_nod.vanster_barn)
		elif nyckel>akt_nod.nyckel and akt_nod.hoger_barn != None:
			return self._reksearch(nyckel,akt_nod.hoger_barn)
		return False
		#raise KeyError(nyckel)


	def search(self,nyckel):
		if self.root != None:
			return self._reksearch(nyckel,self.root)
		else:
			raise KeyError(nyckel)
			#return False

	def _reksearch(self,nyckel,akt_nod):
		if nyckel == akt_nod.nyckel:
			return akt_nod.data
		elif nyckel<akt_nod.nyckel and akt_nod.vanster_barn != None:
			return self._reksearch(nyckel,akt_nod.vanster_barn)
		elif nyckel>akt_nod.nyckel and akt_nod.hoger_barn != None:
			return self._reksearch(nyckel,akt_nod.hoger_barn)
		raise KeyError(nyckel)


	def write(self):
		if self.root != None:
			self._rekwrite(self.root)

	def _rekwrite(self,akt_nod):
		if akt_nod != None:
			self._rekwrite(akt_nod.vanster_barn)
			with open("output.txt", "a") as f:
				print((str(akt_nod.nyckel)), file=f)
				#print (str(akt_nod.nyckel))
				f.close()
			self._rekwrite(akt_nod.hoger_barn)
			f.close()

# tree = Bintree()

tree=Bintree()

# c.store("banan", "frukt")
# c.store("gurka", "grönsak")
# c.store("bil", "fordon")
# c.store("penna","kontor")
# c.store("mus","elektronik")
# c.store("jord","himmel")
# c.store("fysik","kemi")
# c.store("apelsin","frukt2")
# c.store("aloe","växt")

# c.write()

# word="fysik"
# print("\n")
# print(c.search(word))


# tree.store("grönsak","gurka")
# tree.store("frukt","banan")
# tree.store("fordon","bil")


# tree.store("gurka", "grönsak")
# tree.store("banan", "frukt")
# tree.store("bil", "fordon")

# numbers=[1,2,3,4,5,6,7,8]


# first = ["dator",   "gurka", "banan", "bil",  "hammare","lejon"] # banan bil dator gurka hammare
# second = ["teknik","grönsak","frukt","fordon","verktyg","djur"]

# for i in range(len(numbers)):
# 	#tree.store(first[i],second[i])
# 	#tree.store(first[i],second[i])
# 	tree.store(numbers[i],numbers[i])	

# tree.write()




# f = open("output.txt", "a")
# (tree.write(), file=f)
# f.close()
# tree.write()
#print("\n")







# wordcontain="mjöl"
# for i in range(len(first)):
# 	if first[i] in tree:
# 		print(first[i] in tree)
# 		#print("Ordet:",first[i], "finns i trädet!")
# 	else:
# 		print("Existerar EJ!")

# print("\n")
# t = list((tree.write()))
# print(t)
# tree.write2()
# tree.store(first[0],second[0])
# tree.store(first[1],second[1])
# tree.store(first[2],second[2])
# tree.store(first[3],second[3])
# tree.store(first[4],second[4])



# if "banan" in c:
# 	print("bananen finns med!")



# for i in range(len(first)):
# 	print(first[i]+":",tree.search(first[i]))	

# print(first[0],":",tree.search(first[0]))
# print(first[1],":",tree.search(first[1]))
# print(first[2],":",tree.search(first[2]))
# print(first[3],":",tree.search(first[3]))
# print(first[4],":",tree.search(first[4]))


# for i in range(len(first)):
# 	print(first[i]+":",tree.search(first[i]))

# print(second[0],":",tree.search(second[0]))
# print(second[1],":",tree.search(second[1]))
# print(second[2],":",tree.search(second[2]))
# print(second[3],":",tree.search(second[3]))
# print(second[4],":",tree.search(second[4]))


#print("papr:",tree.search("papr"))




