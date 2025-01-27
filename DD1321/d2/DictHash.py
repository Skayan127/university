
# Rayan Alnakar, rayana@kth.se
# Project d2, DD1321 "Tillämpad programmering och datalogi"
# 2021-02-01


class DictHash():

    def __init__(self):
        self.__dictionary = {}

    def __getitem__(self, nyckel):
        return self.search(nyckel)

    def __setitem__(self, nyckel, varde):
        self.store(nyckel,varde)

    def __str__(self):
        return "DictHash med " + str(len(self.__dictionary)) + " elements"

    def store(self, nyckel, varde):
        self.__dictionary[nyckel] = varde
    
    def search(self, nyckel):
        return self.__dictionary[nyckel]