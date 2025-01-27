#include <stdio.h>
#include <stdlib.h>
#include <string.h>



struct artist {
  char artistid[20];
  char artistname[400];
  char songtitle[300];
  double length;
  int year;
};

typedef struct artist Artist;


//  Läser artister från filename och lägger dem i artistarray
//  returnerar antalet inlästa artister
int readartists(char * filename, Artist * artistarray) {
  char linebuffer[425];

  FILE * fil = fopen(filename, "r");

  int currentartist = 0;

  while (fgets (linebuffer, 425, fil) != NULL) {

    Artist * artist = artistarray + currentartist;

    int i = 0;
    int j = 0;
    // kolumner är TAB-separerade 
    while (linebuffer[i] != '\t')             
      i++;

    strncpy(artist -> artistid, linebuffer, j);

    i += 1;
    j = i;
    while (linebuffer[i] != '\t') 
      i++;

    strncpy(artist -> artistname, linebuffer + j, i - j);

    i += 1;
    j = i;
    while (linebuffer[i] != '\t') 
      i++;

    strncpy(artist -> songtitle, linebuffer + j, i - j);

    i += 1;
    // atof - array to float
    artist -> length = atof(linebuffer + i);  

    while (linebuffer[i] != '\t') 
      i++;

    i += 1;
    // atoi - array to integer 
    artist -> year = atoi(linebuffer + i);    

    currentartist += 1;
  }

  fclose(fil);
  return currentartist;
}

extern const int HASHVEKSIZE;

// int main() {
//   Artist * artister = malloc(sizeof(Artist) * 32); // Längden av listan.

//   // calloc är ett alternativ till malloc som initierar vektorn till noll
//   //   Artist * artister = calloc(1000000, sizeof(Artist));

//   int antalartister = readartists("sang-artist-data.txt", artister);


//   Nod ** myhashvek = malloc(sizeof(Nod *) * HASHVEKSIZE);
//   init(myhashvek);

//   int i = 0;
//   for (i = 0; i < antalartister; i += 1) {

//     put(myhashvek, artister[i].artistname, artister[i].songtitle);

//   }

// //   int j;
// //   for (j = 0; j < 32; j++) {
// //       printf("%s\n",myhashvek[j]->key);
// //   }
// //   return 0;


//   char * s = get(myhashvek, "Faster Pussy cat");
//   char * d = get(myhashvek, "Lennart");
//   char * f = get(myhashvek, "Dying Fetus");
//   printf("Key = Faster Pussy cat, Value = %s\n", s);
//   printf("Key = Lennart, Value = %s\n", d);
//   printf("Key = Dying Fetus, Value = %s\n", f);
//   del_all(myhashvek,"Dying Fetus","Ethos of Coercion");
//   printf("Key = Dying Fetus, Value = %s\n", f);
//     // printf("artist: %s\n  songtitle: %s\n  length: %f\n",
//     //    artister[i].artistname, artister[i].songtitle, artister[i].length);
  

//   free(artister);
//   return 0;
// }