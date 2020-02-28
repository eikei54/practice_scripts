x = 'abcdefg'
y = x.rstrip('efg')
print(x)
print(y)
y = x.lstrip('efg')
print(x)
print(y)
y = x.strip('efg')
print(x)
print(y)

x = 'abcdefggefgfegef'
x.rstrip('efg')
print(x)
