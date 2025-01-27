#ifndef LISTA_H
#define LISTA_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// struct nod {
//     char name[30];
//     int tel;
//     struct nod * next;
//     struct nod * prev;
// };
// typedef struct nod Nod;

struct nod {
    char key[512];
    char value[512];
    struct nod * next;
    struct nod * prev;
};
typedef struct nod Nod;

void insertnod(Nod ** list, Nod * tobeadded);
void removenod(Nod ** list, Nod * toberemoved);
void printnod(Nod * node);
void printlist(Nod * node);

Nod * search(Nod * node, char * key);

#endif /* LISTA_H */