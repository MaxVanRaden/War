import unittest
import war

class Tests(unittest.TestCase):
    def testGenDeck(self): # test non-empty list passed in 
        testList = [0, 1]
        self.assertRaises(Exception, war.genDeck, testList )
    def testGenDeck2(self): # test size of deck correct
        testDeck = []
        war.genDeck(testDeck)
        self.assertEqual(len(testDeck), 52)
    def testSplitDeck(self): # test empty deck
        self.assertRaises(Exception, war.splitDeck)
    def testSplitDeck2(self): # test odd deck
        testDeck = [1,2,3]
        self.assertRaises(Exception, war.splitDeck, testDeck)
    def testSplitDeck3(self): # test valid deck, nonempty player 1 deck
        testDeck = [1,2]
        testDeckP1 = [1]
        testDeckP2 = []
        self.assertRaises(Exception, war.splitDeck)
    
    

if __name__ == "__main__":
    unittest.main()