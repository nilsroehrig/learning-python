t_dic = {"first": "value", "key": {"one": "test"}, "num": 100, "num": 200, "num": 300, "bool": True}
print(t_dic)

first = t_dic["first"]

print(first)

t_dic["first"] = "Foobar"

print(t_dic)
print(t_dic["num"])

nested = t_dic["key"]

print(nested)

nested_value = t_dic["key"]["one"]

print(nested_value)

tt_dic = t_dic.copy()
tt_dic["key"]["one"] = "BABA"  # nested dicts are copied by ref

print(t_dic)
print(tt_dic)

tt_dic.pop("first")
print(t_dic)
print(tt_dic)

tt_dic.clear()
print(tt_dic)

print(t_dic.keys())
print(t_dic.values())

tt_dic = {
    "first": 100,
    "second": "Values",
    "third": True
}

print(tt_dic)
