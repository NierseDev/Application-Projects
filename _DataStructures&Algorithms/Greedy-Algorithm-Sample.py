def calculate_change(total_cost, amount_given):
    # Define the denominations
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05]
    
    # Calculate the total change
    change = amount_given - total_cost
    fChange = round(change, 2)

    # Check if the amount given is less than the total cost
    if change < 0:
        return "The amount given is less than the total cost."
    
    # Create a dictionary to hold the count of each denomination
    change_count = {denomination: 0 for denomination in denominations}
    
    # Calculate the minimum number of bills and coins
    for denomination in denominations:
        if change >= denomination:
            count = change // denomination
            change_count[denomination] = int(count)
            change -= denomination * count
    
    return f"{change_count} = {fChange}"

# Test the function
# By taking user input
test = int(input("Enter the number of test cases: "))
print(f"Number of test cases: {test}")
for i in range(test):
    tCost = float(input("Enter the total cost: "))
    gAmount = float(input("Enter the amount given: "))
    print(f"Total Cost: {tCost} \t| Amount Given: {gAmount}")
    print(calculate_change(tCost, gAmount), "\n")

# # Test the function
# # By Opening an Input Text File containing Test Inputs
# with open('input.txt', 'r') as f:
#     test = int(f.readline())
#     print(f"Number of test cases: {test}")
#     for i in range(test):
#         tCost, gAmount = map(float, f.readline().strip().split())
#         print(f"Total Cost: {tCost} \t| Amount Given: {gAmount}")
#         print(calculate_change(tCost, gAmount), "\n")