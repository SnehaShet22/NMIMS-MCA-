############DELETION OF NODE ADDED####################
class Node:
    def _init_(self,data) -> None:
        self.data = data 
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
# 25 78 43 54 12 00 167 24

#                               25     
# 
#                     12                     78   
# 
#              00         24         43              167
# 
#                                          54
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()  

######  PreOrder Visualisation #####
#               25  [25 12 0 24 78 43 54 167]

#        12 [12 0 24]           78 [78 43 54 167]

#    0 [0]      24 [24]      43 [43 54]         167 [167]

#                                  54 [54]


    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res   


    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res 


    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

    def minValueNode(node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
         
        return current

#                               25     right.insert(54)
# 
#                     12                     78   left.insert(54)  self.left=43
# 
#              00                       43              167
# 
#                                            54

    def deleteNode(self,root,data):
 
        # Base Case
        if root is None:
            return root
    
        # If the data to be deleted
        # is smaller than the root's
        # data then it lies in  left subtree
        if data < root.data:
            root.left = self.deleteNode(root.left, data)
    
        # If the kye to be delete
        # is greater than the root's data
        # then it lies in right subtree
        elif(data > root.data):
            root.right = self.deleteNode(root.right, data)
    
        # If data is same as root's data, then this is the node
        # to be deleted
        else:
    
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp
    
            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)
    
            # Copy the inorder successor's
            # content to this node
            root.data = temp.data
    
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.data)
    
        return root   

root = Node(25)

root.insert(78)

root.insert(43)

# root.insert(100)

root.insert(54)

root.insert(12)
root.insert(00)
root.insert(167)
