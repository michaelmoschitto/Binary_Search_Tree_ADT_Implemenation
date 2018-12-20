import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        # bst.insert(10, 'stuff')
        self.assertFalse(bst.search(2))
        self.assertEqual(bst.find_min(), None)
        self.assertEqual(bst.find_max(), None)
        # self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        bst.insert(2, 'brother')
        bst.insert(3, 'sister')
        self.assertFalse(bst.search(13))
        self.assertEqual(bst.find_min(), (2,'brother'))
        self.assertEqual(bst.find_max(), (10, 'other'))

    def test_insert_and_search(self):
        bst = BinarySearchTree()
        bst.root = None
        self.assertEqual(bst.search(2), False)
        self.create_standard_list(bst)
        self.assertEqual(bst.root.data, '10')
        bst.insert(10, "testSameKey")
        self.assertEqual(bst.tree_height(), 3)
        self.assertEqual(bst.root.data, 'testSameKey')
        self.assertEqual(bst.root.left.left.data, '4')
        self.assertEqual(bst.root.left.right.data, '6')
        self.assertEqual(bst.root.left.data, '5')
        self.assertEqual(bst.root.right.right.data, '16')
        self.assertEqual(bst.root.right.left.data, '14')
        self.assertEqual(bst.root.right.data, '15')
        self.assertTrue(bst.search(4))

    def test_tree_height(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        self.create_standard_list(bst)
        self.assertEqual(bst.tree_height(), 3)
        bst.insert(18, '18')
        bst.insert(19, '19')
        self.assertEqual(bst.tree_height(), 5)
        bst.insert(3, '3')
        bst.insert(2, '2')
        bst.insert(1, '1')
        bst.insert(0, '0')
        print(bst.inorder_list())
        self.assertEqual(bst.tree_height(), 6)



    def test_find_min_max(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_min(), None)
        self.assertEqual(bst.find_max(), None)
        self.create_standard_list(bst)
        self.assertEqual(bst.find_max(), (17, '17'))
        self.assertEqual(bst.find_min(), (4, '4'))

    def test_inorder_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.inorder_list(), [])
        self.create_standard_list(bst)
        self.assertEqual(bst.inorder_list(), [4, 5, 6, 10, 14, 15, 16, 17])

    def test_preorder_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), [])
        self.create_standard_list(bst)
        self.assertEqual(bst.preorder_list(), [10, 5, 4, 6, 15, 14, 16, 17])

    def test_level_order_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.level_order_list(), [])
        self.create_standard_list(bst)
        self.assertEqual(bst.level_order_list(), [10, 5, 15, 4, 6, 14, 16, 17])




    def create_standard_list(self,bst):
        bst.insert(10, '10')
        bst.insert(5, '5')
        bst.insert(6, '6')
        bst.insert(4, '4')
        bst.insert(15, '15')
        bst.insert(14, '14')
        bst.insert(16, '16')
        bst.insert(17, '17')









        # self.assertEqual(bst.find_max(), (10, 'other'))
        # self.assertEqual(bst.tree_height(), 0)
        # self.assertEqual(bst.inorder_list(), [10])
        # self.assertEqual(bst.preorder_list(), [10])
        # self.assertEqual(bst.level_order_list(), [10])

if __name__ == '__main__':
    unittest.main()
