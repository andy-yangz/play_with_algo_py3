import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from helpers import Node

def print_tree(tree):
    nodes = [tree.root]
    while True:
        next_layer = []
        while nodes:
            node = nodes.pop(0)
            if not node:
                print("_"+" ", end='')
                next_layer.extend([None, None])
            else:
                print(str(node.key)+":"+str(node.count)+":" + str(node.dups) + " ", end='')
                next_layer.extend([node.left, node.right])
        print()
        if not any(next_layer): break
        nodes = next_layer

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count
    
    def __insert_recur(self, node, key, value):
        if node is None: 
            self.count += 1
            return Node(key, value)
        if node.key == key:
            node.value = value
            node.dups += 1
        elif node.key > key:
            node.left = self.__insert_recur(node.left, key, value)
            node.count += 1
        else:
            node.right = self.__insert_recur(node.right, key, value)
            node.count += 1
        return node

    def __insert_iter(self, node, key, value):
        if not node:
            return Node(key, value)
        root = node
        while True:
            if node.key == key:
                node.value = value
                break
            elif node.key > key:
                if not node.left:
                    node.left = Node(key, value)
                    break
                node = node.left
            else:
                if not node.right:
                    node.right = Node(key, value)
                    break
                node = node.right
        return root
    
    def __contain(self, node, key):
        if not node:
            return False

        if node.key == key:
            return True
        elif node.key > key:
            return self.__contain(node.left, key)
        else:
            return self.__contain(node.right, key)

    def __search(self, node, key, get_node=False):
        if not node:
            return None
        if node.key == key:
            return node if get_node else node.value
        elif node.key > key:
            return self.__search(node.left, key, get_node=get_node)
        else:
            return self.__search(node.right, key, get_node=get_node)
    
    def __preoder(self, node):
        if node:
            print(node.key)
            self.__preoder(node.left)
            self.__preoder(node.right)
    
    def __inoder(self, node):
        if node:
            self.__inoder(node.left)
            print(node.key)
            self.__inoder(node.right)

    def __postorder(self, node):
        if node:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(node.key)
    
    def __minimum(self, node):
        if not node.left: return node
        return self.__minimum(node.left)
    
    def __maximum(self, node):
        if not node.right: return node
        return self.__maximum(node.right)

    def __remove_min(self, node):
        if not node.left:
            if node.dups > 1:
                node.dups -= 1
                return node
            else:
                right = node.right
                self.count -= 1
                return right

        node.left = self.__remove_min(node.left)
        node.count -= 1
        return node
    
    def __remove_max(self, node):
        if not node.right:
            if node.dups > 1:
                node.dups -= 1
                return node
            else:
                left = node.left
                self.count -= 1
                return left

        node.right = self.__remove_max(node.right)
        node.count -= 1
        return node
    
    def __remove(self, node, key):
        if not node: return None

        if node.key < key:
            node.right = self.__remove(node.right, key)
            node.count -= 1
            return node
        elif node.key > key:
            node.left = self.__remove(node.left, key)
            node.count -= 1
            return node
        else: # if equal then remove node, use predessor to replace, 原版使用 successor
            if node.dups > 1:
                node.dups -= 1
                return node
            if not node.left:
                right = node.right
                self.count -= 1
                return right
            if not node.right:
                left = node.left
                self.count -= 1
                return left
            # if both have
            predessor = self.__maximum(node.left)
            predessor.count = node.count - 1
            predessor.left = self.__remove_max(node.left)
            predessor.right = node.right
            return predessor
            
    def __successor(self, node):
        if not node or not node.right: return None
        return self.__minimum(node.right)

    def __predessor(self, node):
        if not node or not node.left: return None
        return self.__maximum(node.left)\
    
    def __floor(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node.key
        elif node.key < key:
            suc = self.__successor(node)
            if (not suc) or (suc.key > key):
                return node.key
            return self.__floor(node.right, key)
        else:
            return self.__floor(node.left, key)
    
    def __ceil(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node.key
        elif node.key > key:
            pred = self.__predessor(node)
            if (not pred) or (pred.key < key):
                return node.key
            return self.__ceil(node.left, key)
        else:
            return self.__ceil(node.right, key)
    
    def __rank(self, node, key):
        if node.key == key:
            if node.left:
                return node.left.count + 1
            return 1
        elif node.key > key:
            return self.__rank(node.left, key)
        else:
            if node.left:
                return node.left.count + 1 + self.__rank(node.right, key)
            return 1 + self.__rank(node.right, key)

    def __select(self, node, rank):
        count = node.left.count if node.left else 0
        if count + 1 == rank:
            return node
        elif count + 1 < rank:
            return self.__select(node.right, rank - count - 1)
        else:
            return self.__select(node.left, rank)

    def insert(self, key, value):
        self.root = self.__insert_recur(self.root, key, value)
        # self.root = self.__insert_iter(self.root, key, value)
    
    def contain(self, key):
        # Check is this BTS contain key
        return self.__contain(self.root, key)
    
    def search(self, key, get_node=False):
        # Search key in BTS or not, if in return value, else return None
        return self.__search(self.root, key, get_node=get_node)
    
    def preorder(self):
        self.__preoder(self.root)

    def inorder(self):
        self.__inoder(self.root)
    
    def postorder(self):
        self.__postorder(self.root)
    
    def minimum(self):
        assert self.count != 0
        return self.__minimum(self.root).value
    
    def maximum(self):
        assert self.count != 0
        return self.__maximum(self.root).value

    def levelorder(self):
        q = [self.root]
        while q:
            node = q.pop(0)
            print(node.key)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    def remove_min(self):
        if self.root:
            self.root = self.__remove_min(self.root)
    
    def remove_max(self):
        if self.root:
            self.root = self.__remove_max(self.root)
    
    def remove(self, key):
        self.root = self.__remove(self.root, key)
    
    def successor(self, key):
        node = self.search(key, get_node=True)
        return self.__successor(node)
    
    def predessor(self, key):
        node = self.search(key, get_node=True)
        return self.__predessor(node)
    
    def floor(self, key):
        return self.__floor(self.root, key)
    
    def ceil(self, key):
        return self.__ceil(self.root, key)
    
    def rank(self, key):
        # Find element's rank
        assert self.contain(key), f"Not contain Key:{key}"
        return self.__rank(self.root, key)

    def select(self, rank):
        # Find the selected rank node
        assert rank > 0, f"Rank should bigger than 0"
        assert rank <= self.count, f"Rank {rank} more than total count {self.count}"
        return self.__select(self.root, rank)

if __name__ == "__main__":
    bst = BST()
    # print(bst.is_empty())
    # print(bst.size())
    bst.insert(10, "ten")
    bst.insert(5, "five")
    bst.insert(10, "Good")
    # print(bst.root.left.value)
    # print(bst.root.right.value)
    bst.insert(6, "six")
    bst.insert(14, "14")
    bst.insert(7, "seven")
    bst.insert(99, '归一')
    bst.insert(99, "smsm")
    print_tree(bst)

    print()
    print(bst.rank(14))
    # print(bst.select(0))
    # print(bst.select(1))
    # print(bst.select(2))
    # print(bst.select(3))
    # print(bst.select(4))
    # print(bst.select(5))
    # print(bst.select(6))
    # bst.remove(10)
    # print_tree(bst)
    # print(bst.successor(15))
    # print(bst.predessor(15))
    # n = 30
    # print("Floor: ", bst.floor(n))
    # print("Ceil: ", bst.ceil(n))
    # print(bst.search(11, True))
    # print(bst.search(7))
    # node = bst.search(99, get_node=True)
    # node.value = "太极"
    # print(bst.search(99))

    # print("Preorder: ")
    # bst.preorder()
    # print()
    # print("Inorder: ")
    # bst.inorder()
    # print()
    # print("PostOrder: ")
    # bst.postorder()
    # print()
    # print("Level Order: ")
    # bst.levelorder()
    # print()
    # print("Maximum: ")
    # print(bst.maximum())
    # print("Minimum: ")
    # print(bst.minimum())
    # bst.remove_min()
    # print_tree(bst)
    # bst.remove_max()
    # print_tree(bst)
    # bst.remove(5)
    # print_tree(bst)