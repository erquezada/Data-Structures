class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree_from_list(nodes):
    def helper(index):
        if index < len(nodes):
            value = nodes[index]
            if value is None:
                return None
            node = TreeNode(value)
            node.left = helper(2 * index + 1)
            node.right = helper(2 * index + 2)
            return node
        return None
    return helper(0)