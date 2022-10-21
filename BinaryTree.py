class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return f'{self.data}'

# root = Node(15)
# root.left = Node(10)
# root.right = Node(16)
# print(f'root: {root}, left: {root.left}, right: {root.right}')

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
            Insert(data: any) -> None:\n 
            creates a new Node from the data passed in and adds it to the tree
            If the data is already in the tree, does not insert it again
        '''
        new_node = Node(data)
        # if this is the first node, make new node the root
        if not self.root:
            self.root = new_node
            return
        
        # loop over the tree starting at the root
        # keep track of the current node
        current_node = self.root
        while current_node:
            # if the new_node is smaller than the current node
            if new_node.data < current_node.data:
                # ...if there is no left
                if not current_node.left:
                    # insert the node to the left of current node
                    current_node.left = new_node
                    return
                # if there is a left, we want to keep iterating
                else:
                    current_node = current_node.left
            # if the new_node is greater than the current node
            elif new_node.data > current_node.data:
                # if there is no right
                if not current_node.right:
                    # insert new node
                    current_node.right = new_node
                    return
                # if there is a right, continue iterating
                else:
                    current_node = current_node.right
            # if the new_node is a duplicate of the current node
            else:
                # stop iterating
                return

    
    def dfs(self, val):
        '''
            dfs(val: any) -> value or bool:\n 
            Performs depth first search
            Search the Tree for a node with the given value
            If the node exists, return it
            If the node doesn't exist, return false
        '''
        
        # if there is no root return early
        if not self.root:
            return False

        # loop through the tree iteratively
        current_node = self.root
        while current_node:
            # the value we are searching for is smaller than current node
            if val < current_node.data:
                current_node = current_node.left
            # the value is greater than current node
            elif val > current_node.data:
                current_node = current_node.right
            # if the value neither -- its a match!
            else:
                return current_node
        
        # if we make it here, nothing was found
        return False

    def bfs(self, val):
        '''
            bfs(val: any) -> value or bool:\n
            Performs breadth first search
            Search the Tree for a node with the given value
            If the node exists, return it
            If the node doesn't exist, return false
        '''
        pass

    # print out all the nodes
    def print(self, node=None):
        '''
            print() -> None:\n
            prints out all values recursively (in a depth first search fashion)
            default start is at root node
        '''
        # if this is the first invokation
        if not node:
            node = self.root

        # if this node has a left or right, we will recursively print
        
        # dfs
        print(node)

        if node.left:
            self.print(node.left)
        # print(node) # in order traversal
        if node.right:
            self.print(node.right)

my_tree = BinaryTree()
my_tree.insert(15)
my_tree.insert(10)
my_tree.insert(16)
my_tree.insert(19)
my_tree.insert(22)
my_tree.insert(17)
my_tree.insert(6)
my_tree.insert(9)
my_tree.insert(2)

my_tree.print()
# print(f'root\'s left: {my_tree.root.left}, root\'s right: {my_tree.root.right}')