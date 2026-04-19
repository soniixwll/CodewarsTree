from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

# def has_children(node):

def tree_by_levels(node):

    if node is None:
        return []

    answear_list = []
    queue = deque([node])
    while queue:
        part = queue.popleft()
        answear_list.append(part.value)

        if part.left:
            queue.append(part.left)

        if part.right:
            queue.append(part.right)

    return answear_list
