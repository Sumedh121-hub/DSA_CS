# Linear Search Function
def linear_search(id_list, key):
    n = len(id_list)
    i = 0
    while i < n:
        if id_list[i] == key:
            print(f"Customer ID {key} Found at position {i}")
            return i
        i += 1
    print(f"Customer ID {key} Not Found")
    return -1


# Binary Search Function (Array must be sorted)
def binary_search(id_list, key):
    low = 0
    high = len(id_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if id_list[mid] == key:
            print(f"Customer ID {key} Found at position {mid}")
            return mid
        elif key < id_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    print(f"Customer ID {key} Not Found")
    return -1


# --- Driver Code / Testing ---
if __name__ == "__main__":
    # Test Data: Unsorted list of Customer Account IDs
    customer_ids = [1045, 1012, 1088, 1003, 1067, 1031, 1099, 1020]
    
    print("Customer ID List (unsorted):", customer_ids)
    print("\n--- LINEAR SEARCH ---")
    linear_search(customer_ids, 1067)  # Found case
    linear_search(customer_ids, 1500)  # Not found case

    # Binary search requires sorted data
    sorted_ids = sorted(customer_ids)
    print("\nCustomer ID List (sorted):", sorted_ids)
    print("\n--- BINARY SEARCH ---")
    binary_search(sorted_ids, 1067)   # Found case
    binary_search(sorted_ids, 1500)   # Not found case