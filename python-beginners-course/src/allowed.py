userInput = input("How old are you?: ")
print("Thanks, I'm checking")

if not userInput.isnumeric():
    print("Invalid input, please provide your age!")
else:
    age = int(userInput)
    if age >= 21:
        print("Welcome, have a drink!")
    elif age >= 18:
        print("Welcome, have a soda!")
    else:
        print("Du kommst hier net rein!")
