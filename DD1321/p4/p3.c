
#include "lista.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Nod * makeNode(int tel, char * name) {
//     Nod * newNode = malloc(sizeof(Nod));
//     strcpy(newNode->name,name);
//     newNode->tel = tel;
//     newNode->next = NULL;
//     newNode->prev = NULL;
//     return newNode;
// }




extern const int HASHVEKSIZE;


Nod * makeNode(char * key, char * value) {
    Nod * newNode = malloc(sizeof(Nod));
    strcpy(newNode->key,key);
    strcpy(newNode->value,value);
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

void main() {

    Nod * root = NULL;

    //Nod ** myhashvek = malloc(sizeof(Nod *) * HASHVEKSIZE);

    // Nod * nyNod = makeNode(123,"Rayan");
    // Nod * nyNod2 = makeNode(456,"Kris");
    // Nod * nyNod3 = makeNode(789,"Mic");
    // Nod * nyNod4 = makeNode(101112,"hello");

    Nod * nyNod = makeNode("1998","Rayan");
    Nod * nyNod2 = makeNode("1999","Kris");
    Nod * nyNod3 = makeNode("2000","Mike");
    Nod * nyNod4 = makeNode("2001","John");
    
    printlist(root);
    insertnod(&root,nyNod);
    insertnod(&root,nyNod2);
    insertnod(&root,nyNod3);
    insertnod(&root,nyNod4);

    printf("\n");

    printf("Nedan söker jag efter 2000 \n");
    printnod(search(root,"2000"));
    
    printf("\n");
    printf("Nedan printar jag listan: \n");
    printlist(root);
    
    printf("\n");
    
    
    // removenod(&root,nyNod2);
    // removenod(&root,nyNod4);
    // removenod(&root,nyNod);
    // removenod(&root,nyNod3);
}