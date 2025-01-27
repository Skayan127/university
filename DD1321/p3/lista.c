#include "lista.h"
#include <stdio.h>
#include <stdlib.h>
// Tog hjälp av Caspar Westerbergs övning om länkade listor i C.

void insertnod(Nod ** root, Nod * laggas_till) {
    if (*root == NULL){     //Ifall listan är tom, fyll listan med noden.
        *root = laggas_till;
    }
    else {                  // Om listan inte är tom.
        Nod * gammalForst = *root;
        *root = laggas_till;
        laggas_till->next = gammalForst;
        gammalForst->prev = laggas_till;
    }
}



void removenod(Nod ** root, Nod * att_raderas){
    if (*root !=NULL){
        Nod * temp = *root;

        if (att_raderas->next==NULL && att_raderas->prev==NULL) {   //Endast ett element i listan
            temp=NULL;
            free(att_raderas);
        }
        else if (att_raderas->prev==NULL) { //Första element i listan
            *root = temp->next;
            att_raderas->next->prev=NULL;
            free(att_raderas);
        }
        else if (att_raderas->next==NULL) { //Sista element i listan
            att_raderas->prev->next=NULL;
            free(att_raderas);
        }
        else { //Godtycklig plats i mitten av listan
            att_raderas->next->prev=att_raderas->prev;
            att_raderas->prev->next=att_raderas->next;
            free(att_raderas);
        }
    }
}


void printlist(Nod * node){
    if (node!=NULL) {       // Om noden inte är tom, om nodens nextpekare inte är NULL printa noden. Gör processen rekursivt.
        
        if (node->next != NULL){
            printnod(node);
            printlist(node->next);
        }
        else {
            printnod(node); //Om nodens nextpekare är NULL, printa noden.
        }
    }
    else {
        printf("List is empty!");
    }
}

void printnod(Nod * node){
    if (node == NULL){      // Om noden är tom, skriv ut "NULL", annars skriv ut telefonnummer samt namn.
        printf("NULL\n");
    }
    else {
        printf("( tel: %d, name: %s )\n",node->tel,node->name);
    }
}

Nod * search(Nod * node, int tel){
    if (node!=NULL) {       // om noden inte är tom, om angivna tel är samma som nodens tel, returnera nod.

        if (node ->tel==tel){
            return node;
        }
        else if (node->next==NULL){ //Om man nått slutet av listan, returnera NULL.
            return NULL;
        }
        else {
            return search(node->next,tel);  //Leta igenom nästa nod.
        }
    }
    else {
        return NULL;
    }
}
