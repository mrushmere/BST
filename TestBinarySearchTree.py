import unittest
from BinarySearchTree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def test_GetTreeHeight0(self):
        root = BinarySearchTree([])
        self.assertTrue(root.GetTreeHeight(root.Root) == 0)

    def test_GetTreeHeight1(self):
        root = BinarySearchTree([26])
        self.assertTrue(root.GetTreeHeight(root.Root) == 1)

    def test_GetTreeHeight2(self):
        root = BinarySearchTree([26, 82, 16])
        self.assertTrue(root.GetTreeHeight(root.Root) == 2)
    
    def test_GetTreeHeight3(self):
        root = BinarySearchTree([26, 82, 16, 92, 33])
        self.assertTrue(root.GetTreeHeight(root.Root) == 3)

    def test_GetTreeHeight4(self):
        root = BinarySearchTree([12,11,90,82,7,9])
        self.assertTrue(root.GetTreeHeight(root.Root) == 4)

    def test_GetNodesForLevel1(self):
        root = BinarySearchTree([12,11,90,82,7,9])
        self.assertTrue(root.GetNodesForLevel(root.Root, 1, 1, []) == [12])
    
    def test_GetNodesForLevel2(self):
        root = BinarySearchTree([12,11,90,82,7,9])
        self.assertTrue(root.GetNodesForLevel(root.Root, 1, 2, []) == [11, 90])
    
    def test_GetNodesForLevel3(self):
        root = BinarySearchTree([12,11,90,82,7,9])
        self.assertTrue(root.GetNodesForLevel(root.Root, 1, 3, []) == [7, 82])

    def test_GetNodesForLevel4(self):
        root = BinarySearchTree([12,11,90,82,7,9])
        self.assertTrue(root.GetNodesForLevel(root.Root, 1, 4, []) == [9])

if __name__ == '__main__':
    unittest.main()