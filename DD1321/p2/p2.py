
# Programmeringsuppgift p2


import sys

alfabet = {'a': 'A', 
            'b': 'B',
            'c': 'C',
            'd': 'D',
            'e': 'E',
            'f': 'F',
            'g': 'G',
            'h': 'H',
            'i': 'I',
            'j': 'J',
            'k': 'K',
            'l': 'L',
            'm': 'M',
            'n': 'N',
            'o': 'O',
            'p': 'P',
            'q': 'Q',
            'r': 'R',
            's': 'S',
            't': 'T',
            'u': 'U',
            'v': 'V',
            'w': 'W',
            'x': 'X',
            'y': 'Y',
            'z': 'Z'}



## 2.1 Stora och små bokstäver

###########################################################################
##
## IN  sträng (bokstav)
##     
## OUT sträng (bokstav)
##
## INTENTION: en hjälpfunktion som tar en bokstav och returnerar stor bokstav 
## (om det går, annars returneras parametern oförändrad)
## Använder en dictionary där jag hårdkodar in alfabetets små och stora bokstäver.
##


def liten_stor_bokstav(bokstav):
    if bokstav in alfabet:
        return alfabet[bokstav]
    else:
        return bokstav

#print(liten_stor_bokstav('t'))





#txt = "     banana     "
#x = txt.strip()
#print("of all fruits", x, "is my favorite")



with open("p2_passwords.txt", "r") as text_file:
    data = text_file.readlines()

y = []
for x in range(0,len(data)):
    y.extend([data[x].strip()])

#print(y)
#print(data[1].strip(data[1]))










list_of_combinations = []


siffra_tecken_lista = ['0','1','2','3','4']

for k in range (0,len(y)):
    word = y[k]
    






    ## 2.2 Lista med en stor bokstav

    ###########################################################################
    ##
    ## IN  sträng (ett ord)
    ##     
    ## OUT lista (vektor av modifierade ordet)
    ##
    ## INTENTION: En funktion som tar en sträng och returnerar 
    ## en lista av ord där en av bokstäverna gjorts till stor bokstav.
    ## 
    ##



    stor_bokstav_lista = []
    def stor_bokstav(ord):
        for i in range(0,len(ord)):
            stor_bokstav_lista.extend([(ord[:i] + liten_stor_bokstav(ord[i]) + ord[i+1:])])

    stor_bokstav(word)
    # print(stor_bokstav_lista)
    # print('Antalet ord i 1 stor bokstavslistan är: ', len(stor_bokstav_lista),'\n')









    ## 2.3 Lista med två stora bokstäver

    ###########################################################################
    ##
    ## IN  sträng (ett ord)
    ##     
    ## OUT lista (vektor av modifierade ordet)
    ##
    ## INTENTION: Skriv en funktion som tar en sträng och returnerar en lista av ord 
    ## där alla kombinationspar av två bokstäver har gjorts till versal.
    ## 
    ## n(n+1)/2
    ##


    #text = 'abcdefg'
    #new = list(text)
    #new[6] = 'W'
    #''.join(new)



    tva_stora_lista = []
    def tva_stora(ord):
        for i in range(0,len(ord)):
            for j in range(i+1,len(ord)):
                new = list(ord)
                new[i] = liten_stor_bokstav(ord[i])
                new[j] = liten_stor_bokstav(ord[j])
                modifierat_ord = ''.join(new)
                tva_stora_lista.extend([modifierat_ord])


    tva_stora(word)
    # print(tva_stora_lista)
    # print('Antalet ord i 2 stora bokstavslistan är: ', len(tva_stora_lista),'\n')







    ## 2.4 Lista med en inskjuten siffra eller specialtecken

    ###########################################################################
    ##
    ## IN  sträng (ett ord)
    ##     
    ## OUT lista (vektor av modifierade ordet)
    ##
    ## INTENTION: Skriv en funktion som givet en sträng skjuter in en siffra eller 
    ## ett specialtecken ( + - * / ). De ska läggas in i början och slutet och mellan varje bokstav.
    ## 
    ## 
    ## 
    ##



    skjutinspecial_lista = []

    def skjutinspecial(ord):
        for i in range(0,len(ord)+1):
            for x in siffra_tecken_lista:
                skjutinspecial_lista.extend([ord[:i] + x + ord[i:]])


    skjutinspecial(word)
    # print(skjutinspecial_lista)
    # print('Antalet ord i skjutinspeciallistan är: ', len(skjutinspecial_lista),'\n\n\n\n\n\n\n')



    # tot_komb = len(stor_bokstav_lista) + len(tva_stora_lista) + len(skjutinspecial_lista) + 1
    # print('Totalt olika kombinationer: ', tot_komb,'\n\n\n')


    




    ## 2.5 Kombinera metoderna

    ###########################################################################
    ##
    ## IN  sträng (ett ord)
    ##     
    ## OUT lista (vektor av totala antalaet modifierade ord)
    ##
    ## INTENTION: Funktionen kombinerar metoderna från ovan och ser till att dubbletter undviks. 
    ## 
    ## 
    ## 
    ##




    komb_metoder_lista = [word] + stor_bokstav_lista + tva_stora_lista
    #print(komb_metoder_lista)
    total_antal_kombinationer = []


    def komb_metoder(ord):
        for x in siffra_tecken_lista:
            for i in range(0,len(komb_metoder_lista)):
                for j in range(0,len(komb_metoder_lista)):
                    if komb_metoder_lista[i][:j] + x + komb_metoder_lista[i][j:] not in total_antal_kombinationer:
                        total_antal_kombinationer.extend([komb_metoder_lista[i][:j] + x + komb_metoder_lista[i][j:]])


    komb_metoder(word)
    total_antal_kombinationer = komb_metoder_lista + total_antal_kombinationer
    #print(total_antal_kombinationer)
    #print('Antalet ord i kombinerade metoder listan är: ', len(total_antal_kombinationer))

    list_of_combinations = list_of_combinations + total_antal_kombinationer



#print('Totala antalet kombinationer för vart och ett av lösenorden i filen: ', len(list_of_combinations))

#f = open("my_own_p2_combinations.txt", "x")









## 2.6 Komplexitetsundersökning




















## 2.7 Lösenord på fil
##
###########################################################################
##
## IN  filnamn OCH lista med alla olika kombinationer
##     
## OUT textfil som innehåller alal olika kombinationer
##
## INTENTION: Funktionen skriver in alla olika kombinationer i en textfil. 
## 
## 
## 
##



## Färdig funktion från p2 

def save_file_content(my_own_p2_combinations, list_of_combinations):
    with open("my_own_p2_combinations.txt", 'w') as f: 
        for item in list_of_combinations: 
            f.write("%s\n" % item)



save_file_content("my_own_p2_combinations.txt", list_of_combinations)













## 2.8 Kommandoradsargument

###########################################################################
##
## IN  sträng (ett eller flera argument)
##     
## OUT sträng (meddelande hurvuda lösenordet är lämpligt eller ej)
##
## INTENTION: Programmet tar in ett eller flera argument  och 
## skriver ut ifall det/de är lämpligt/lämpliga som lösenord.
## 
## 
## 



with open("my_own_p2_combinations.txt", "r") as text_file:
    data = text_file.readlines()

y = []
for x in range(0,len(data)):
    y.extend([data[x].strip()])

print(len(y))


if len( sys.argv ) > 1:
    for i in range(0,len(sys.argv)):
        word_to_test = sys.argv[i]
        if word_to_test in y:
            print('"' + sys.argv[i] + '" är ett olämpligt lösenord!')

