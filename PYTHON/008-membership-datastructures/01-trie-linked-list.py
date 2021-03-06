# ======================================================================================================
# Trie Data Structure
# ======================================================================================================
# - only membership(retrieval) test. Cannot be used for deletion
# - Can suggest alternatives unlike bloom filter's only True/False output
#       + But bloom filters are clearly Faster!
#       + Trie takes more space (ironic to T-S-Complexity) 
# - Implementation using linked list of linked lists. Same can be done using
#       + Sparse matrix
#       + Trie Tree  
#
# see: 006-trees/trie-tree.py for implementation

'''
class TrieNode:
    """
    DATA MEMBERS
        - val       : unit of the key
        - next      : node addr of succesive unit of the same key as `val`
        - follows   : node addr of succesive unit of difft. key
    """
    def __init__(self, unit, next=None, follows=None):
        self.unit       = unit
        self.next       = next
        self.follows    = follows
    # end def __init__

# end class Node


class Trie:
    """
    DATA MEMBERS
        - root      : like root of tree. denotes starting point

    METHODS
        - insert    : recursive. can be done iteratively too.
        - contains  : recursive  
    """

    def __init__(self, contents=[]):
        self.root = TrieNode('root', None, None)

        for __key in contents:
            self.insert(__key)

    def insert(self, key):
        """
        - recursively insert
        """        
        pass

    def __contains__(self, key):
        """
        - recursively check membership
        """
        pass

if __name__ == '__main__':
    lst = ['hello', 'no', 'hellen', 'heman']
    trie = Trie(lst)
    root = trie.root
    print(root)
'''