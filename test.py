import unittest
import war

class Tests(unittest.TestCase):

    def testGenDeck(self): # test non-empty list passed in 
        testDeck = []
        testDeck = war.genDeck(testDeck)
        self.assertRaises(Exception, war.genDeck, testDeck)
    def testGenDeck2(self): # test size of deck correct
        testDeck = []
        testDeck = war.genDeck(testDeck)
        self.assertEqual(len(testDeck), 52)
    
    def testSplitDeck(self): # test empty deck
        self.assertRaises(Exception, war.splitDeck)
    def testSplitDeck2(self): # test odd deck
        testDeck = []
        testDeck = war.genDeck(testDeck)
        testDeck.pop()
        self.assertRaises(Exception, war.splitDeck, testDeck)
    def testSplitDeck3(self): # test valid deck, nonempty player 1 deck
        testDeck = []
        testDeckP1 = []
        testDeck = war.genDeck(testDeck)
        testDeckP1 = war.genDeck(testDeckP1)
        testDeckP2 = []
        self.assertRaises(Exception, war.splitDeck, testDeck, testDeckP1, testDeckP2)
    
    def testPlayCards(self): # test playing 0 cards 
        testDeck = []
        testWarDeck = []
        testDeck = war.genDeck(testDeck)
        testWarDeck = war.genDeck(testWarDeck)
        self.assertRaises(Exception, war.playCards, testDeck, testWarDeck, num=0)
    
    def testGetCards(self): # Test receiving empty decks
        self.assertRaises(Exception, war.getCards)
    
    def testBattle(self): # test recieving empty decks
        self.assertRaises(Exception, war.battle)

    

    
    

if __name__ == "__main__":
    unittest.main()