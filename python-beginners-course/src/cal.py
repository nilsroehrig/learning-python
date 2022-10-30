num1 = input("First number: ")
num2 = input("Second number: ")

if not num1.isnumeric():
    print("First number is not numeric!")
    exit(1)

if not num2.isnumeric():
    print("Second number is not numeric!")
    exit(1)

total = int(num1) + int(num2)
calc = num1 + "+" + num2 + "=" + str(total)

print("Result is " + calc)
