print("What type of toppings would you like on your pizza?")
print("Enter 'quit' when you are finished : ")

while True:
    topping = input()
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break