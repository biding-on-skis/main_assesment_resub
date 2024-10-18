import time

def not_blank(question):
    error = "Please give a valid answer."
    while True:
        user_name = input(question)
        if user_name != '':
            return user_name
        else:
            print(error)

# Test for not_blank
if __name__ == "__main__":
    print("Testing not_blank function")
    name = not_blank("Enter your name: ")
    print(f"You entered a valid name: {name}")

time.sleep(15)
