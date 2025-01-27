
# LinkedQ - en kö av noder (länkad lista)

# Nu ska du istället implementera kön som en länkad lista. 

# Då behövs två nya klasser: Node och LinkedQ. 
# Skriv in bägge klasserna i samma fil: linkedQFile.py. 
# Noderna i listan är objekt som vardera innehåller två publika attribut: 
# ett värde (value) och en referens till nästa objekt (next). 

# Själva LinkedQ-klassen ska ha två privata attribut: 
# first som håller reda på den första noden i kön och last som pekar ut den sista.
# Använd samma gränssnitt som i uppgift 1:

# enqueue(x)	stoppa in något sist
# x = dequeue()	plocka ut det som står först
# isEmpty()	kolla om kön är tom

# Det är extra knepigt att programmera enqueue(x) eftersom det blir två fall, 
# beroende på om kön är tom eller inte. 
# Rita upp bägge fallen (lådor med pilar) innan du skriver koden!



class queueOfWords:
    def __init__(self):
        self.__first = None         # LinkedQ-klassen har två privata attribut.
        self.__last = None          # first som håller reda på den första noden i kön och last som pekar ut den sista.

    def enqueue(self,x):
        ny = Node(x)
        if self.__first == None:    # Definierar nod "ny" och ser om kön är tom eller ej och lägger sedan till noden.
            self.__first = ny
            self.__last = ny
        else:
            self.__last.next = ny
            self.__last = ny


    def dequeue(self):  #Plockar bort första noden från kön och sparar nodens data i x.
        x = self.__first.data
        self.__first = self.__first.next
        return x


    def display(self):  #Möjliggör utskrift av kön genom iteration tills alla element sparats i en lista.
        if self.__first == None:
            return None
        else:
            elements = []
            current_node = self.__first
            elements.append(current_node.data)
            while current_node.next != None:
                current_node = current_node.next
                elements.append(current_node.data)
            return elements


    def remove(self,x):             # Raderar första upptäckta noden med värde x.
        if self.isEmpty() == 1:     # Kollar om kön är tom samt att programmet inte kraschar
            pass

        elif x == self.__first.data:
            self.__first = self.__first.next    # Om elementet som raderas är det första i kön sköts det av detta.
            return x

        elif self.__first != None:
            current_node = self.__first    # Itererar genom kön tills första noden med motsvarande angivet värde hittas och raderar den.

            while current_node.next != None:              # Fastnade på denna ett tag och frågade Stackoverflow om hjälp med en sak.
                last_node = current_node                  # Länken till Stackoverflow: https://bit.ly/3p11F8y
                current_node = current_node.next

                if current_node.data == x:
                    last_node.next = current_node.next
                    return
                


    def isEmpty(self):  #Kontrollerar om kön är tom genom att se ifall första noden pekar på None.
        if self.__first == None:
            return True
        else:
            return False

class Node:         #Klass med två publika attribut: ett värde (value) och en referens till nästa objekt (next).
   def __init__(self, x, next = None):
      self.data = x
      self.next = next

if __name__ == "__main__":  #If sats för att inte köra kod som eventuellt inte behövs i huvudprogrammet.
    
    p = LinkedQ()

    p.enqueue(1)
    p.enqueue(2)
    p.enqueue(3)
    p.enqueue(4)
    p.enqueue(5)

    print(p.display())

    p.remove(8)    #p.display()[len(p.display())//2])

    print(p.display())
