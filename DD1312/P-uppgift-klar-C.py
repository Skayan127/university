#P-uppgift 140: Sålda biobiljetter av Rayan Alnakar CLGYM17
print("===============SÅLDA BIOBILJETTER===============")
class Biograf:
    #Klass som fungerar som mall för de olika biografer
    
    def __init__(self, namn, platser, V_pris, P_pris, B_pris):
        #Attrbibuterna för klassen; egenskaperna som varje Biografobjekt ska ha
        self.namn = namn
        self.platser = platser
        self.V_pris = V_pris
        self.P_pris = P_pris
        self.B_pris = B_pris
        self.beläggning = 0
        self.intäkter = 0


    def __str__(self):
        #str-metod som senare används för att skriva ut listan med biografer som finns i inlästa filen
        return "\nName: " + self.namn +\
               "\nAntal platser: " + str(self.platser) +\
               "\nVuxenpris: " + str(self.V_pris) +\
               "\nPensionärpris: " + str(self.P_pris) +\
               "\nBarnpris: " + str(self.B_pris)
    def __lt__(self, biograf2):
        #lt-metod som används för att sortera den utskrivna listan efter beläggning baserat på användarens inmatning
        return self.beläggning < biograf2.beläggning



def inläsning():
    #Här läses filen in och läggs i en lista. try & except används för att kontrollera ifall den angivna filen existerar
    biografers = list()
    try:
        infil = open("Biografer2-3.txt","r")
        rad = infil.readline() # för rad 1
    except FileNotFoundError:
        print("Den angivna filen existerar inte!")
        raise SystemExit()
        #SystemExit stoppar hela programmet om den angivna filen inte existerar
    while rad!="":
        rad = rad.rstrip("\n")
        biografinfo = rad.split(";")

        if len(rad.strip(";").split(";")) != 5:
            #Ser till att varje biograf i filen har samma format,dvs att alla har fem kolumner med namn, platser och tre prisklasser
                    print(rad, "har fel kolumnformat!")
                    raise SystemExit()
        
        b = Biograf((biografinfo[0]),int(biografinfo[1]),int(biografinfo[2]),int(biografinfo[3]),int(biografinfo[4]))
        #Gör ett klassobjekt av en biograf i filen och läggs sedan i listan, sedan läses andra raden osv tills antalet biografer är slut 
        biografers.append(b)
        rad = infil.readline() # för rad 2+
    infil.close()
    return biografers

biografers = inläsning()



for biograf in biografers:
    #skriver ut alla biografer och deras egenskaper från filen
    print(biograf)

totalintäkter = 0
for biograf in biografers:
    #for-loop där användaren matar in antalet sålda biobiljetter för varje biograf
    inmatningsfel = True
    while inmatningsfel:
        inmatningsfel = False
        try:
            #try & except som ser till att användarens inmatning enbart är heltal, annars ges felmeddelande
            vuxenplatser = int(input("\nAntal sålda vuxenbiljetter för " + biograf.namn +  ": "))
            pensionsplatser = int(input("Antal sålda pensionärbiljetter för " + biograf.namn + ": "))
            barnplatser = int(input("Antal sålda barnbiljetter för " + biograf.namn + ": "))
        except ValueError:
                print("Det där var inget heltal, försök igen!")
                inmatningsfel = True
    #Här beräknas användarens inmatningar som ger intäkter, beläggning samt antalet uppköpta platser för respektive biograf 
    biograf.intäkter = (vuxenplatser*biograf.V_pris+pensionsplatser*biograf.P_pris+barnplatser*biograf.B_pris)
    biograf.beläggning = round(100*(vuxenplatser+pensionsplatser+barnplatser)/biograf.platser)
    biograf.upptagnaplatser = vuxenplatser + pensionsplatser + barnplatser

    if biograf.upptagnaplatser > biograf.platser:
        #En if-sats som alarmerar användaren om att det totala antalet angivna platser överstiger antalet tillgängliga platser
        print("Totala antalet angivna platser överstiger antalet tillgängliga platser!")

    if not biograf.V_pris > biograf.P_pris > biograf.B_pris:
        #En if-sats som ser till att prisreglerna följs(barnbiljetter billigast osv), annars ges felmeddelande för berörd biograf
        #Vid felaktigt prisformat i filen upphör programmet från att köras med hjälp av SystemExit
            print("\nFilformatet är fel för biografen", biograf.namn + "!!!")
            raise SystemExit()            

biografers = sorted(biografers, reverse=True)
#Ser till att den slutliga utskriften efter användarens inmatningar sorteras efter beläggning, där den med störst andel komemr först osv
for biograf in biografers:
    #for-loop som ser till att utdata kommer ut efter användarens inmatning, där utskriften anger biografernas namn, intäkter,
    #antal upptagna platser samt beläggning i procent
    print("\n", biograf.namn + ":", str(biograf.intäkter), "kr, beläggning:", str(biograf.upptagnaplatser),
          "platser,", str(biograf.beläggning), "%")

    totalintäkter += biograf.intäkter
#print sats som skriver ut summan av alla biografernas intäkter
print("\nSumman av alla biografers intäkter:", totalintäkter, "kr")
