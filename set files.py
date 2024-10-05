a={"viya","riya","priya"}
b={"vijji","priya","geetha"}
#print(a.union(b))#{'geetha', 'viya', 'vijji', 'priya', 'riya'}
#print(a.symmetric_difference(b)){'riya', 'vijji', 'geetha', 'viya'}
#a.update(b)
#print(a)#{'priya', 'viya', 'riya', 'geetha', 'vijji'}
#print(a & b)
#a.intersection_update(b)
#print(a)
print(a.union((11,23,343)))
print(a | b)
print(a & b)
print(a ^ b)
print(a - b)
print(a.isdisjoint(b))
