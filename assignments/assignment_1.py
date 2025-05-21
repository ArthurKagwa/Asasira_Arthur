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