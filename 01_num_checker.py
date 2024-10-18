import time

def num_checker(question, low, high):
    while True:
        error = f"Enter a valid option"
        try:
            user_response = int(input(question))
            if low <= user_response <= high:
                return user_response
            else:
                print(error)
        except ValueError:
            print(error)


# Test for num_checker
if __name__ == "__main__":
    print("Testing num_checker function")
    number = num_checker("Enter a number between 1 and 10: ", 1, 10)
    print(f"You entered a valid number: {number}")

time.sleep(10)