import re

def is_number(string):
    """

    Determines if a given string represents a number

    """
    try:
        int(string)
        return True
    except ValueError:
        return False
    
def peek(stack):
    """

    Peeks at the top element of a stack    

    """
    return stack[-1] if stack else None

def apply_operator(operators, values):
    """
    
    Applies an operator to the two most recent values in the values stack
    
    """
    operator = operators.pop()
    right_num = values.pop()
    left_num = values.pop()
    
    formula = "{0}{1}{2}".format(left_num, operator, right_num)
    values.append(eval(formula))

def evaluate(expression):
    """

    Evaluates a mathematical expression using the Shunting Yard Algorithm
    
    """
    tokens = re.findall("[+/*()]")