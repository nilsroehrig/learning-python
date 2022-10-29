name = " Laurence Svekis "
print(name)

name_len = len(name)
print(name_len)
print("Sve" in name)
print("SDe" in name)
print("SDe" not in name)

print(name[0:5])
print(name[:5])
print(name[6:])
print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace("a", ""))
print(name.strip().replace("e", "ö").upper())
print(name.strip().split(" "))
print(" ".join(name.strip().split(" ")))
