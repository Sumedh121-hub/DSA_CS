class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # 1. Add student at the end
    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print(f"Added: ({roll}, '{name}', {marks})")

    # 2. Delete student by roll number
    def delete(self, roll):
        temp = self.head
        prev = None

        # Search for the node to delete
        while temp is not None and temp.roll != roll:
            prev = temp
            temp = temp.next

        # Node not found
        if temp is None:
            print(f"Roll No {roll} not found")
            return

        # Deleting the head node
        if prev is None:
            self.head = temp.next
        else:
            # Bypassing the node
            prev.next = temp.next

        print(f"Deleted record of Roll No {roll}")

    # 3. Update student details
    def update(self, roll, new_name, new_marks):
        temp = self.head
        while temp is not None:
            if temp.roll == roll:
                temp.name = new_name
                temp.marks = new_marks
                print(f"Updated record of Roll No {roll}")
                return
            temp = temp.next
        print(f"Roll No {roll} not found")

    # 4. Search student by roll number
    def search(self, roll):
        temp = self.head
        while temp is not None:
            if temp.roll == roll:
                print(f"Record Found -> Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
                return
            temp = temp.next
        print("Record Not found")

    # 5. Sort records (Bubble Sort swapping data fields)
    def sort(self, field="roll", ascending=True):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next is not None:
                a = getattr(temp, field)
                b = getattr(temp.next, field)

                # Comparison check
                if (ascending and a > b) or (not ascending and a < b):
                    # Swap data fields between adjacent nodes
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next

        order = "ascending" if ascending else "descending"
        print(f"Records sorted by {field} ({order})")

    # 6. Display all records
    def display(self):
        if self.head is None:
            print("No records found.")
            return

        print(f"{'Roll No':<8} | {'Name':<12} | {'Marks'}")
        print("-" * 32)
        temp = self.head
        while temp is not None:
            print(f"{temp.roll:<8} | {temp.name:<12} | {temp.marks}")
            temp = temp.next
        print()


# ---------------- Interactive Menu-Driven Runner ----------------
# Use this block if the examiner asks for terminal input (matches practical flowchart)
if __name__ == "__main__":
    system = StudentList()

    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Record")
        print("2. Delete Record")
        print("3. Update Record")
        print("4. Search Record")
        print("5. Sort Records")
        print("6. Display Records")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            roll = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            system.add(roll, name, marks)

        elif choice == "2":
            roll = int(input("Enter Roll No to delete: "))
            system.delete(roll)

        elif choice == "3":
            roll = int(input("Enter Roll No to update: "))
            name = input("Enter New Name: ")
            marks = float(input("Enter New Marks: "))
            system.update(roll, name, marks)

        elif choice == "4":
            roll = int(input("Enter Roll No to search: "))
            system.search(roll)

        elif choice == "5":
            field_choice = input("Sort by (1. Roll No / 2. Marks): ").strip()
            field = "marks" if field_choice == "2" else "roll"
            order_choice = input("Order (1. Ascending / 2. Descending): ").strip()
            asc = False if order_choice == "2" else True
            system.sort(field=field, ascending=asc)
            system.display()

        elif choice == "6":
            system.display()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, try again.")