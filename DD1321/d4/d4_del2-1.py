

from quicksort import *
from mergesort import *
import timeit
class Songlength(): # Klass för sångobjekten med metoder och attribut.

    def __init__(self,artist,song,length):
        self.artist = artist
        self.song = song
        self.length = length

    def __str__(self):
        return self.artist , self.song, self.length

    def __lt__(self,other):                                                     
        return min(self.length, other.length) == self.length



def readfile(filnamn):   # Funktion som läser in filinnehållet
    y = []
    artist_song__length_objs=[]
    artist_list=[]
    song_list=[]
    song_length=[]
    with open(filnamn, "r") as text_file:
        data = text_file.readlines()

    for x in range(0,len(data)):    # "Rensar" filinnehållet så att man får strängar för sig själva
        y.extend([data[x].split('\t')])
        y[x][4] = y[x][4].rstrip("\n")
        artist_song__length_objs.append(Songlength(y[x][1],y[x][2],y[x][3]))
        artist_list.append(y[x][1])
        song_list.append(y[x][2])
        song_length.append(float(y[x][3]))
    return artist_song__length_objs, artist_list, song_list, song_length

filename="sang_artist_data.txt"

fildata = readfile(filename) # Kallar på funktionen och sparar det returnerade till variabel fildata
fildata2 = readfile(filename) # Kallar på funktionen och sparar det returnerade till variabel fildata2

artist_list = fildata[1]
song_list = fildata[2]
song_length = fildata[3]
song_length2 = fildata2[3]


# Metod 1 – upprepade linjärsökningar
print("Antal element:",len(song_length))

def metod1(lista, k):    # Hämtad från föreläsningsanteckningar, men har redigerat lite själv också.
    
    for i in range(k-1):
        max_value = lista[0]
        for ele in lista:
            if ele > max_value:
                max_value = ele
        lista.remove(max_value)
    
    max_value=lista[0]
    for ele in lista:
        if ele > max_value:
            max_value = ele
    return max_value



# Metod 2 – sortera och plocka ut
def metod2(lista,k):
    quicksort(song_length2)
    return song_length2[-k]



k = 1

while k <= 40:
   time_1 = timeit.timeit(stmt = lambda: metod1(song_list, k), number = 1)
   time_2 = timeit.timeit(stmt = lambda: metod2(song_list, k), number = 1)
   
   if time_1 < time_2:
       print("k:",k,", Metod 1:" ,"**"+str(round(time_1,4))+"**", "Metod 2:",round(time_2,4))
   else:
        print("k:",k,", Metod 1:" ,round(time_1,4),"Metod 2:","**"+str(round(time_2,4))+"**")

   k += 4






