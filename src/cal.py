num1 = input("Input first number: ")
num2 = input("Input second number: ")

if not num1.isnumeric():
    print("First number is not numeric!")
    exit(1)

if not num2.isnumeric():
    print("Second number is not numeric!")
    exit(1)

print("Result is: " + str(int(num1) + int(num2)))
