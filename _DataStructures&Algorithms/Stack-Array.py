<<<<<<< HEAD
class Stack:

    # Initilize an Empty List to represent the stack
    def __init__(self):
        self.stack = []

    # Add a Item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # Remove the Item from the top of the Stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Return the Height (Number of Items) of the Stack
    def height(self):
        return len(self.stack)

# Check if the stack are equal in height or not
def find_equal_height(stack1, stack2, stack3):
    height1 = stack1.height()   # Get the height of Stack 1
    height2 = stack2.height()   # Get the height of Stack 2
    height3 = stack3.height()   # Get the height of Stack 3

    if height1 == height2 == height3:
        print("----------------------------------")
        print("The stacks are equal at height:", height1)   # If all stacks equals in height, print the height
    else:
        print("----------------------------------")
        print("The stacks are not equal at any height.")    # if the heights are not equal, print a message

# Gets a set of elements from the user to the machine
def get_stack_elements():
    print("----------------------------------")
    elements = input("Enter the elements of the stack (separated by space): ")
    return elements.split()


def main():
    continue_program = True
    iteration = 1
    stack1_elements = []
    stack2_elements = []
    stack3_elements = []


    while continue_program:
        # Creating instances of a stack for Stack 1 to 3
        stack1 = Stack()
        stack2 = Stack()
        stack3 = Stack()
        
        # Get the elements from the function "get_stack_elements" to retrieved for each stack
        elements1 = get_stack_elements()
        elements2 = get_stack_elements()
        elements3 = get_stack_elements()

        stack1_elements.extend(elements1)
        stack2_elements.extend(elements2)
        stack3_elements.extend(elements3)

        #  Push each element to Stack 1-3
        for element in elements1:
            stack1.push(element)
        for element in elements2:
            stack2.push(element)
        for element in elements3:
            stack3.push(element)

        # Print the height of Stack 1-3
        print("----------------------------------")
        print("Current elements of Stack 1:", stack1_elements)
        print("Current elements of Stack 2:", stack2_elements)
        print("Current elements of Stack 3:", stack3_elements)

        # Check if the heights of each are equal using the "find_equal_height" function
        find_equal_height(stack1, stack2, stack3)

        choice = input("Enter the stack number to pop from (1, 2, 3, or ): ")
        if choice == '1':
            stack1.pop()
        elif choice == '2':
            stack2.pop()
        elif choice == '3':
            stack3.pop()
        else:
            print("Invalid choice. Please try again.")

        # Checks if the user wants to continue or not
        print("----------------------------------")
        choice = input("Do you want to continue? (Y/N): ")
        if choice.lower() == 'n':
            continue_program = False

        iteration += 1


if __name__ == "__main__":
    class Stack:

        # Initilize an Empty List to represent the stack
        def __init__(self):
            self.stack = []

        # Add a Item to the top of the stack
        def push(self, item):
            self.stack.append(item)

        # Remove the Item from the top of the Stack
        def pop(self):
            if not self.is_empty():
                return self.stack.pop()

        # Check if the stack is empty
        def is_empty(self):
            return len(self.stack) == 0

        # Return the Height (Number of Items) of the Stack
        def height(self):
            return len(self.stack)

    # Check if the stack are equal in height or not
    def find_equal_height(stack1, stack2, stack3):
        height1 = stack1.height()   # Get the height of Stack 1
        height2 = stack2.height()   # Get the height of Stack 2
        height3 = stack3.height()   # Get the height of Stack 3

        if height1 == height2 == height3:
            print("----------------------------------")
            print("The stacks are equal at height:", height1)   # If all stacks equals in height, print the height
        else:
            print("----------------------------------")
            print("The stacks are not equal at any height.")    # if the heights are not equal, print a message

    # Gets a set of elements from the user to the machine
    def get_stack_elements():
        print("----------------------------------")
        elements = input("Enter the elements of the stack (separated by space): ")
        return elements.split()


    def main():
        continue_program = True
        iteration = 1
        stack1_elements = []
        stack2_elements = []
        stack3_elements = []


        while continue_program:
            # Creating instances of a stack for Stack 1 to 3
            stack1 = Stack()
            stack2 = Stack()
            stack3 = Stack()
            
            # Get the elements from the function "get_stack_elements" to retrieved for each stack
            elements1 = get_stack_elements()
            elements2 = get_stack_elements()
            elements3 = get_stack_elements()

            stack1_elements.extend(elements1)
            stack2_elements.extend(elements2)
            stack3_elements.extend(elements3)

            #  Push each element to Stack 1-3
            for element in elements1:
                stack1.push(element)
            for element in elements2:
                stack2.push(element)
            for element in elements3:
                stack3.push(element)

            # Print the height of Stack 1-3
            print("----------------------------------")
            print("Current elements of Stack 1:", stack1_elements)
            print("Current elements of Stack 2:", stack2_elements)
            print("Current elements of Stack 3:", stack3_elements)

            # Check if the heights of each are equal using the "find_equal_height" function
            find_equal_height(stack1, stack2, stack3)

            choice = input("Enter the stack number to pop from (1, 2, 3, or ): ")
            if choice == '1':
                stack1.pop()
            elif choice == '2':
                stack2.pop()
            elif choice == '3':
                stack3.pop()
            else:
                print("Invalid choice. Please try again.")

            # Checks if the user wants to continue or not
            print("----------------------------------")
            choice = input("Do you want to continue? (Y/N): ")
            if choice.lower() == 'n':
                continue_program = False

            iteration += 1


if __name__ == "__main__":
    main()