import java.util.HashMap;//importing Hashmap
import java.util.Map;// importing dictionary 
import java.util.Scanner;

public class pizzaShop {
    public static void main(String[] args) {
        Map<String, Integer> inventory = new HashMap<>(); // Initialize the inventory

        // Initial inventory setup
        inventory.put("Margherita", 10);
        inventory.put("Pepperoni", 8);
        inventory.put("Vegetarian", 12);

        Scanner scanner = new Scanner(System.in);

        while (true) {
			System.out.println("\n\t\t\t\t--------------------------------------------------------");
            System.out.println("\t\t\t\tHello! Welcome to the Pizza Store Management System!\n");
            System.out.println("\t\t\t\tWhat Can I do for you today?\n");
            System.out.println("\t\t\t\t1. Add an item to the inventory");
            System.out.println("\t\t\t\t2. Delete an item from the inventory");
            System.out.println("\t\t\t\t3. Show current inventory");
            System.out.println("\t\t\t\t4. Exit\n");

            System.out.print("\t\t\t\tEnter your choice (1/2/3/4): ");
            int choice = scanner.nextInt();


            switch (choice) {
                case 1:
                    addItemToInventory(inventory, scanner);
                    break;
                case 2:
                    deleteItemFromInventory(inventory, scanner);
                    break;
                case 3:
                    showInventory(inventory);
                    break;
                case 4:
					System.out.println("\t\t\t\t--------------------------------------------------------\n");
                    System.out.println("\t\t\t\tThank you, Goodbye!");
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("\n\t\t\t\tInvalid choice. Please choose 1, 2, 3, or 4.");
            }
        }
    }

    private static void addItemToInventory(Map<String, Integer> inventory, Scanner scanner) {
        System.out.println("\t\t\t\t--------------------------------------------------------\n");
		System.out.print("\t\t\t\tEnter the name of the pizza: ");
        String pizzaName = scanner.next();
		System.out.println("\t\t\t\t--------------------------------------------------------\n");
        System.out.print("\t\t\t\tEnter the quantity to add: ");
        int quantity = scanner.nextInt(); // Adding Item and asking how many Quantity

        if (inventory.containsKey(pizzaName)) {
            int currentQuantity = inventory.get(pizzaName);
            inventory.put(pizzaName, currentQuantity + quantity);
        } else {
            inventory.put(pizzaName, quantity);
        }

        System.out.println("\t\t\t\t" + " " + quantity + " " + pizzaName + "(s) added to the inventory.");
    }

    private static void deleteItemFromInventory(Map<String, Integer> inventory, Scanner scanner) {
		System.out.println("\t\t\t\t--------------------------------------------------------");	
        System.out.print("\n\t\t\t\tEnter the name of the pizza to delete: "); // Deleting Items from inventory...
        String pizzaName = scanner.next();

        if (inventory.containsKey(pizzaName)) {
            int currentQuantity = inventory.get(pizzaName);
            if (currentQuantity > 0) {
                System.out.print("\n\t\t\t\tEnter the quantity to delete: ");
                int quantity = scanner.nextInt();
                if (quantity <= currentQuantity) {
                    inventory.put(pizzaName, currentQuantity - quantity);
                    System.out.println("\n\t\t\t\t " + quantity + " " + pizzaName + "(s) deleted from the inventory.");
                } else {
                    System.out.println("\n\t\t\t\tNot enough quantity to delete.");
                }
            } else {
                System.out.println("\n\t\t\t\tNo " + pizzaName + " in the inventory.");
            }
        } else {
            System.out.println("\n\t\t\t\tI am Sorry but " + pizzaName + " is not found in the inventory.");
        }
    }

    private static void showInventory(Map<String, Integer> inventory) { // Showing the current/updated inventory
	System.out.println("\t\t\t\t--------------------------------------------------------");	
        System.out.println("\n\t\t\t\tCurrent Inventory:");
        for (String pizza : inventory.keySet()) {
            int quantity = inventory.get(pizza);
            System.out.println("\t\t\t\t" + " " + pizza + ": " + quantity);
        }
    }
}
