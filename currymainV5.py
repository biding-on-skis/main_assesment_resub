import time
import pandas as pd


# checks if numbers entered
def num_checker(question, low, high):
    while True:
        error = "Please Enter A Valid Phone Number"
        try:
            user_response = int(input(question))
            if low <= user_response <= high:
                return user_response
            else:
                print(error)
        except ValueError:
            print(error)


# allows for single letter input
def string_checker(question, valid_ans):
    error = f"Enter a valid option from {valid_ans}"
    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response or user_response == item[0]:
                return item
        print(error)


# doesn't allow for blank response
def not_blank(question):
    error = "Please give a valid answer."
    while True:
        user_name = input(question)
        if user_name != '':
            return user_name
        else:
            print(error)


# checks for size of curry (small medium large)
def curry_size_checker(curry_size):
    if curry_size == "small":
        return 10
    elif curry_size == "medium":
        return 15
    else:
        return 20


# checks for size of drink (can bottle)
def drink_size_checker(drink_size_check):
    if drink_size_check == "can":
        return 3.3
    else:
        return 5


# checks number and displays corresponding flavour
def curry_selector(curry):
    curry_names = {
        1: "Chicken Tikka Masala",
        2: "Korma",
        3: "Rogan Josh",
        4: "Butter Chicken",
        5: "Madras",
        6: "Chicken Curry",
        7: "Chana Masala",
        8: "Palak Paneer",
        9: "Vindaloo",
        10: "Dhansak",
        11: "Goan Curry",
        12: "Jalfrezi",
        13: "Malai Kofta",
        14: "Rogan Josh",
        15: "Saag Aloo",
        16: "Tandoori Chicken",
        17: "Navratan Korma",
        18: "Lamb Curry"
    }
    return curry_names.get(curry, "Unknown Curry")


# checks integer input and displays corresponding flavour
def drink_selector(drink, select_drink_size):
    drink_names = {
        1: "Coke",
        2: "Fanta",
        3: "Lift",
        4: "Sprite",
        5: "Coke Zero",
        6: "L & P"
    }
    drink_name_select = drink_names.get(drink, "Unknown Drink")
    drink_cost_select = drink_size_checker(select_drink_size)
    return drink_name_select, drink_cost_select


# adds together all sizes and prices of items ordered and displays calculated price at end of code
def calculate_price(curry_order_size_calc, drink_size_calc, delivery_calc):
    curry_prices = {'small': 10, 'medium': 15, 'large': 20}
    drink_prices = {'bottle': 5, 'can': 3.30}

    # Calculate curry cost
    curry_cost = sum(curry_prices[size_1] for size_1 in curry_order_size_calc)

    # Calculate drink cost if drink_size is not 'none'
    drink_cost_calc = 0
    if drink_size_calc != 'none':
        drink_cost_calc = drink_prices[drink_size]

    # Add $6 surcharge for delivery
    if delivery_calc == "delivery":
        return curry_cost + drink_cost_calc + 6
    else:
        return curry_cost + drink_cost_calc


# set maximum number of tickets below
MAX_CURRY = 10

# Variables
yes_no = ["yes", "no"]
delivery_option = ["delivery", "pick up"]
size_option = ["large", "medium", "small"]
size_drink = ["can", "bottle"]

curry_order = []
curry_order_size = []
ordered_curries = []
drink_order = []
ordered_drinks = []  # Initialize list to hold d    rink names
drink_size = 'none'  # Initialize with a placeholder value
address = ""  # Initialize address with a default value

keep_going = "yes"

