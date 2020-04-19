items = {'note':1, 'notebook':2, 'sketchbook':3}
for key in items:
    #print(items[key])
    print(items.get(key))
    print(key)

hoge = { str(v) for v in range(1,10) }
print(hoge)
banana = ( str(v) for v in range(1,10) )
print(type(banana))
orange = [ str(v) for v in range(1,10) ]
print(orange)
for p in range(1,10):
    print(p)
