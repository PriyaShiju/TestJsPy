import unittest
from sortedfrozenset import sortedfrozenset

class Test_sortedFrozen(unittest.TestCase):
    
    def test_classempty(self):
        s= sortedfrozenset([])
        
    def test_classnonempty(self):
        s= sortedfrozenset([7,3,2,1])
    
    def test_classiterator(self):
        items = [3,4,5,6]
        iterator = iter(items)
        s= sortedfrozenset(iterator)
         
    def test_noarguments(self):
        s= sortedfrozenset()

class Test_ContainerProtocol(unittest.TestCase):
    def setUp(self):
        self.s = sortedfrozenset([4,5,6,7,9])
        
    def test_containpositive(self):
        self.assertTrue(6 in self.s)
        
    def test_containnegative(self):
        self.assertFalse(-2 in self.s)
        
    
        
        
    
    
if __name__=="__main__":
    unittest.main()