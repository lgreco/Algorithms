from binaryTree import Node
from letterFrequencies import english_alphabet_frequencies
import queue

our_priority_queue = queue.PriorityQueue()

for letter in english_alphabet_frequencies:
    our_priority_queue.put(letter)

while our_priority_queue.qsize()>1:
    left  = our_priority_queue.get()
    right = our_priority_queue.get()
    new_node = Node(left, right)
    new_tuple = (left[0] + right[0], new_node)
    our_priority_queue.put((new_tuple)) # LI note: your new_tuple needed to
                                        # be in parentheses.


# Traverse through tree producing Huffman codes for each letter

def tree_traversal(tree_root, prefix="", code={}):
    if isinstance(tree_root[1].left[1], Node):
        tree_traversal(tree_root[1].left, prefix + "0", code)
    else:
        code[tree_root[1].left[1]]= prefix + "0"
    if isinstance(tree_root[1].right[1], Node):
        tree_traversal(tree_root[1].right, prefix + "1", code)
    else:
        code[tree_root[1].right[1]]= prefix + "1"
    return(code)

huffman = tree_traversal(our_priority_queue.get())
for symbol in sorted(english_alphabet_frequencies, reverse=True):
    print(symbol[1], symbol[0], huffman[symbol[1]])