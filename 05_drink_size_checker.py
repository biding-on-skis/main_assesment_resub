import time

def drink_size_checker(drink_size):
    if drink_size == "can":
        price = 3.3
        name = "can"
    elif drink_size == "bottle":
        price = 5
        name = "bottle"

    return name, price

# Test for drink_selector
if __name__ == "__main__":
    print("Testing drink_selector function")
    drink_id = input("Enter either can or bottle: ")
    drink_name, drink_cost = drink_size_checker(drink_id)
    print(f"The drink selected is: {drink_name} with a cost of ${drink_cost:.2f}")



















