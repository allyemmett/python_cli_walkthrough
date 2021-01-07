"""
Work wants an inventory app that:
    Stores Data into a file
    Uses the command line to list/add/update/delete:
        "Items" they have:
            id
            name
            cond
"""
from models.item import Item  # And Import Statement to make code from other files available

next_id = 0
items = []  # This will be used to store items

def menu():  # Prints Menu Options for the user
    print("""
1. List All Items
2. Add New Item
3. Update Existing Item
4. Delete Item (By item id)
5. Exit
""")

def list_items():  # Writes all items to the Terminal
    for item in items:
        print(item)

def new_item():  # Gets user input for all need fields for an Item
    global next_id  # Allows us access to the next_id number

    name = input("Name: ")
    cond = input("Condition: ")
    item_id = next_id  # Uses the global counter to give a Unique Id for each "Item"

    next_id += 1  # Updates Id with new value so next one is 1 more

    # This is the Class -> Item from the other file we imported 
    tmp = Item(item_id, name, cond)  # Builds An Item/Stores it in tmp

    items.append(tmp)  # Adds Item to global items array

def update_existing(): # Update Existing Item
    print("inside update existing")
    if not items:
        print("You have no items to update")
        return
    list_items()
    try:
        item_id_to_update = int(input("What is the item id you wish to update\n>"))
    except Exception:
        print("not a valid number")
        return

    for item in items:
        if item.item_id == item_id_to_update:
            name = input("Name: ")
            cond = input("Condition: ")
            item.name = name
            item.condition = cond
            break
    else: # if for loop does not find a match, else will fire EVEN THOUGH else is outside for loop (when else is outside, will fire if at END of loop no match is found)
        print("We didn't find a match")


def delete_item(): # Delete Item (By item id)
    print("inside del item")
    if not items: # check make sure have item
        print("You have no items to update")
        return
    list_items() # shows choices for user 
    try:
        item_id_to_delete = int(input("What is the item you wish to update\n>")) # turn user input into number
    except Exception: # if casting from string to number fails, then back to menu loop
        print("Not a valid number.")
        return
    for index, item in enumerate(items): # Otherwise, look at items in list... need enumerate with index 
        if item.item_id == item_id_to_delete: # if id is same as number to type in,
            index_to_remove = index # then will remove the item with the id inputted by user
            break
    else:
        print("We didn't find a match")
        return
    print(f"Found:\n{items.pop(index_to_remove)} it has been removed") # removes item from list, but also gives back to user 
    

def main():  # Starts the Program off, holds the loop until exit.
    while True:
        menu()  # Prints the Options to the Terminal
        choice = input("> ")  # Takes use choice

        # The Conditional Options: hands off the work to the functions above.
        if choice == "1":
            list_items() 
        elif choice == "2":
            new_item()
        elif choice == "3":
            update_existing()
        elif choice == "4":
            delete_item()
        elif choice == "5":  # Exit
            exit()
        else:  # User gave us bad input we let them know then loop again.
            input("Invalid Input!\n(Press Enter to try again)")


# TODO Make the File Saving stuff

if __name__ == "__main__":
    main()

