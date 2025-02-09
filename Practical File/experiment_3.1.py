# Performing Various Operations on Lists
def add_element(my_list):
    element = int(input("Enter an element to append: "))
    my_list.append(element)
    print(f"{element} added successfully!\n")
def remove_element(my_list):
    element = int(input("Enter an element to remove: "))
    if element in my_list:
        my_list.remove(element)
        print(f"{element} removed successfully!\n")
    else:
        print(f"Element {element} not found in the list.\n")
def sort_list(my_list):
    print("Sorted List (Ascending):", sorted(my_list))
def reverse_sort_list(my_list):
    print("Sorted List (Descending):", sorted(my_list, reverse=True))
def find_element(my_list):
    element = int(input("Enter an element to find: "))
    if element in my_list:
        print(f"Index of {element}: {my_list.index(element)}\n")
    else:
        print(f"Element {element} not found in list.\n")
def combine_lists(my_list):
    extra_list = list(map(int, input("Enter another list elements separated by space: ").split()))
    print("Combined List:", my_list + extra_list, "\n")
def display_list(my_list):
    print("Current List:", my_list, "\n")
def main():
    my_list = list(map(int, input("Enter the list elements separated by space: ").split()))  
    while True:
        print("Menu:")
        print("1. Add Element")
        print("2. Remove Element")
        print("3. Sort List (Ascending)")
        print("4. Sort List (Descending)")
        print("5. Find Element")
        print("6. Combine Lists")
        print("7. Display List")
        print("8. Exit")
        choice = input("Enter your choice: ")    
        if choice == '1':
            add_element(my_list)
        elif choice == '2':
            remove_element(my_list)
        elif choice == '3':
            sort_list(my_list)
        elif choice == '4':
            reverse_sort_list(my_list)
        elif choice == '5':
            find_element(my_list)
        elif choice == '6':
            combine_lists(my_list)
        elif choice == '7':
            display_list(my_list)
        elif choice == '8':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()