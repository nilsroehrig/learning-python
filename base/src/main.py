import pandas

# df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])
# print(df1)

# df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"])
# print(df1)

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"], index=["First", "Second"])
# print(df1.mean())
# print(df1.mean().mean())

# print(type(df1.mean()))
# print(type(df1.mean().mean()))

# print(df1.Price.mean())
# print(df1.Price.max())


# df2 = pandas.DataFrame([{"name": "John"}, {"name": "Jack"}])
# print(df2)

# df2 = pandas.DataFrame([{"name": "John", "surname": "Johnson"}, {"name": "Jack"}])
# print(df2)
