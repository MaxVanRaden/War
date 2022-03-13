import unittest
import war

class Tests(unittest.TestCase):
    def testGenDeck(self):
        testList = [0, 1]
        self.assertRaises(Exception, war.genDeck, testList )
    def testGenDeck2(self):
        testDeck = []
        war.genDeck(testDeck)
        self.assertEqual(len(testDeck), 52)

if __name__ == "__main__":
    unittest.main()