t_set = {"Svekis", 100, True, "Laurence", "Svekis", 100, True, "Laurence"}
print(t_set)

t_set.add("New")
print(t_set)

t_set.remove(100)
print(t_set)

t_set.pop()
print(t_set)

svekis_exists = ("Svekis" in t_set)
print(svekis_exists)
