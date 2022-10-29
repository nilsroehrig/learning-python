test_list = [50, 100, "Laurence", 50, 100, True, "Hello"]
a, b, c, d, e, f, g = test_list

test_list.insert(3, "Svekis")
test_list.append("End")
test_list[0] = "New"
test_list[-2] = False

print(test_list)
# print(test_list[2])
# print(c)
# print(len(test_list))
# print(test_list[-1])
# print(test_list[-2])
# print(test_list[1:3])
# print(test_list[1:-2])
# print(test_list[:3])
# print(test_list[:-3])
# print(test_list.index("Svekis"))
# print(test_list.index(100))

val = ("Svekis" in test_list)
val2 = ("ASvekis" in test_list)
print(val, val2)

test_list.remove(100)
print(test_list)
test_list.pop()
print(test_list)
test_list.pop(3)
print(test_list)

del test_list[1]
print(test_list)

# test_list.clear()
# print(test_list)
test_list.remove(100)
test_list.remove(True)
test_list.remove(False)
test_list.append("Arnold")
print(test_list)
test_list.sort()
print(test_list)
test_list.reverse()
print(test_list)

test_list_copy = test_list.copy()
print(test_list_copy)
print("appending to new list")
test_list_copy.append("Foo")
print(test_list)
print(test_list_copy)
