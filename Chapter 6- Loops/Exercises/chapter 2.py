print("How old are you?")
print("Enter 'quit' when you are finished.")

while True:
    persons_age = input()
    if persons_age== 'quit':
        break
    persons_age=int(persons_age)

    if persons_age < 3:
        print("  You get in free!")
    elif persons_age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")