while keep_going == "yes":
    # Welcome message
    print("<---Welcome to Curry Haven--->")
    print()

    # Instructions question
    want_instruc = string_checker("Would you like to read the instructions: ", yes_no)

    if want_instruc == "yes":
        print('''        
    |-----Instructions-----|
    -When answering a question you can put the first letter of
     the word and it will go through as correct

    -The code will ask for your name, phone number, address (if clicked delivery), 
     curry flavour, size, drink and drink size.
        ''')

    delivery = string_checker("Is this order pick up or delivery? ", delivery_option)

    if delivery == "delivery":
        print("There is a $6 surcharge for delivery")

        # Ask for name and details
        print()
        name = not_blank("Enter your name: ")

        # Ask for phone number
        print()
        phone_num = num_checker("Enter your phone number: ", 10000000, 99999999999)

        # Ask for address
        print()
        address = not_blank("Enter your address: ")

    else:
        # Ask for name and details
        name = not_blank("Enter your name: ")
        # Ask for phone number
        phone_num = num_checker("Enter your phone number: ", 9999999, 99999999999)

    # Time wait
    time.sleep(.5)

    # Do you want the Menu?
    print()
    want_menu = string_checker(f"Hello {name}, would you like the curry menu? ", yes_no)

    if want_menu == "yes":

        # Set display options for pandas
        all_names = ["Chicken Tikka Masala", "Korma", "Rogan Josh", "Butter Chicken",
                     "Madras", "Chicken Curry", "Chana Masala", "Palak Paneer",
                     "Vindaloo", "Dhansak", "Goan Curry", "Jalfrezi",
                     "Malai Kofta", "Duck Curry", "Saag Aloo", "Tandoori Chicken",
                     "Navratan Korma", "Lamb Curry"]

        all_small_size = [6] * len(all_names)
        all_medium_size = [10.99] * len(all_names)
        all_large_size = [14] * len(all_names)

        df = pd.DataFrame({
            'Name': all_names,
            'Small Size Cost': all_small_size,
            'Medium Size Cost': all_medium_size,
            'Large Size Cost': all_large_size
        })

        pd.set_option('display.max_columns', None)  # Show all columns
        pd.set_option('display.expand_frame_repr', False)  # Prevent wrapping
        pd.set_option('display.max_rows', None)  # Show all rows, if needed

        # Set index to start from 1
        df.index = range(1, len(df) + 1)

        print(df)

    add_to_order = "yes"

    # While loop for user to keep adding to their curry order
    while add_to_order == "yes":
        # Curry id question
        curry_num_id = num_checker("Enter the curry number: ", 1, 18)
        curry_order.append(curry_num_id)

        # Ask for size
        size = string_checker("What Size | Small | Medium | Large |: ", size_option)
        curry_order_size.append(size)

        user_curry_selection = curry_selector(curry_num_id)
        user_curry_cost = curry_size_checker(size)

        print(f"Great! You have selected a {user_curry_selection}:  ${user_curry_cost}")

        # Add to the ordered curries list
        ordered_curries.append(user_curry_selection)

        print()
        add_to_order = string_checker("Do you want to order another curry? ", yes_no)

    # After the loop, print all ordered curries
    print(f"You have ordered the following: {', '.join(ordered_curries)} with the sizes: {curry_order_size}")

    # Price summary for food
    total_price = calculate_price(curry_order_size, 'none', delivery)  # Use 'none' for initial calculation
    print(f"Your order so far costs = ${total_price:.2f} (including delivery)")

    # Time wait
    time.sleep(1)

    # Would you like the drink menu question
    want_menu = string_checker(f"{name}, would you like the drink menu? ", yes_no)

    if want_menu == "yes":
        # Set display options for pandas
        all_names = ["Coke", "Fanta", "Lift", "Sprite", "Coke Zero", "L & P"]

        all_Can_size = [3.3] * len(all_names)
        all_Bottle_size = [5] * len(all_names)

        df = pd.DataFrame({
            'Name': all_names,
            'Bottle (1.5L) Size Cost': all_Bottle_size,
            'Can (330mL) Cost': all_Can_size,
        })

        pd.set_option('display.max_columns', None)  # Show all columns
        pd.set_option('display.expand_frame_repr', False)  # Prevent wrapping
        pd.set_option('display.max_rows', None)  # Show all rows, if needed

        # Set index to start from 1
        df.index = range(1, len(df) + 1)

        print(df)

        add_drinks = "yes"

        # While loop for user to keep adding to their drink order
        while add_drinks == "yes":
            # Drink selection question
            drink_num_id = num_checker("Enter the drink number:", 1, 6)
            drink_size = string_checker("What Size | Bottle (1.5L) | Can (330mL) |: ", size_drink)

            # Fetch drink name and cost using the selector function
            drink_name, drink_cost = drink_selector(drink_num_id, drink_size)

            print(f"Great! You have selected a {drink_name} ({drink_size})")

            # Add drink to order
            drink_order.append(drink_num_id)
            ordered_drinks.append(drink_name)  # Add drink name to ordered drinks list

            # loop question yes/no
            add_drinks = string_checker("Do you want to order another drink? ", yes_no)

        # After finishing drink orders, display all selected drinks
        print(f"You have ordered the following drinks: {', '.join(ordered_drinks)}")

    # Confirmation code
    want_confirmation = string_checker("Would you like to confirm your order: ", yes_no)

    if want_confirmation != "yes":
        print("Your Order has been Canceled")
        curry_order.clear()
        curry_order_size.clear()
        ordered_curries.clear()
        ordered_drinks.clear()
        time.sleep(1)
    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        pass

    # Order price calculator (including drink if selected)
        total_price = calculate_price(curry_order_size, drink_size, delivery)

        # Set display options for pandas
        all_names = ["Total Price:", "Name:", "Order:", "Drink Order:", "Phone Number:", "Address:"]

        # Use join to list all ordered curries and drinks
        all_Detail_size = [
            f"${total_price}",
            f"{name}",
            f"{', '.join(ordered_curries)}",
            f"{', '.join(ordered_drinks)}",  # Update this line to show all drinks
            f"{phone_num}",
            f"{address}"
        ]

        df = pd.DataFrame({
            'Titles': all_names,
            'Details': all_Detail_size,
        })

        pd.set_option('display.max_columns', None)  # Show all columns
        pd.set_option('display.expand_frame_repr', False)  # Prevent wrapping
        pd.set_option('display.max_rows', None)  # Show all rows, if needed

        # Set index to start from 1
        df.index = range(1, len(df) + 1)

        print(df)
        # Time wait
        time.sleep(2)

        # Ready message
        print("Your curry will be ready from 10 to 20 minutes")

    keep_going = string_checker("Would you like place another order? (yes/no): ", yes_no)

    if keep_going == "yes":
        curry_order.clear()
        curry_order_size.clear()
        ordered_curries.clear()
        drink_order.clear()
        ordered_drinks.clear()
    else:
        pass

    print("Thank you for ordering with Curry Haven")
