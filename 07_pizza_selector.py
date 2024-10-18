
def pizza_selector(pizza):
    pizza_name = "The Lot"
    pizza_cost = 9.99

    if pizza == 1:
        pizza_name = "Lamb Kebab"

    elif pizza == 2:
        pizza_name = "Crispy BBQ Pork Belly"

    elif pizza == 3:
        pizza_name = "The Lot"

    elif pizza == 4:
        pizza_name = "Chicken and bacon aoli"

    elif pizza == 5:
        pizza_name = "Smokehouse Meat lover"

    elif pizza == 6:
        pizza_name = "Peri-Peri Chicken"

    elif pizza == 7:
        pizza_name = "Philly Cheese steak"

    elif pizza == 8:
        pizza_name = "Supreme"

    elif pizza == 9:
        pizza_name = "Double Bacon Cheeseburger"

    elif pizza == 10:
        pizza_name = "Butter Chicken"

    elif pizza == 11:
        pizza_name = "BBQ Meat lovers"

    elif pizza == 12:
        pizza_name = "Chicken Supreme"

    elif pizza == 13:
        pizza_name = "Cheesy Garlic Pizza"

    elif pizza == 14:
        pizza_name = "Pepperoni"

    elif pizza == 15:
        pizza_name = "Ham Cheese"

    elif pizza == 16:
        pizza_name = "Simply Cheese"

    elif pizza == 17:
        pizza_name = "Hawaiian"

    else:
        pizza_name = "Mega Pepperoni"

    return pizza_name

# Test for pizza_selector
if __name__ == "__main__":
    print("Testing pizza_selector function")
    pizza_id = int(input("Enter pizza ID (1-18): "))
    pizza_name = pizza_selector(pizza_id)
    print(f"The pizza selected is: {pizza_name}")

