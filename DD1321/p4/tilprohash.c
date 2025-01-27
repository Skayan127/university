

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