"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        pre = [] #array
        def check(node, arr):
            if node == None: #base call 1
                return 0
            arr.append(node.val) #add val to list
            if node.children == None: #base call 2
               return 0
            i = 0
            while i < len(node.children): #recursive call
                check(node.children[i], arr)
                i += 1
        check(root, pre)
        return pre
      
'''
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
'''
