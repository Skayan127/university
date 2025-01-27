
# Rayan Alnakar, rayana@kth.se
# Project d2, DD1321 "Tillämpad programmering och datalogi"
# 2021-02-01


class DictHash():

    def __init__(self):
        self.__dict = {}

    def __getitem__(self,key):
        return self.search(key)

    def __setitem__(self,key,value):
        self.store(key,value)

    def __contains__(self,key):
        return key in self.__dict

    def store(self,key,value):
        self.__dict[key] = value
    
    def search(self,key):
        return self.__dict[key]







