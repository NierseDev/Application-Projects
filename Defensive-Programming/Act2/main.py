class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Balance:
    def __init__(self, balance):
        self.balance = balance

    def add_to_balance(self, amount):
        self.balance += amount

    def subtract_from_balance(self, amount):
        self.balance -= amount

    def get_balance(self):
        print(f"Your current balance is: {self.balance}")
        return self.balance


class ShoppingCart:
    def __init__(self, user_balance):
        self.user_balance = user_balance
        self.products = []
    
    def add_product(self, name, price):
        self.products.append(Product(name, price))

    def remove_product(self, product, num=1):
        try:
            for _ in range(num):
                self.products.remove(product)
        except ValueError:
            print("\nProduct not found in cart. Please try again!")
    
    def list_products(self):
        if len(self.products) == 0:
            print(f"\nIn Cart:\nEmpty")
        else:
            print("\nIn Cart:")
            for index, product in enumerate(self.products, start=1):
                print(index, product.name, product.price)
    
    def purchase_products(self):
        total_price = 0
        for product in self.products:
            total_price += product.price
        if total_price > self.user_balance.get_balance():
            print("Not Enough Balance!")
        else:
            self.user_balance.subtract_from_balance(total_price)
            for product in self.products:
                self.remove_product(product, self.products.count(product))
            self.products = []
            print("You have purchased the products in the cart")

def main():
    user_balance = Balance(100)
    shopping_cart = ShoppingCart(user_balance)

    ### Debugging Code ###
    # # Product 1: Keyboard
    # product1 = Product("Keyboard", 1399)
    # shopping_cart.add_product(product1)
    # # Product 2: Mouse
    # product2 = Product("Mouse", 399)
    # shopping_cart.add_product(product2)

    # Customer Input
    print("Hello, Welcome to my store!")
    shopping_cart.list_products()

    while True:
        print("""
What would you like to do?
              
    1. Add product to cart
    2. Remove product from cart
    3. List products in cart
    4. Purchase products
    5. Deposit to Balance
    6. Check Balance
        """)

        user_input = int(input("Enter Option: "))
        match user_input:
            case 1:
                input_product = input("\nEnter Name of Product: ")
                input_price = int(input("Enter the Product Price: "))

                shopping_cart.add_product(input_product, input_price)
            case 2:
                input_product = input("\nEnter Name of Product: ")
                for product in shopping_cart.products:
                    if product.name == input_product:
                        shopping_cart.remove_product(product)
                        break
                    else:
                        print("\nProduct not found in cart. Please try again!")
            case 3:
                shopping_cart.list_products()
            case 4:
                shopping_cart.purchase_products()
            case 5:
                amount = int(input("\nEnter Amount to Deposit: "))
                shopping_cart.user_balance.add_to_balance(amount)
            case 6:
                shopping_cart.user_balance.get_balance()
            case _:
                print("Invalid Option. Please try again!")

if __name__ == "__main__":
    main()