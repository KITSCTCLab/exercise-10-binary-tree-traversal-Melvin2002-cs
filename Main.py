class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

        
        


def insert(root, new_value) -> BinaryTreeNode:
    
    # Write your code here
    if root==None:
        root=BinaryTreeNode(new_value)
    else:
        temp=root
        while(temp!=None):
            if temp.data>new_value:
                temp=temp.left_child
            else:
                temp=temp.right_child
        temp=BinaryTreeNode(new_value)


def inorder(root) -> None:
    # Write your code here
    if root.left_child==None:
        print(root.data,end=" ")
        return
    inorder(root.left_child)
    print(root.data,end=" ")
    inorder(root.right_child)
    
    

def preorder(root) -> None:
    # Write your code here


def postorder(root) -> None:
    # Write your code here


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)




"""If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
