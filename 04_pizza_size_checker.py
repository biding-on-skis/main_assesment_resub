import time

def pizza_size_checker(pizza_size):
    if pizza_size == "small":
        return 5
    elif pizza_size == "medium":
        return 9.99
    elif pizza_size == "large":
        return 12

# Test for pizza_size_checker
if __name__ == "__main__":
    print("Testing pizza_size_checker function")
    size = input("Enter pizza size (small, medium, large): ").lower()
    cost = pizza_size_checker(size)
    print(f"The cost for a {size} pizza is: ${cost:.2f}")

time.sleep(10)