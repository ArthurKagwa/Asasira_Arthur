# use loops to handle inventory

products = {
    "Tundra" : 10,
    "Civic" : 5,
    "Accord" : 7,
    "Rogue" : 3,
    "CR-V" : 2,
    "Pilot" : 1,
    "RAV4" : 4,
}

# Loop through the dictionary and print each product and its quantity
def print_inventory(products):
    print("Inventory:")
    print("===================================")
    for product, quantity in products.items():
        print(f"Product: {product}, Quantity: {quantity}")

# Function to add a new product to the inventory
def add_product(products):
    print("Add a new product:")
    product_name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity: "))
    #validate the quantity
    if quantity < 0:
        print("Quantity cannot be negative.")
        return
    # Check if the product already exists
    if product_name in products:
        print(f"Product {product_name} already exists with quantity {products[product_name]}.")
        return
    # Add the new product to the inventory
    products[product_name] = quantity
    print(f"Product {product_name} added with quantity {quantity}.")
    
    
#make a sell
def sell(products):
    #display products with numbers
    print("Select a product to sell:")
    for i, product in enumerate(products.keys(), start=1):
        print(f"{i}. {product}")
    #get the product number
    product_number = int(input("Enter the product number: "))
    #validate the product number
    if product_number < 1 or product_number > len(products):
        print("Invalid product number.")
        return
    #get the product name
    product_name = list(products.keys())[product_number - 1]
    #get the quantity
    quantity = int(input("Enter the quantity: "))
    #validate the quantity
    if quantity < 0:
        print("Quantity cannot be negative.")
        return
    # Check that quantity is lee than or equal to the available quantity
    if quantity > products[product_name]:
        print(f"Not enough {product_name} in stock. Available quantity is {products[product_name]}.")
        return
    # Reduce the quantity of the product
    products[product_name] -= quantity
    print(f"Sold {quantity} {product_name}(s).")
    # Print the updated inventory
    print_inventory(products)

# Function to restock a product
def restock(products):
    print("Restock a product:")
    #display products with numbers
    print("Select a product to restock:")
    for i, product in enumerate(products.keys(), start=1):
        print(f"{i}. {product}")
    #get the product number
    product_number = int(input("Enter the product number: "))
    #validate the product number
    if product_number < 1 or product_number > len(products):
        print("Invalid product number.")
        return
    #get the product name
    product_name = list(products.keys())[product_number - 1]
    #get the quantity
    quantity = int(input("Enter the quantity: "))
    #validate the quantity
    if quantity < 0:
        print("Quantity cannot be negative.")
        return
    # Add the new product to the inventory
    products[product_name] += quantity
    print(f"Product {product_name} restocked with quantity {quantity}.")
    # Print the updated inventory
    print_inventory(products+'\n\n')

# start loop
def main():
    while True:
        print("1. Print inventory")
        print("2. Add product")
        print("3. Sell product")
        print("4. Restock product")
        print("5. Exit\n\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            print_inventory(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            sell(products)
        elif choice == "4":
            restock(products)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


main()