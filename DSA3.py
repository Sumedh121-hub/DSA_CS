from collections import deque

# Create queue
call_queue = deque()

# Add a call
def addCall():
    customerID = input("Enter Customer ID: ")
    callTime = int(input("Enter Call Time (minutes): "))

    call_queue.append((customerID, callTime))
    print("Call added successfully.")

# Answer a call
def answerCall():
    if not call_queue:
        print("Queue is empty. No call to answer.")
    else:
        customerID, callTime = call_queue.popleft()
        print("Answered Call")
        print("Customer ID:", customerID)
        print("Call Time:", callTime, "minutes")

# View all calls
def viewQueue():
    if not call_queue:
        print("Queue is empty.")
    else:
        print("\nCurrent Call Queue:")
        for customerID, callTime in call_queue:
            print("Customer ID:", customerID,
                  "| Call Time:", callTime, "minutes")

# Check if queue is empty
def isQueueEmpty():
    if not call_queue:
        print("Queue is empty.")
    else:
        print("Queue is not empty.")

# Menu
while True:
    print("\n----- CALL CENTER QUEUE -----")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check Queue Empty")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addCall()

    elif choice == 2:
        answerCall()

    elif choice == 3:
        viewQueue()

    elif choice == 4:
        isQueueEmpty()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")