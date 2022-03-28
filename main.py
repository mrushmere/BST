from BinarySearchTree import BinarySearchTree

bstArray = list(map(int, input("Enter binary tree as comma separated list").split(",")))
rootNode = BinarySearchTree(bstArray)
lowestLevel = rootNode.GetTreeHeight(rootNode.Root)
lowestNodes = ",".join(map(str,rootNode.GetNodesForLevel(rootNode.Root, 1, lowestLevel, []))) 

print("deepest, {}; depth, {}".format(lowestNodes, lowestLevel-1))
