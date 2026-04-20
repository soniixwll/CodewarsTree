# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:

            if not root.left:
                return root.right
            # elif not root.right:
            elif not root.right:
                return root.left
            else:
                head = root.right
                while head.left:
                    head = head.left

                root.val = head.val

                root.right = self.deleteNode(root.right , head.val)

                return root
