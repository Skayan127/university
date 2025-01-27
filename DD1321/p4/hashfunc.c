#include "hashfunc.h"
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>


#ifndef hashfunc_c
#define hashfunc_c

Nod * makeNode(char * key, char * value) {
    Nod * newNode = malloc(sizeof(Nod));
    strcpy(newNode->key,key);
    strcpy(newNode->value,value);
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}


// Nod ** myhashvek = malloc(sizeof(Nod *) * HASHVEKSIZE);
// const int HASHVEKSIZE = 32;
const int HASHVEKSIZE = 1048576;    // 2 upphöjt till 20 ungefär 1 miljon
//const int HASHVEKSIZE = 2097152     // 2 upphöjt till 21
//const int HASHVEKSIZE = 4194304     // 2 upphöjt till 22

uint32_t tilpro_hash(const char * s) {
  uint32_t hash = 0;
  size_t i = 0;
  while (s[i] != '\0') {
    hash += s[i++];
    hash += hash << 10;
    hash ^= hash >> 6;
  }
  hash += hash << 3;
  hash ^= hash >> 11;
  hash += hash << 13;

  hash = hash & ( HASHVEKSIZE - 1 );
  return hash;
}


void put(Nod ** hashtable, char * key, char * value) {
    int slot = tilpro_hash(key);

    if (hashtable[slot] == NULL){
        insertnod(&hashtable[slot],makeNode(key,value));

    }
    else  {
        Nod * foundnode = search(hashtable[slot],key);
        if (foundnode == NULL) {
            insertnod(&hashtable[slot],makeNode(key,value));

        }
        else {
            strcpy(foundnode->value,value);
        }
    }
}


char * get(Nod ** hashtable, char * key) {
    // TODO
    int slot = tilpro_hash(key);

    if (hashtable[slot] == NULL){
        return NULL;
    }
    else {
        Nod * foundnode = search(hashtable[slot],key);
        if (foundnode != NULL) {
            // printf("%s\n",foundnode->value);
            return foundnode->value;
        }
        else {
            return 0;
        }
        
    }
}

void del_all(Nod ** hashtable){
    for (int i = 0; i < HASHVEKSIZE; i++) {
        while (hashtable[i] != NULL){
            removenod(&hashtable[i],hashtable[i]);
        }
    }
}
// del_all, gå igenom arrayen och remova noder, annars gå vidare.


void init(Nod ** vek) {

    for (int i=0; i < HASHVEKSIZE; i++) {
        vek[i] = NULL;
    }
}

#endif /* hashfunc.c */