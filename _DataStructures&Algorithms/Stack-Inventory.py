<<<<<<< HEAD
class Stack:

    # Initilize an Empty List to represent the stack
    def __init__(self, limit):
        self.stack = []
        self.limit = limit

    # Add a Item to the top of the stack
    def push(self, item):
        if len(self.stack) < self.limit:
            self.stack.append(item)
            print("Item added to the stack.")

        else:
            print("----------------------------------")
            print("Stack is already full. Cannot add item.")

    # Remove the Item from the top of the Stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        
        else:
            print("----------------------------------")
            print("Stack is already empty. Cannot remove item.")

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Return the Height (Number of Items) of the Stack
    def height(self):
        return len(self.stack)


def main():
    # Creating instances of a stack for Stack 1 to 3 with a limit of 9 Items
    stack1 = Stack(2)
    stack2 = Stack(9)
    stack3 = Stack(9)

    equipment_list = ["Sword", "Shield", "MedallionofHope", "Helmet", "Leggings", "ChestPlate"]

    while True:
        print("----------------------------------")
        print("1. Character 1")
        print("2. Character 2")
        print("3. Character 3")
        print("4. Quit")
        print("----------------------------------")

        choice = input("Select a character (1-3) or quit (4): ")
        print("----------------------------------")

        if choice == "1":
            print("1. Add item")
            print("2. Remove item")
            print("----------------------------------")
            action_choice = input("Select an action (1-2): ")

            if action_choice == "1":
                print("----------------------------------")
                print("Equipment List:", equipment_list)
                item = input("Enter the item to add to Character 1: ")
                stack1.push(item)

                print("----------------------------------")
                print("Character 1 Equipment Count:", stack1.height())
                print("Character 1 Equipment:", stack1.stack)
                
            elif action_choice == "2":
                removed_item = stack1.pop()

                if removed_item:
                    print("----------------------------------")
                    print("Item removed from Character 1:", removed_item)

                    print("----------------------------------")
                    print("Character 1 Equipment Count:", stack1.height())
                    print("Character 1 Equipment:", stack1.stack)

            else:
                print("----------------------------------")
                print("Invalid action. Please try again.")

        elif choice == "2":
            print("1. Add item")
            print("2. Remove item")
            print("----------------------------------")
            action_choice = input("Select an action (1-2): ")

            if action_choice == "1":
                print("----------------------------------")
                print("Equipment List:", equipment_list)
                item = input("Enter the item to add to Character 2: ")
                stack2.push(item)

                print("----------------------------------")
                print("Character 2 Equipment Count:", stack2.height())
                print("Character 2 Equipment:", stack2.stack)

            elif action_choice == "2":
                removed_item = stack2.pop()

                if removed_item:
                    print("----------------------------------")
                    print("Item removed from Character 2:", removed_item)

                    print("----------------------------------")
                    print("Character 2 Equipment Count:", stack2.height())
                    print("Character 2 Equipment:", stack2.stack)
                    
            else:
                print("----------------------------------")
                print("Invalid action. Please try again.")

        elif choice == "3":
            print("1. Add item")
            print("2. Remove item")
            print("----------------------------------")
            action_choice = input("Select an action (1-2): ")

            if action_choice == "1":
                print("----------------------------------")
                print("Equipment List:", equipment_list)
                item = input("Enter the item to add to Character 3: ")
                stack3.push(item)

                print("----------------------------------")
                print("Character 3 Equipment Count:", stack3.height())
                print("Character 3 Equipment:", stack3.stack)

            elif action_choice == "2":
                removed_item = stack3.pop()

                if removed_item:
                    print("----------------------------------")
                    print("Item removed from Character 3:", removed_item)

                    print("----------------------------------")
                    print("Character 3 Equipment Count:", stack3.height())
                    print("Character 3 Equipment:", stack3.stack)
                    
            else:
                print("----------------------------------")
                print("Invalid action. Please try again.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
            print("----------------------------------")


if __name__ == "__main__":
    class Stack:

        # Initilize an Empty List to represent the stack
        def __init__(self, limit):
            self.stack = []
            self.limit = limit

        # Add a Item to the top of the stack
        def push(self, item):
            if len(self.stack) < self.limit:
                self.stack.append(item)
                print("Item added to the stack.")

            else:
                print("----------------------------------")
                print("Stack is already full. Cannot add item.")

        # Remove the Item from the top of the Stack
        def pop(self):
            if not self.is_empty():
                return self.stack.pop()
            
            else:
                print("----------------------------------")
                print("Stack is already empty. Cannot remove item.")

        # Check if the stack is empty
        def is_empty(self):
            return len(self.stack) == 0

        # Return the Height (Number of Items) of the Stack
        def height(self):
            return len(self.stack)


    def main():
        # Creating instances of a stack for Stack 1 to 3 with a limit of 9 Items
        stack1 = Stack(2)
        stack2 = Stack(9)
        stack3 = Stack(9)

        equipment_list = ["Sword", "Shield", "MedallionofHope", "Helmet", "Leggings", "ChestPlate"]

        while True:
            print("----------------------------------")
            print("1. Character 1")
            print("2. Character 2")
            print("3. Character 3")
            print("4. Quit")
            print("----------------------------------")

            choice = input("Select a character (1-3) or quit (4): ")
            print("----------------------------------")

            if choice == "1":
                print("1. Add item")
                print("2. Remove item")
                print("----------------------------------")
                action_choice = input("Select an action (1-2): ")

                if action_choice == "1":
                    print("----------------------------------")
                    print("Equipment List:", equipment_list)
                    item = input("Enter the item to add to Character 1: ")
                    stack1.push(item)

                    print("----------------------------------")
                    print("Character 1 Equipment Count:", stack1.height())
                    print("Character 1 Equipment:", stack1.stack)
                    
                elif action_choice == "2":
                    removed_item = stack1.pop()

                    if removed_item:
                        print("----------------------------------")
                        print("Item removed from Character 1:", removed_item)

                        print("----------------------------------")
                        print("Character 1 Equipment Count:", stack1.height())
                        print("Character 1 Equipment:", stack1.stack)

                else:
                    print("----------------------------------")
                    print("Invalid action. Please try again.")

            elif choice == "2":
                print("1. Add item")
                print("2. Remove item")
                print("----------------------------------")
                action_choice = input("Select an action (1-2): ")

                if action_choice == "1":
                    print("----------------------------------")
                    print("Equipment List:", equipment_list)
                    item = input("Enter the item to add to Character 2: ")
                    stack2.push(item)

                    print("----------------------------------")
                    print("Character 2 Equipment Count:", stack2.height())
                    print("Character 2 Equipment:", stack2.stack)

                elif action_choice == "2":
                    removed_item = stack2.pop()

                    if removed_item:
                        print("----------------------------------")
                        print("Item removed from Character 2:", removed_item)

                        print("----------------------------------")
                        print("Character 2 Equipment Count:", stack2.height())
                        print("Character 2 Equipment:", stack2.stack)
                        
                else:
                    print("----------------------------------")
                    print("Invalid action. Please try again.")

            elif choice == "3":
                print("1. Add item")
                print("2. Remove item")
                print("----------------------------------")
                action_choice = input("Select an action (1-2): ")

                if action_choice == "1":
                    print("----------------------------------")
                    print("Equipment List:", equipment_list)
                    item = input("Enter the item to add to Character 3: ")
                    stack3.push(item)

                    print("----------------------------------")
                    print("Character 3 Equipment Count:", stack3.height())
                    print("Character 3 Equipment:", stack3.stack)

                elif action_choice == "2":
                    removed_item = stack3.pop()

                    if removed_item:
                        print("----------------------------------")
                        print("Item removed from Character 3:", removed_item)

                        print("----------------------------------")
                        print("Character 3 Equipment Count:", stack3.height())
                        print("Character 3 Equipment:", stack3.stack)
                        
                else:
                    print("----------------------------------")
                    print("Invalid action. Please try again.")

            elif choice == "4":
                break

            else:
                print("Invalid choice. Please try again.")
                print("----------------------------------")


if __name__ == "__main__":
    main()