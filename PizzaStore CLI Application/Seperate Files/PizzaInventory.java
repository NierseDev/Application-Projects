import java.util.HashMap;

public class PizzaInventory {
    private HashMap<String, Integer> priceMap = new HashMap<>();
    private HashMap<String, HashMap<String, Integer>> inventoryMap = new HashMap<>();

    public void addPizza(String pizzaName, int pizzaPrice, int amount) {
        priceMap.put(pizzaName, pizzaPrice);

        HashMap<String, Integer> amountMap = new HashMap<>();
        amountMap.put(pizzaName, amount);
        inventoryMap.put(pizzaName, amountMap);
    }

    public void deletePizza(String pizzaName, int amount) {
        if (inventoryMap.containsKey(pizzaName)) {
            int currentAmount = inventoryMap.get(pizzaName).get(pizzaName);
            if (currentAmount > amount) {
                HashMap<String, Integer> amountMap = new HashMap<>();
                amountMap.put(pizzaName, currentAmount - amount);
                inventoryMap.put(pizzaName, amountMap);
            } else {
                inventoryMap.remove(pizzaName);
                priceMap.remove(pizzaName);
            }
        } else {
            System.out.println("Pizza " + pizzaName + " not found in the inventory.");
        }
    }

    public void printInventory() {
        for (String pizzaName : priceMap.keySet()) {
            int price = priceMap.get(pizzaName);
            int amount = inventoryMap.get(pizzaName).get(pizzaName);
            System.out.println("Pizza Name: " + pizzaName + ", Price: " + price + ", Amount: " + amount);
        }
    }

    public static void main(String[] args) {
        PizzaInventory inventory = new PizzaInventory();
        inventory.addPizza("Margherita", 500, 10);
        inventory.addPizza("Pepperoni", 600, 15);
        inventory.printInventory();
        inventory.deletePizza("Margherita", 5);
        inventory.printInventory();
    }
}
