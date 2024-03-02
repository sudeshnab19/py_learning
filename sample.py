# Heterogenios + indexed + dynamic data structure 
# index = 0 to len(collection) - 1

l = ["puglu", "gablu", "gublu"]

print(l)
print(l[0])
# print(l[3]) # it will give index out of bounds error.

names = ["puglu", "gublu", "gublu", "puglu", "gublu"]
cont_gublu = 0
to_search = "gublu"
for name in names:
    if name == to_search:
        cont_gublu += 1
    else:
        continue

print(f"There are {cont_gublu} many {to_search}s")

##############################################


t = (1, [3, 4], 4)

print(t)

t[1][0] = 7

print(t)
