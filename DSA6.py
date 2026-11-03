# Practical No. 6
# Binary Search Tree (BST)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert a node
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

# Search a key
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

# Find minimum node
def find_min(root):
    while root.left is not None:
        root = root.left
    return root

# Delete a node
def delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Preorder traversal
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

# Main program
root = None
while True:
    print("\n\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display (Inorder)")
    print("5. Display (Preorder)")
    print("6. Display (Postorder)")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        key = int(input("Enter value: "))
        root = insert(root, key)
        print("Node inserted successfully.")
    elif choice == '2':
        key = int(input("Enter value to search: "))
        if search(root, key):
            print("Value found in BST.")
        else:
            print("Value not found.")
    elif choice == '3':
        key = int(input("Enter value to delete: "))
        if search(root, key):
            root = delete(root, key)
            print("Node deleted successfully.")
        else:
            print("Value not found.")
    elif choice == '4':
        print("Inorder Traversal:", end=" ")
        inorder(root)
    elif choice == '5':
        print("Preorder Traversal:", end=" ")
        preorder(root)
    elif choice == '6':
        print("Postorder Traversal:", end=" ")
        postorder(root)
    elif choice == '7':
        print("Program terminated.")
        break
    else:
        print("Invalid choice.")