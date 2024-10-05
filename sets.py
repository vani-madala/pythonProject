
"""set_1={78,83,True,"jenny","hello"}
set_2={78,45,67}
#print(set_1.union(set_2))
#print(set_1 | set_2)
#set_1.update([23,34,232,343,45])
#set_1.update(set_2)
#print(set_1)
set_1.update([32,45,23,4546,46,45])
print(set_1)
#set_1.intersection(set_2)
print(set_1.intersection(set_2))
set_1.intersection_update([23,43])
print(set_1)
"""
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
print(x.union(y))
x.update(y)
print(x)
print(x.intersection(y))
print(x)
x.intersection_update()
print(x)
print(x.union(["akash","jiya","jenny"]))
x.intersection_update(["akash","jiya","banana"])
print(x)