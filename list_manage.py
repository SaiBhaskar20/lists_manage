# Shopping list manager

# Create an empty list
shopping_list = []

while True:
    print("\n--- Shopping List Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Check if item exists")
    print("5. Sort list")
    print("6. Exit")

    choice = input("Enter your choice (1–6): ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to list.")
    
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print(f"{item} not found in list.")
    
    elif choice == "3":
        print("Current Shopping List:", shopping_list)
    
    elif choice == "4":
        item = input("Enter item to check: ")
        if item in shopping_list:
            print(f"{item} is in the list.")
        else:
            print(f"{item} is NOT in the list.")
    
    elif choice == "5":
        shopping_list.sort()
        print("Sorted List:", shopping_list)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1–6.")
