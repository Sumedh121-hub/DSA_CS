# Hash Table using Division Method and Linear Probing

SIZE = 10
hash_table = [None] * SIZE
DELETED = "DELETED"

# Hash function using Division Method
def hash_function(key):
    return key % SIZE

# Insert a key
def insert(key):
    index = hash_function(key)

    for i in range(SIZE):
        new_index = (index + i) % SIZE

        if hash_table[new_index] == key:
            print("Key already exists.")
            return

        if hash_table[new_index] is None or hash_table[new_index] == DELETED:
            hash_table[new_index] = key
            print("Key inserted successfully.")
            return

    print("Hash Table is full.")

# Search for a key
def search(key):
    index = hash_function(key)

    for i in range(SIZE):
        new_index = (index + i) % SIZE

        if hash_table[new_index] is None:
            break

        if hash_table[new_index] == key:
            print("Key found at index:", new_index)
            return

    print("Key not found.")

# Delete a key
def delete(key):
    index = hash_function(key)

    for i in range(SIZE):
        new_index = (index + i) % SIZE

        if hash_table[new_index] is None:
            break

        if hash_table[new_index] == key:
            hash_table[new_index] = DELETED
            print("Key deleted successfully.")
            return

    print("Key not found.")

# Display hash table
def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(i, ":", hash_table[i])

# Main menu
while True:
    print("\n----- HASH TABLE MENU -----")
    print("1. Insert a Key")
    print("2. Search for a Key")
    print("3. Delete a Key")
    print("4. Display Hash Table")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        insert(key)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")