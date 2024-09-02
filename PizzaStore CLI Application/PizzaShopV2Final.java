import java.util.Scanner;
import java.util.HashMap;

class PizzaConstuctor {
    Scanner scan = new Scanner(System.in);

    // Variables
    protected String pizzaName;
    protected int pizzaQuantity;
    protected int pizzaPrice;

    // Constructor
    public PizzaConstuctor(String pizzaName, int pizzaQuantity, int pizzaPrice) {
        this.pizzaName = pizzaName;
        this.pizzaQuantity = pizzaQuantity;
        this.pizzaPrice = pizzaPrice;
    }

    // Dictionary using HashMap Package
    // Using Static to achieve updates across child classes
    static HashMap<String, Integer> priceMap = new HashMap<>();
    static HashMap<String, HashMap<String, Integer>> inventoryMap = new HashMap<>(); // Outer Dictionary
    static HashMap<String, Integer> amountMap = new HashMap<>(); // Inner Dictionary
    static HashMap<String, Integer> cartMap = new HashMap<>();

    // Method for Initial Items to initialize Dictionary
    public void InitialItems (String pizzaName, int pizzaQuantity, int pizzaPrice) {
        priceMap.put(pizzaName, pizzaPrice);

        if (!inventoryMap.containsKey(pizzaName)) {
            inventoryMap.put(pizzaName, new HashMap<>());
        }

        inventoryMap.get(pizzaName).put(pizzaName, pizzaQuantity);
    }
    
    // Display Method
    public void CurrentInventory() { // Display Current Inventory
        System.out.println("========================================================\n");
        System.out.println("\t\t\tInventory");
        for (String pizzaName : priceMap.keySet()) {
            int pizzaPrice = priceMap.get(pizzaName);
            int pizzaQuantity = inventoryMap.get(pizzaName).get(pizzaName);

            System.out.println("\n\t\tName of Pizza: " + pizzaName + "\n\t\tQuantity of Pizza: " + pizzaQuantity + "\n\t\tPrice of Pizza: " + pizzaPrice + " PHP\n");
        }
    }

    public void CurrentCart() { // Display Current Cart
        System.out.println("========================================================\n");
        System.out.println("Current items in cart:\n");
        for (String pizzaName : cartMap.keySet()) {
            int quantity = cartMap.get(pizzaName);
            System.out.println("\t\tName of Pizza: " + pizzaName + "\n\t\tQuantity of Pizza: " + quantity + "\n");
        }
    }
}

// Pizza Stock Management System
class PizzaManager extends PizzaConstuctor {
    public PizzaManager(String pizzaName, int pizzaQuantity, int pizzaPrice) {
        super(pizzaName, pizzaQuantity, pizzaPrice);
    }

    // Inventory
    public void AppendInventory() {
        // Display
        System.out.println("========================================================\n");
        System.out.println("Name of Pizza:");
        String pizzaName = scan.next();
        System.out.println("Quantity of Pizza:");
        int quantity = scan.nextInt();
        System.out.println("Price of Pizza:");
        int pizzaPrice = scan.nextInt();
        

        // Method Usage
        if (inventoryMap.containsKey(pizzaName)) {
            int pizzaQuantity = priceMap.get(pizzaName);
            
            priceMap.put(pizzaName, pizzaQuantity + quantity);
        } else {
            priceMap.put(pizzaName, pizzaPrice);
            amountMap.put(pizzaName, quantity);
            inventoryMap.put(pizzaName, amountMap);
        }
    }

    public void DeleteInventory() {
        // Display
        System.out.println("========================================================\n");
        System.out.println("Name of Pizza:");
        String pizzaName = scan.next();


        // Method Usage
        int currentAmount = inventoryMap.get(pizzaName).get(pizzaName);
        if (currentAmount <= 0) {
            System.out.println("No " + pizzaName + " in the inventory.");
            return;
        }

        System.out.print("Enter the quantity to delete: ");
        int quantity = scan.nextInt();

        amountMap.put(pizzaName, currentAmount - quantity);
        inventoryMap.put(pizzaName, amountMap);
        System.out.println(" " + quantity + " " + pizzaName + "(s) deleted from the inventory.\n");


        // Error Handling
        if (!inventoryMap.containsKey(pizzaName)) {
            System.out.println("Pizza " + pizzaName + " not found in the inventory.");
            return;
        }

        if (quantity > currentAmount) {
            System.out.println("Not enough quantity to delete.");
            return;
        }
    }

}

// Store Management System
class PizzaStore extends PizzaConstuctor {
    public PizzaStore(String pizzaName, int pizzaQuantity, int pizzaPrice) {
        super(pizzaName, pizzaQuantity, pizzaPrice);
    }

    public void AddOrder() {
        // Display
        System.out.println("========================================================");
        System.out.println("\t\t\tMenu\n");
        for (String pizzaName : priceMap.keySet()) {
            int pizzaPrice = priceMap.get(pizzaName);

            System.out.println("\n\t\tName of Pizza: " + pizzaName + "\n\t\tPrice of Pizza: " + pizzaPrice + " PHP\n");
        }
        System.out.println("========================================================\n");
        System.out.println("Name of Pizza:");
        String pizzaName = scan.next();

        // Method Usage
        System.out.print("Enter Quantity: ");
        int quantity = scan.nextInt();

        int currentAmount = inventoryMap.get(pizzaName).get(pizzaName);
        if (currentAmount <= 0) {
            System.out.println("No more " + pizzaName + " in the inventory.");
            return;
        }

        amountMap.put(pizzaName, currentAmount - quantity);
        inventoryMap.put(pizzaName, amountMap);

        cartMap.put(pizzaName, quantity);
        System.out.println("\n " + quantity + " " + pizzaName + "(s) added to cart.\n");

        // Error Handling
        if (quantity > currentAmount) {
            System.out.println("Quanity Requested exceeds Current Amount.");
            return;
        }
    }

