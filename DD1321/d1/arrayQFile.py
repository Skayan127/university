
# Frågade Stackoverflow om hjälp för att förstå i detalj hur klasser fungerar i vissa fall.
# Länk till Stackoverflow: https://bit.ly/3mtgPlc

from array import array # Importerar arraymodulen

class ArrayQ:           # Skapar en klass ArrayQ med privata attributen queue som en array.    
    def __init__(self):
        self.__queue=array('Q')

    def enqueue(self, value):   #Metod för att lägga till element sist i array mha inbygga append().
        return self.__queue.append(value)

    def dequeue(self):          #Metod för att radera första elementet i array mha inbygga pop(0)
        return self.__queue.pop(0)

    def isEmpty(self):          #Kontrollerar om array är tom eller ej.
        #a=1
        if not self.__queue:
            return True
        else:
            return False
