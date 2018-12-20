from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root == None

    def search(self, key): # returns True if key is in a node of the tree, else False
        if not self.is_empty():
            return self.search_helper(key, self.root)
        else:
            return False

    def search_helper(self, key, node):
        if node is None:
            return False

        elif node.key == key:
            return True
        # self.search_helper(key, node.left)
        # self.search_helper(key, node.right)
        if key < node.key:
            return self.search_helper(key, node.left)
        else:
            return self.search_helper(key, node.right)
    



    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST,
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        newNode = TreeNode(key, data)

        self.root = self.insert_helper(self.root, newNode)


    def insert_helper(self, node, newNode):
        if node is None:
            return newNode

        else:
            if newNode.key > node.key:
                node.right = self.insert_helper(node.right, newNode)
        
            if newNode.key < node.key:
                node.left = self.insert_helper(node.left, newNode)
                
            if node.key == newNode.key:
                node.data = newNode.data
            return node




    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        else:
            return self.find_min_helper(self.root)



    def find_min_helper(self,node):
        if node.left is None:
            return (node.key, node.data)
        return self.find_min_helper(node.left)


    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        return self.find_max_helper(self.root)

    def find_max_helper(self, node):
        if node.right is None:
            return (node.key, node.data)
        return self.find_max_helper(node.right)


    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        else:
            return self.tree_height_helper(self.root)


    def tree_height_helper(self, node):
        if node is None:
            return -1
        else:
            left = 1 + self.tree_height_helper(node.left)
            right = 1 + self.tree_height_helper(node.right)
        if left >= right:
            return left
        else:
            return right









    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        return self.inorder_list_helper(self.root, [])

    def inorder_list_helper(self, node, list):
        if node is not None:
            self.inorder_list_helper(node.left, list)
            list.append(node.key)
            self.inorder_list_helper(node.right, list)
            return list
        else:
            return []



    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        if self.is_empty():
            return []
        else:
         return self.preorder_list_helper(self.root, [])

    def preorder_list_helper(self, node, list):
        if node is not None:
            list.append(node.key)
            self.preorder_list_helper(node.left, list)
            self.preorder_list_helper(node.right, list)
        return list


    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this! Queue(25000)
        level_order_list = []
        if self.is_empty():
            return []
        q.enqueue(self.root)
        while not q.is_empty():
            node = q.dequeue()
            level_order_list.append(node.key)
            if node.left :
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        return level_order_list
