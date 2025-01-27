

from arrayQFile import ArrayQ       #Importerar de skapade modulerna från filerna arrayQFile och linkedQFile

from linkedQFile import LinkedQ

def main():
    #q = ArrayQ()       #Man kan välja mellan ArrayQ eller LinkedQ genom att kommentera bort den man inte vill köra.
    q = LinkedQ()
    card_order ='7 1 12 2 8 3 11 4 9 5 13 6 10' #'7 1 12 2 8 3 11 4 9 5 13 6 10' #input("What order should the cards be in? ")  #"3 1 5 2 4" 
    def las_in_rad():       # Läser in raden som en sträng, delar upp den, konverterar till tal och lägger till dem i listan card_list
        split_cards = card_order.split(' ')
        card_list = [int(x) for x in split_cards]
        for i in card_list:
            q.enqueue(i)

    las_in_rad()
    
    final_list = []
    def sort_cards():       # Algoritmen för trollkarlsprogrammet.
        global a            # Bränner ett kort, sparar dess värde och lägger det längst bak i kön.
        a=1                 # Kortet efter det sparas i egen variabel add_card och sparas i separat lista final_list.
        while a == 1:
            burn_card = q.dequeue()
            q.enqueue(burn_card)
            add_card = q.dequeue()
            final_list.append(add_card)

            if q.isEmpty() == 1:    # Processen fortsätter tills kön är tom. Därmed har alla korten sorterats enligt algoritmen.
                a = 0

    sort_cards()
    print(final_list)

main()

if __name__ == "__main__":
    '''
    # Trollkarlsprogrammet
    # De tretton korten ska ligga i följande ordning för att trolla fram alla tretton i rätt ordning
    # 7  1  Q12  2  8  3  J11  4  9  5  K13  6  10
    # Efter trolleriet blir de:
    # 1  2  3  4  5  6  7  8  9  10  J11  Q12  K13
    # '''