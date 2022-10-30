testList = ["Laurence", "Hello", "World", 55, 100, True]

for item in testList:
    print(item)

myStr = "Hello World"

for letter in myStr:
    if letter == "l":
        continue
    if letter == "x":
        break

    print(letter)
else:
    print("Word done")

testDic = {
    "first": "Laurence",
    "last": "Svekis",
    "allowed": True
}

for key in testDic.keys():
    print(key + ":" + str(testDic[key]))

for value in testDic.values():
    print(value)

for pair in testDic.items():
    print(pair)

for key,value in testDic.items():
    print(key, value)