#include "hashfunc.h"
#include "hashfunc.c"
#include "lista.c"
#include "readartists.c"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// ...

extern const int HASHVEKSIZE;
// ...

int main()
{
    Nod **myhashvek = malloc(sizeof(Nod *) * HASHVEKSIZE);
    init(myhashvek);

    Artist *artister = malloc(sizeof(Artist) * 1000000); // Längden av listan.

    // calloc är ett alternativ till malloc som initierar vektorn till noll
    //   Artist * artister = calloc(1000000, sizeof(Artist));

    int antalartister = readartists("sang-artist-data.txt", artister);

    for (int i = 0; i < antalartister; i += 1){
        // if (strlen(artister[i].songtitle) < 1 ) {
        //     printf("i=%d artist = %s",i,artister[i].artistname);
        // }
        put(myhashvek, artister[i].artistname, artister[i].songtitle);
        
    }

    // put(myhashvek, "Adam", "123321");
    // put(myhashvek, "Adam", "87");
    // put(myhashvek, "Bertil", "45");
    // put(myhashvek, "JOohan", "89");
    char *s = get(myhashvek, "Ministry");
    char *d = get(myhashvek, "Lennart");
    char *f = get(myhashvek, "Benny Green");
    printf("Ministry -> value = %s\n", s);
    printf("Lennart -> value = %s\n", d);
    printf("Benny Green -> value = %s\n", f);

    del_all(myhashvek);
    free(artister);
    free(myhashvek);
}