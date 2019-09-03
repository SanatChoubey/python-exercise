lists = [12,23,44,55,66]
lists[1]=0

print(lists[::-1])
print(list(range(0,20)))
#add
lists.append(99)
lists.insert(0,122)

#remove
lists.pop(0)
print(lists)
if 12 in lists:
     print(lists.index(12))




#sort and lambda function
data = [
     ("product1",12),
     ("product2",52),
     ("product3",42),
] 
def sort_data(item):
     return item[1]
data.sort(key=lambda item:item[1])    
print(data)

#map function on list 
datafor_map = [
     ("product1",12),
     ("product2",52),
     ("product3",42), 
]
x= map(lambda item:item[1],datafor_map)
for item in x:
     print(item)

     