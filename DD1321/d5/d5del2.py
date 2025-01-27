
# En del av denna kod tagen från labbspecen.
# Rayan Alnakar, rayana@kth.se
# Project d5, DD1321 "Tillämpad programmering och datalogi"
# 2021-02-22

import unittest

from d5del1 import *

class BintreeTest(unittest.TestCase):

    def testInsert(self):
         """ Testar Subj och Pred """
         b = Bintree()
         b.store("adam", 123)
         self.assertEqual(b.root.nyckel, "adam")
         self.assertEqual(b.root.data, 123)


    def testInsertMore(self):                                            #  banan
         c = Bintree()                                                   #       \
         c.store("banan", "frukt")                                       #       gurka
         c.store("gurka", "grönsak")                                     #      /
         c.store("bil", "fordon")                                        #     bil
         self.assertEqual(c.root.hoger_barn.nyckel, "gurka")
         self.assertEqual(c.root.hoger_barn.vanster_barn.nyckel, "bil")

    def testSearch(self):
         b = Bintree()
         #b.store("eva","människa")
         with self.assertRaises(KeyError): 
             b.search("eva")
    
    def testMore(self):
         d = Bintree()
         d.store("penna", "kontor")
         d.store("mus", "elektronik")
         d.store("jord", "himmel")
         self.assertEqual("jord" in d, True)
         self.assertEqual("mus" in d, True)
         self.assertEqual("penna" in d, True)


if __name__ == '__main__':
    unittest.main()