from Node import Node

class BinarySearchTree:

    def __init__(self, bstArray):
        self.Root = self.ConvertArrayToBinarySearchTree(bstArray)

    def ConvertArrayToBinarySearchTree(self, bstArray):
        if not bstArray:
            return
        
        root = None
        for key in bstArray: 
            root = self.InsertNode(root, key)        

        return root
        
    def InsertNode(self, node: Node, key):
        if node is None:
            return Node(key)
        else :
            if key > node.Key:
                node.Right = self.InsertNode(node.Right, key)
            elif key < node.Key:
                node.Left = self.InsertNode(node.Left, key)

        return node

    def GetTreeHeight(self, node: Node):
        maxHeight = 0
        if node is None:
            return 0

        leftHeight = self.GetTreeHeight(node.Left)
        rightHeight = self.GetTreeHeight(node.Right)

        maxHeight = max(leftHeight, rightHeight) + 1

        return maxHeight

    def GetNodesForLevel(self, node: Node, currentLevel, desiredLevel, nodesAtLevel):

        if node is None:
            return

        if currentLevel == desiredLevel:
            nodesAtLevel.append(node.Key)

        currentLevel += 1
        self.GetNodesForLevel(node.Left, currentLevel, desiredLevel, nodesAtLevel)
        self.GetNodesForLevel(node.Right, currentLevel, desiredLevel, nodesAtLevel)

        return nodesAtLevel
