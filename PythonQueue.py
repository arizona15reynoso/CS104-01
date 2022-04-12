#Arizona Reynoso
#PythonQueue Assignment
names = []
for x in range(10):
    name= input("enter name: ")
    names.append(name)
    #names.insert(0,name)
print(names)
for x in range(10):
    print(names.pop(0))
