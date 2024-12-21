import treeNode

def numberLeafs(root):
    # Write your code here.
    pass

# number of nodes along the longest path from the root node down to the farthest leaf node.
def maximumDepth(root):
    pass

# Given a root of a BINARY SEARCH TREE, and a value k, return a list with the path from root to k (including root and k)
# Assume k always exists in the binary search tree (There is always a valid path)
def path_to_k(root,k):
    pass

if __name__ == "__main__":
    print("Problem 1: ")
    tree_list = [[3, 9, 20, None, None, 15, 7],[1,2,2,3,3,None,None,4,4],[1]]
    for l in tree_list:
        root = treeNode.build_tree_from_list(l)
        print(numberLeafs(root))
    
    print("Problem 2: ")
    tree2_list = [[3,9,20,None,None,15,7],[1,None,2]]
    for l in tree2_list:
        root2 = treeNode.build_tree_from_list(l)
        print(maximumDepth(root2))

    print("Problem 3: ")
    tree3_list = [15,9,20,None,None,17,30]
    root3 = treeNode.build_tree_from_list(tree3_list)
    print(path_to_k(root3, 30))
    tree3_list2 = [24,17,43,16,23,17,30,10,None,18,None]
    root4 = treeNode.build_tree_from_list(tree3_list2)
    print(path_to_k(root4, 18))
    
    

'''
Expected output:

Problem 1: 
3
4
1

Problem 2:
3
2

Problem 3:
[15, 20, 30]
[24, 17, 23, 18]

'''   

