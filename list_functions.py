list_1=[11,21,212,333,443,3221,35,332]
print("the original list is",list_1)
list_1.sort()
print("the sorted list is",list_1)
list_1.reverse()
print("the reversed list is ",list_1)
print("the maximum value in the list is ",max(list_1))
print("the minimum value in the list is ",min(list_1))
print("the sum of all elements in the list is",sum(list_1))
print(list_1.count(21))
list_1.append(11)
print(list_1)
list_1.insert(2,34)
print(list_1)
list_1.extend([11,21,23,1232,2324,21,232,2121,3])
print(list_1)
list_1.remove(11)
print(list_1)
list_1.pop(2)
print(list_1)
list_1.clear()
print(list_1)


