"""hbfuisrhosf"""
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

    if node is None:
        return []
    else:
        answer_list = [node.data]

        # if node.left:
        # answer_list.append(node.left.data)
        # answer_list += pre_order(node.left)

    # if node.right:
        # answer_list.append(node.right.data)
        # answer_list += pre_order(node.right)

        # if node is None:
        #     answer_list.append('leaf')

    return answer_list + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):

    if node is None:
        return []
    else:
        answer_list = [node.data]

        if node.left:
            answer_list.append(node.left.data)
            pre_order(node.left)

        answer_list.append(node.data)

        if node.right:
            answer_list.append(node.right.data)
            pre_order(node.right)

        if node is None:
            answer_list.append('leaf')

    return answer_list

# Post-order traversal
def post_order(node):

    if node is None:
        return []
    else:
        answer_list = [node.data]

        if node.left:
            answer_list.append(node.left.data)
            pre_order(node.left)

        if node.right:
            answer_list.append(node.right.data)
            pre_order(node.right)

        if node is None:
            answer_list.append('leaf')

        answer_list.append(node.data)

    return answer_list
