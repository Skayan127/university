
# Rayan Alnakar, rayana@kth.se
# Project d2, DD1321 "Tillämpad programmering och datalogi"
# 2021-02-01

import math

class HashNode():

    def __init__(self,nyckel,varde):
        self.nyckel = nyckel
        self.varde = varde

    def __str__(self):
        return str(self.nyckel) + str(self.varde)

class Hashtabell():

    def __init__(self,storlek):

        storlek = self.__primtal(storlek*2)
        self.__dictionary = [None] * storlek
        self.__hashtabell_storlek = storlek
        self.__element = 0


    def __getitem__(self,nyckel):
        return self.search(nyckel)

    def __setitem__(self,nyckel,varde):
        self.store(nyckel,varde)

    def __str__(self):
        return "Hashtabell med " + str(self.__element) + " element"

    def __primtal(self,nummer):
        b = 0
        while b != 1:
            if nummer > 1:
                for i in range(2, math.ceil(math.sqrt(nummer))+1):
                    if (nummer % i) == 0:
                        a=0
                        break
                    else:
                        a=1
            if a == 1:
                b = 1
            else:
                nummer += 1
                b = 0
        return nummer
        


    def __hashfunktion(self,nyckel):
        result = 0

        for c in nyckel:
            result = result*32 + ord(c)
        return result % self.__hashtabell_storlek

    
    def store(self,nyckel,varde):

        for n in range(self.__hashtabell_storlek):

            ind = (self.__hashfunktion(nyckel) + n**2) % self.__hashtabell_storlek

            if self.__dictionary[ind] == None:

                self.__element = self.__element + 1
                self.__dictionary[ind] = HashNode(nyckel,varde)
                break

            elif self.__dictionary[ind].nyckel == nyckel:

                self.__dictionary[ind].varde = varde
                break


    def search(self,nyckel):

        for n in range(self.__hashtabell_storlek):
            ind = (self.__hashfunktion(nyckel) + n**2) % self.__hashtabell_storlek


            if self.__dictionary[ind] == None:
                break

            elif self.__dictionary[ind].nyckel == nyckel:
                return self.__dictionary[ind].varde
        
        raise KeyError(nyckel)