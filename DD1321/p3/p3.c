
#include "lista.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


Nod * makeNode(int tel, char * name) {
    Nod * newNode = malloc(sizeof(Nod));
    strcpy(newNode->name,name);
    newNode->tel = tel;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

void main() {

    Nod * root = NULL;


    Nod * nyNod = makeNode(123,"Rayan");
    Nod * nyNod2 = makeNode(456,"Kris");
    Nod * nyNod3 = makeNode(789,"Mic");
    Nod * nyNod4 = makeNode(101112,"hello");
    
    printlist(root);
    insertnod(&root,nyNod);
    insertnod(&root,nyNod2);
    insertnod(&root,nyNod3);
    insertnod(&root,nyNod4);

    printf("\n");
    
    printnod(search(root,456));
    
    printf("\n");
    
    printlist(root);
    
    printf("\n");
    
    
    removenod(&root,nyNod2);
    removenod(&root,nyNod4);
    removenod(&root,nyNod);
    removenod(&root,nyNod3);
}