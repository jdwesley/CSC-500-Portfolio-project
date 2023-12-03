#create item to purchase class and initialize item variables
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    #define total cost of an item in the cart to be called later
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
    #define item description of an item in the cart item to be called later
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


#create class shopping cart to define cart actions
class ShoppingCart:
    #initialize customer name and date variables 
    #create new list for each cart item
    def __init__(self, customer_name="none", current_date="Nov 19, 2023"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    #define add item using append function
    def add_item(self, item):
        self.cart_items.append(item)
    #define remove item that iterates over the list and uses the remove function if item name equals input item
    def remove_item(self, item):
        for i in self.cart_items:
            if i.item_name == item:
                self.cart_items.remove(i)
                return
        print("Item not found in cart. Nothing removed.")
    #define modify_item using a for loop over cart items
    def modify_item(self, item):
        for i in range(len(self.cart_items)):
            #if item in cart equals a entered item name them new values can be assinged 
            if self.cart_items[i].item_name == item.item_name:
                    self.cart_items[i] = item
                    return
            
        print("Item not found in cart. Nothing modified.")
    #define number of items in cart function and return the sum of item quantity for every item in cart
    def get_num_items_in_cart(self):
        return sum(i.item_quantity for i in self.cart_items)
    #define the cost of cart function and return the sum of item quantity * item price for every item in cart
    def get_cost_of_cart(self):
        total_cost = sum(i.item_quantity * i.item_price for i in self.cart_items)
        return total_cost
    #define print total function
    def print_total(self):
        #create instance of get cost of cart to print later
        total_cost = self.get_cost_of_cart()
        #print customer name and current dat for shopping cart output
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        #call and print number of items in cart method
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        #for loop iterates over cart items
        if self.cart_items:
            for item in self.cart_items:
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_quantity * item.item_price}")
            #print total cost using instance of get_cost_of_cart and f string
            print(f"\nTotal: ${total_cost}")
        else:
            print("SHOPPING CART IS EMPTY")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            #call print_item_description on the object item
            item.print_item_description()
            print()

#define and print the menu options
def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

#define the main function 
def main():
    #use logical if, elif operators to execute the menu options
    def execute_menu(choice, cart):
        if choice == 'a':
            #print purpose of choice
            print("ADD ITEM TO CART")
            #set variables equal to inputs
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            #call add_item function
            cart.add_item(item)
        elif choice == 'r':
            #print purpose of choice
            print("REMOVE ITEM FROM CART")
            #set variable equal to input
            item_name = input("Enter name of item to remove:\n")
            #call remove_item function
            cart.remove_item(item_name)
        elif choice == 'c':
            #print purpose of choice
            print("CHANGE ITEM QUANTITY")
            #set variables equal to input
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            item_price = float(input("Enter the item price:\n"))
            item = ItemToPurchase(item_name, item_price, new_quantity)
            #call modify_item function
            cart.modify_item(item)
        elif choice == 'i':
            print('OUTPUT ITEM DESCRIPTIONS')
            #call print_descriptions function
            cart.print_descriptions()
        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            #call print_total function
            cart.print_total()
            #if choice is q do nothing
        elif choice == 'q':
            pass
        else:
            print("Invalid option. Please try again.")

    #set variables equal in input and print strings
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}\n")
    #create instance of class ShoppingCart
    shopping_cart = ShoppingCart(customer_name, current_date)
    choice = ''
    #while loop 
    #when choice input is anything other than q call print menu and execute menu 
    while choice != 'q':
        print_menu()
        choice = input("\nChoose an option: ")
        execute_menu(choice, shopping_cart)
    #'q' breaks loop
    print('Shopping Done')
#call main function    
main()