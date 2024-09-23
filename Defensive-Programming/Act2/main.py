class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShopInventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product.name in self.products:
            self.products[product.name]['quantity'] += quantity
        else:
            self.products[product.name] = {'product': product, 'quantity': quantity}
    
    def subtract_from_inventory(self, product, quantity):
        if product.name in self.products:
            if self.products[product.name]['quantity'] >= quantity:
                self.products[product.name]['quantity'] -= quantity
            else:
                print("Not enough quantity in stock!")
        else:
            print("Product is not available in stock!")


class Balance:
    def __init__(self, balance):
        self.balance = balance

    def add_to_balance(self, amount):
        self.balance += amount

    def subtract_from_balance(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


class ShoppingCart:
    def __init__(self, user_balance, shop_inventory):
        self.user_balance = user_balance
        self.shop_inventory = shop_inventory
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)
    
    def list_products(self):
        if len(self.products) == 0:
            print("No products available!")
        else:
            for index, product in enumerate(self.products):
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
                self.shop_inventory.subtract_from_inventory(product, 1)
            self.products = []
            print("You have purchased the products in the cart")

def main():
    user_balance = Balance(0)
    shopping_cart = ShoppingCart(user_balance)

    # Product 1: Keyboard
    product1 = Product("Keyboard", 1399)
    shopping_cart.add_product(product1)

    # Product 2: Mouse
    product2 = Product("Mouse", 399)
    shopping_cart.add_product(product2)

    # Choose User

    # Admin (ShopInventory)

    # Customer
    print("Hello, Welcome to my store!")

    while True:
        shopping_cart.list_products()
        print("What would you like to do?")
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. List products in cart")
        print("4. Purchase products")
        print("5. Deposit to Balance")

        user_input = int(input("Enter Option No.: "))
        match user_input:
            case 1:
                input_product = input("Enter Name of Product: ")
                input_price = input("Enter the Product Price: ")

                shopping_cart.add_product()
            case 2:
                input_product = input("Enter Name of Product: ")
                shopping_cart.remove_product(Product(input_product, 0))
            case 3:
                shopping_cart.list_products()
            case 4:
                shopping_cart.purchase_products()
            case 5:
                amount = int(input("Enter Amount to Deposit: "))
                shopping_cart.user_balance.add_to_balance(amount)    
            case _:
                print("Invalid Option. Please try again!")

if __name__ == "__main__":
    main()