a = "test"
b = 0


def fun1(val):
    # b = b + 1
    # a = "hello"
    def fun2():
        nonlocal val
        val += 1000
        print(val)

    fun2()

    global b
    b = 1000

    print(a)


fun1(100)
print(b)
