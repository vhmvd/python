"""
            [5]
           /   \
         [1]   [6]
        /   \     \
      [0]   [2]   [8]
                  /  \
                [7]  [9]

pre-order traversal : 5,1,0,2,6,8,7,9
in-order traversal  : 0,1,2,5,6,7,8,9
post-order traversal: 0,2,1,7,9,8,6,5  
"""


class Node(object):
      def __init__(self, value = None):
          """
          basic structure of a binary tree is a single node.
          a node can hold a node value and it
          lays out a connection for other nodes
          to be placed either left or right during the next recursive
          pass of the binary tree construction process. 
          initially the node is empty (i.e. value = None) but it 
          posesses all features to become a tree. 
          all values that are used during the construction of the 
          binary tree are contained in a list L.
          the first element in list L, L[0], becomes the value of the
          root node. the rest of the nodes are then added to it using the
          insert_node() method. see construct_binary_tree(L) method.
          """
          self.value = value
          self.left = None
          self.right= None

      def insert_node(self, new_value):
          """
          this method inserts a new node into the object
          recursively, using the standard convention:
          values equal or smaller than the root go to the left,
          the rest goes to the right.
          """
          if new_value <= self.value:
             if self.left == None:
                self.left = Node(new_value)
             else:
                self.left.insert_node(new_value)
          else: #case when new_value > self.value:
               if self.right == None:
                  self.right = Node(new_value)
               else:
                  self.right.insert_node(new_value)

      def construct_binary_tree(self, L):
          self.value = L[0]
          for e in L[1:]:
              self.insert_node(e)

      def preorder_traversal(self):
          print(self.value)
          if self.left != None: #alternatively, if self.left: 
             self.left.preorder_traversal()  #go a level deeper
          if self.right != None: #if node on right is not None!
             self.right.preorder_traversal() #go a level deeper

      def inorder_traversal(self):
          if self.left != None: 
             self.left.inorder_traversal()  #go a level deeper
          print(self.value)
          if self.right != None:
             self.right.inorder_traversal() #go a level deeper

      def postorder_traversal(self):
          if self.left != None: 
             self.left.postorder_traversal()  #go a level deeper
          if self.right != None: 
             self.right.postorder_traversal() #go a level deeper
          print(self.value)

      def count_nodes(self, L=[]):
          L.append(self.value)
          if self.left != None: #alternatively, if self.left: 
             self.left.count_nodes()  #go a level deeper
          if self.right != None: #if node on right is not None!
             self.right.count_nodes() #go a level deeper
          return len(L)

      def find_leaf_nodes(self, L = []):
          """
          this method finds all leaf nodes. These are the 
          nodes at the bottom of the tree and there are 
          no nodes below them. we will place the values
          of the nodes in a list L, initially empty.
          """
          if self.left == None and self.right == None:
             L.append(self.value)
          else:
             if self.left != None:
                self.left.find_leaf_nodes()
             if self.right != None:
                self.right.find_leaf_nodes()
          return L

      def count_leaf_nodes(self):
          cnt = 0
          if self.left == None and self.right == None:
             return 1
          if self.left != None:
             cnt += self.left.count_leaf_nodes()
          if self.right != None:
             cnt += self.right.count_leaf_nodes()
          return cnt      

      def alternative_count_leaf_nodes(self, L = []):
          if self.left == None and self.right == None:
             L.append(self.value)
          else:
             if self.left != None:
                self.left.alternative_count_leaf_nodes()
             if self.right != None:
                self.right.alternative_count_leaf_nodes()
          return len(L)    
     
def main():
    T = Node() # intilly, the tree is empty
    T.construct_binary_tree([4,3,7,6,5,2,4,1,0,7])
    print("preorder")
    T.preorder_traversal()
    print("inorder")
    T.inorder_traversal()
    print("postorder")
    T.postorder_traversal()

    print("node count")
    print(T.count_nodes())
    
    print("leaf nodes")
    print(T.find_leaf_nodes())

    print("leaf node count")
    print(T.count_leaf_nodes())

    print("alternative leaf node count")
    print(T.alternative_count_leaf_nodes())
    
main()
