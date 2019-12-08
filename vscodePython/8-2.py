import mod1

print(mod1.add(3, 4))
print(mod1.sub(4, 2))


from mod1 import add
print(add(3, 4))


import mod1 as m
print(add(4, 5))


