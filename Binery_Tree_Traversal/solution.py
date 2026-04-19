"""Module traversal tree"""
class Node:
    def __init__(self, data=None, left=None, right=None):
        if data == None:
            self.data = 'leaf'
        else:
            self.data = data

        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node: Node):
    """Traversal in pre-order"""

    if node is None:
        return []
    else:
        answer_list = [node.data]

    return answer_list + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    """Traversal in in-order"""

    if node is None:
        return []
    else:
        answer_list = [node.data]

    return in_order(node.left) + answer_list + in_order(node.right)

# Post-order traversal
def post_order(node):
    """Traversal in post-order"""

    if node is None:
        return []
    else:
        answer_list = [node.data]

    return post_order(node.left) + post_order(node.right) + answer_list
