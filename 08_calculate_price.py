
def calculate_price(pizza_order_size, drink_size, delivery):
    pizza_prices = {'small': 5, 'medium': 9.99, 'large': 12}
    drink_prices = {'bottle': 5, 'can': 3.30}

    # Calculate pizza cost
    pizza_cost = sum(pizza_prices[size] for size in pizza_order_size)

    # Calculate drink cost if drink_size is not 'none'
    drink_cost = 0
    if drink_size != 'none':
        drink_cost = drink_prices[drink_size]

    # Add $6 surcharge for delivery
    if delivery == "delivery":
        return pizza_cost + drink_cost + 6
    else:
        return pizza_cost + drink_cost

# Test for calculate_price
if __name__ == "__main__":
    print("Testing calculate_price function")
    pizza_sizes = input("Enter pizza sizes (comma-separated, e.g., small,medium,large): ").split(',')
    drink_size = input("Enter drink size (can, bottle, none): ").lower()
    delivery = input("Is this delivery or pick up? ").lower()

    total_cost = calculate_price(pizza_sizes, drink_size, delivery)
    print(f"Total cost for your order is: ${total_cost:.2f}")
