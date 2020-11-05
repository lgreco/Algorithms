#
#      A simple Node class with an initial constructor, an insertion
#      method, a listing method, and a  membership test. Insertions,
#      listings, and membership  tests  are conducted  using  Binary
#      Search Tree rules.  Therefore, objects instantiated from this
#      class behave like BSTs.                      
#
#      This class can be used as a Jupyter Notebook  cell, or it may
#      be saved in a .py file and imported as a module.
#
#                                                     leo@cs.luc.edu 
#                                                   COMP 363 002 F20
#
class Node:

    #
    # Initial constructor for first node in the structure.
    # instantiates an object with the given content and no children.
    # Subsequent nodes can be added with the insert method, defined
    # below. 
    #
    # Usage:
    #   myTreeName = Node(content)
    #
    def __init__(self, content):
        self.left = None
        self.right = None
        self.parent = None
        self.content = content

    # 
    # Method to insert data into the tree; content is placed
    # to the left or right of parent node, based on comparisons
    # (smaller to the left, larger to the right.) The method
    # traverses the tree recursively until an empty spot is found.
    # 
    # Usage:
    #   myTreeName.insert(newValue)
    #
    def insert(self, newValue):

        if self.content is None:                # Current node is empty!
            self.content = newValue             #   place new value here.
        else:                                   # current node not empty
            if newValue < self.content:         #   new value less than current node value
                if self.left is None:           #   if left child null
                    self.left = Node(newValue)  #     place new value here
                else:                           #   if left child not null
                    self.left.insert(newValue)  #     recurse to the left
            elif newValue > self.content:       #   new value more than current node value
                if self.right is None:          #   if right child null
                    self.right = Node(newValue) #     place new value here
                else:                           #   if right child not null
                    self.right.insert(newValue) #     recurse to the right


    #
    # In-order tree traversal lists the contents of the tree in
    # ascending order. The recursive algorith can be applied on
    # any node (though, usually we start at the root of the tree)
    # and prints all the contents below, including the initial node,
    # as follows:
    #      inOrderTraversal(node)
    #        inOrderTraversal(node.left)
    #        print(node.contents)
    #        inOrderTraversal(node.right)
    # 
    # Usage:
    #   myTreeName.inOrderTravesal()
    #
    def inOrderTraversal(self):
        if self.left:                     # if left child not null
            self.left.inOrderTraversal()  #    process it
        print(self.content)               # process the node
        if self.right:                    # if right child not null
            self.right.inOrderTraversal() #    process it

    #
    # method to test membership in a tree. It can be applied on
    # any node (though, usually we start at the root) and returns
    # TRUE is the argumement searchFor is stored in the tree,
    # FALSE, otherwise.
    #
    # Usage:
    #   myTreeName.contains(searchFor)
    #
    def contains(self, searchFor):
        if searchFor < self.content:
            if self.left is None:
                return False
            return self.left.contains(searchFor)
        elif searchFor > self.content:
            if self.right is None:
                return False
            return self.right.contains(searchFor)
        else:
            return True

    # Max
    def maxNode(self):
        current = self
        if current.right is not None:
            return current.right.maxNode()
        return current.content

    #Min
    def minNode(self):
        current = self
        if current.left is not None:
            return current.left.minNode()
        return current.content


#predecessor
def predecessorNode(currentNode, previous, key):
    if currentNode is None:
        return None

    # if .left not empty max(.left) but first find node of interest
    if currentNode.content == key:
        if currentNode.left is not None:
            return currentNode.left.maxNode()
    elif key < currentNode.content:
        return predecessorNode(currentNode.left, previous, key)
    else:
        previous = currentNode
        return predecessorNode(currentNode.right, previous, key)
    return previous


#
# DRIVING CODE
#
# Use GitHub:dwyl's english words project to populate a BST
# with words, as if it was a dictionary.
#     https://github.com/dwyl/english-words
# Rather than opening a URL stream to the dwyl's file (and dealing
# with network issues) I have made a local copy here.

words = open('../CommonDataFiles/words_alpha.txt', 'r')
words = words.read()
words = words.split('\n')
number_of_words = len(words)
number_of_words_100th = int(number_of_words/100)

# at this point, words is a list with 370,103 items, 
# specifically english words in alphabetical order.
# Let's scramble them.
import random
words = sorted(words, key = lambda  x:random.random())
#print(words)

# create a tree using the first word in the list
first_word = words[0]
words.remove(words[0])
print("The tree will be build on root value of", first_word)

root = Node(first_word)

# add words to tree
word_counter = 0
for word in words:
    root.insert(word)
    word_counter = word_counter + 1
    if (word_counter%number_of_words_100th == 0):
        print(".", end="")

# Try in-Order traversal
#root.inOrderTraversal()

print(root.maxNode())

predecessor =  (predecessorNode(root, None, 'zyzzyvas'))


if predecessor is not None:
    print(predecessor.content)
else:
    print("Nothing found")