    public void RemoveOrder() {
        // Display
        System.out.println("========================================================\n");
        System.out.println("Name of Pizza to remove from cart:");
        String pizzaName = scan.next();
        System.out.println("Quantity to remove: ");
        int quantity = scan.nextInt();

        //Error Handling
        if (!cartMap.containsKey(pizzaName)) {
            System.out.println("Pizza " + pizzaName + " not found in the cart.");
            return;
        }

        int currentAmount = cartMap.get(pizzaName);
        if (currentAmount < quantity) {
            System.out.println("Not enough " + pizzaName + " in the cart to remove.");
            return;
        }

        // Method Usage
        // Return Pizza back to Inventory
        int currentInventoryAmount = inventoryMap.get(pizzaName).get(pizzaName);
        inventoryMap.get(pizzaName).put(pizzaName, currentInventoryAmount + quantity);

        if (currentAmount == quantity) {
            cartMap.remove(pizzaName);
        } else {
            cartMap.put(pizzaName, currentAmount - quantity);
    }

    System.out.println(" " + quantity + " " + pizzaName + "(s) removed from cart.\n");
    }

    public void Payout() {
        // Computation for Total Amount
        int total = 0;
        for (String pizzaName : cartMap.keySet()) {
            int quantity = cartMap.get(pizzaName);
            int price = priceMap.get(pizzaName);
            total += quantity * price;
        }

        // Display
        System.out.println("========================================================\n");
        System.out.println("Total cost: " + total + " PHP");

        System.out.print("Enter the amount you want to pay: ");
        int payment = scan.nextInt();

        // Error Handling and Payment Successful Message
        if (payment < total) { // Check if payment is below the cost
            System.out.println("The amount you entered is less than the total cost. Please enter a valid amount.");

        } else {
            System.out.println("\n\t\t PAYMENT SUCCESSUL!\n\t\tYour change is " + (payment - total) + " PHP.\n\n");
            cartMap.clear(); // Clear Cart
        }
    }
}

// Main Function
public class PizzaShopV2Final {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        PizzaManager pizza = new PizzaManager("None", 0, 0);
        PizzaStore pizzaOrder = new PizzaStore("None", 0, 0);
        PizzaConstuctor inventory = new PizzaConstuctor("None", 0, 0);

        // Initial Items
        inventory.InitialItems("Margherita", 30, 120);
        inventory.InitialItems("Pepperoni", 80, 210);
        inventory.InitialItems("Vegetarian", 23, 150);
        
        // Main Program
        while (true) {
            boolean run = true; // For nested while loops to return to main 'while loop'
            
            System.out.println("========================================================\n");
            System.out.println("\tHello! Welcome to the Pizza Store!");
            System.out.println("\tWhat can I do for you today?\n");
            System.out.println("1. Access Pizza Menu System");
            System.out.println("2. Access Management System");
            System.out.println("3. Exit\n");

            System.out.print("\tEnter your choice (1/2/3): ");
            int choice = scan.nextInt();
            System.out.print("\n");

            if (choice == 1) {
                while (run) {
                    System.out.println("========================================================\n");
                    System.out.println("Hello! Welcome to the Pizza Order System!\n");
                    System.out.println("What Can I do for you today?\n");
                    System.out.println("1. Add to Cart");
                    System.out.println("2. Remove from Cart");
                    System.out.println("3. View Cart");
                    System.out.println("4. Order");
                    System.out.println("5. Return\n");

                    System.out.print("\tEnter your choice (1/2/3/4): ");
                    int storeChoice = scan.nextInt();
                    System.out.print("\n");

                    switch (storeChoice) {
                        case 1:
                            pizzaOrder.AddOrder();
                            break;
                        case 2:
                            pizzaOrder.RemoveOrder();
                            break;
                        case 3:
                            pizzaOrder.CurrentCart();
                            break;
                        case 4:
                            pizzaOrder.Payout();
                            break;
                        case 5: // Return back to main 'while' loop
                            run = false;
                            break;
                        default: // Error Handling
                            System.out.println("Invalid choice.\nPlease choose 1, 2, 3, 4, or 5.");
                    }
                }
            } else if (choice == 2) {
                while (run) {
                    System.out.println("========================================================\n");
                    System.out.println("Hello! Welcome to the Pizza Store Management System!\n");
                    System.out.println("What Can I do for you today?\n");
                    System.out.println("1. Add an item to the inventory");
                    System.out.println("2. Delete an item from the inventory");
                    System.out.println("3. Show current inventory");
                    System.out.println("4. Return\n");

                    System.out.print("\tEnter your choice (1/2/3/4): ");
                    int manageChoice = scan.nextInt();
                    System.out.print("\n");

                    switch (manageChoice) {
                        case 1:
                            pizza.AppendInventory();
                            break;
                        case 2:
                            pizza.DeleteInventory();
                            break;
                        case 3:
                            pizza.CurrentInventory();
                            break;
                        case 4:
                            run = false;
                            break;
                        default:
                            System.out.println("Invalid choice.\nPlease choose 1, 2, 3, or 4.");
                    }
                }
            } else if (choice == 3) { // Exit, End Program
                System.out.println("========================================================\n");
                System.out.println("\tTHANK YOU, GOODBYE!\n");
                System.out.println("========================================================\n");
                scan.close();
                System.exit(0);
            } else { // Error Handling
                System.out.println("Invalid choice.\nPlease Choose 1, 2, or 3!");
            }
        }
    }
}
