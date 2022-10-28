def fun1(val):
    print(val * val)


fun1(7)
fun1(5)
fun1(12)


def fun2(first, last):
    print("Hi, " + first + " " + last)
    return first + " " + last


fun2("Nils", "Röhrig")
fun2("Alex", "List")
fun2("John", "Doe")


def fun3(val1, val2):
    total = val1 + val2
    print(str(val1) + " + " + str(val2) + " = " + str(total))
    return total


num1 = fun3(1, 2)
num2 = fun3(3, 4)
num3 = fun3(76, 21)

print(num1, num2, num3)

myname = fun2("Karl", "Peters")
print(myname)
