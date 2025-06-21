# Tuples

# We can't modify a tuple

names = ("Tushar","Rishi",'zz last index -1')

print(names[-1])
print(names.index("Tushar"))

print(len(names))

print("Shyam" in names)

print(names[0:2])

print(sorted(names))

new_names = names + ("Adam","Crish","Robin")

print(sorted(new_names))