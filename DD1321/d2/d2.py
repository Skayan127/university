

from DictHash import DictHash
from hashtabell import HashNode, Hashtabell            

def las_fil(filnamn):
    y = []
    with open(filnamn, "r") as text_file:
        data = text_file.readlines()

    for x in range(0,len(data)):
        y.extend([data[x].split('<SEP>')])
        y[x][3] = y[x][3].rstrip("\n")
    return y


fildata = las_fil("unique_tracks.txt") 
fillangd = len(fildata)

dic_klass = DictHash()
hash_klass = Hashtabell(fillangd)

for f in range(fillangd):
    artist = fildata[f][2]
    sang = fildata[f][3]
    dic_klass[artist] = sang
    hash_klass[artist] = sang

sokord = "Stevie Wonder"
print("Testar Store-funktionen")
print("Totala element att lagra:",f'{fillangd:,}')
print(hash_klass)
print(dic_klass)
print("\n")
print("Testar Search-funktionen")
print(sokord + ", Hashtabell:", hash_klass[sokord])
print(sokord + ", DictHash:", dic_klass[sokord])