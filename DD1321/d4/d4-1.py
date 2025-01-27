# Rayan Alnakar, rayana@kth.se
# Project d4, DD1321 "Tillämpad programmering och datalogi"
# 2021-02-01

from DictHash import DictHash
from quicksort import *
from mergesort import *

import timeit
import random

dic_klass = DictHash()

class Song():   # Klass för sångobjekten med metoder och attribut.

    def __init__(self,artist,song):
        self.artist = artist
        self.song = song

    def __str__(self):
        return self.artist , self.song

    def __lt__(self,other):
        return min(self.artist, other.artist) == self.artist


def readfile(filnamn):   # Funktion som läser in filinnehållet
    y = []
    artist_song_objs=[]
    artist_list=[]
    song_list=[]
    with open(filnamn, "r") as text_file:
        data = text_file.readlines()

    for x in range(0,len(data)):    # "Rensar" filinnehållet så att man får strängar för sig själva
        y.extend([data[x].split('<SEP>')])
        y[x][3] = y[x][3].rstrip("\n")
        artist_song_objs.append(Song(y[x][2],y[x][3]))
        dic_klass[y[x][2]] = y[x][3]
        artist_list.append(y[x][2])
        song_list.append(y[x][3])
    return artist_song_objs, dic_klass, artist_list, song_list



fildata = readfile("unique_tracks.txt") # Kallar på funktionen och sparar det returnerade till variabel fildata
fillangd = len(fildata)

artist_list = fildata[2]
song_list = fildata[3]


def linsok(lista, testartist):    # Hämtad från föreläsningsanteckningar
    for count,ele in enumerate(lista):
        if ele == testartist:
            return testartist,count
    return False


def binary_search(lista, testartist): # Hämtad från föreläsningsanteckningar
   low = 0
   high = len(lista)-1
   found = False

   while low <= high and not found:
      middle = (low + high)//2
      if lista[middle] == testartist:
         found = True
      else:
         if testartist < lista[middle]:
            high = middle - 1
         else:
            low = middle + 1
   return found



def linsok1000(data):
    for i in range(10):
        r = int(random.random() * len(data)//1 - 1)
        linsok(data,data[r])




#--------------------------------------------------------------------------------------
# Tidtagning
# 


nastSista = artist_list[-2]
numberOfTimes = 100


linsok_osorterad = timeit.timeit(stmt = lambda: linsok(artist_list, nastSista), number = numberOfTimes) # Hämtad från föreläsningen, likaså för de nedre exemplen.
print("Linjärsökningen (osorterad lista, näst sista elementet) tog", round(linsok_osorterad, 4) , "sekunder")



linsok_1000_osorterad = timeit.timeit(stmt = lambda: linsok1000(artist_list), number = numberOfTimes)
print("Linjärsökningen (osorterad lista, 1000 slumpade element) tog", round(linsok_1000_osorterad, 4) , "sekunder")


quicksorterad = timeit.timeit(stmt = lambda: quicksort(artist_list), number = numberOfTimes)
print("Sorteringen (quicksort) tog", round(quicksorterad, 4) , "sekunder")


linsok_sorterad = timeit.timeit(stmt = lambda: linsok(artist_list, nastSista), number = numberOfTimes)
print("Linjärsökningen (sorterad lista, näst sista elementet) tog", round(linsok_sorterad, 4) , "sekunder")



binsok_sorterad = timeit.timeit(stmt = lambda: binary_search(artist_list, nastSista), number = numberOfTimes)
print("Binärsökning (sorterad lista, näst sista elementet) tog", round(binsok_sorterad, 4) , "sekunder")


dict_sokning = timeit.timeit(stmt = lambda: dic_klass.search(nastSista), number = numberOfTimes)
print("Uppslagning i dictionary (näst sista elementet) tog", round(dict_sokning, 4) , "sekunder")

print(round(linsok_osorterad, 4) , round(linsok_1000_osorterad, 4), round(quicksorterad, 4), round(linsok_sorterad, 4), round(binsok_sorterad, 4), round(dict_sokning, 4))
