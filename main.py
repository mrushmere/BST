from BinarySearchTree import BinarySearchTree

def DeepestNodes(bstArray):
    rootNode = BinarySearchTree(bstArray)
    lowestLevel = rootNode.GetTreeHeight(rootNode.Root)
    lowestNodes = ",".join(map(str,rootNode.GetNodesForLevel(rootNode.Root, 1, lowestLevel, []))) 
    print("deepest, {}; depth, {}".format(lowestNodes, lowestLevel-1))

bstArray = list(map(int, input("Enter binary tree as comma separated values").split(",")))
DeepestNodes(bstArray)