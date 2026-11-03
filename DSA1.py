n = int(input("Enter total number of library members: "))

borrowed_books = []

for i in range(n):
    count = int(input(f"Enter number of books borrowed by Member {i + 1}: "))
    borrowed_books.append(count)

total_books = sum(borrowed_books)
average = total_books / n

highest = max(borrowed_books)
lowest = min(borrowed_books)

zero_count = borrowed_books.count(0)

frequency = {}

for count in borrowed_books:
    if count in frequency:
        frequency[count] += 1
    else:
        frequency[count] = 1

max_frequency = max(frequency.values())

modes = []
for count in frequency:
    if frequency[count] == max_frequency:
        modes.append(count)

print("\n----- Library Borrowing Record -----")
print("Total Members:", n)
print("Borrowing Records:", borrowed_books)
print("Average Books Borrowed:", average)
print("Highest Number of Books Borrowed:", highest)
print("Lowest Number of Books Borrowed:", lowest)
print("Members Who Borrowed 0 Books:", zero_count)
print("Most Frequently Borrowed Count:", modes)
print("Highest Frequency:", max_frequency)