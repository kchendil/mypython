thislist = ["apple","banana","cherry"]
print(thislist)
print(thislist[1])
thislist[1]="orange"
print(thislist)
print(thislist[1])
for x in thislist:
  print(x)
if "apple" in thislist:
  print("Yes, 'apple' is in this list")
if "banana" not in thislist:
  print("Sorry, 'banana' is not in this list")
print(len(thislist))
thislist.append("kiwi")
print(len(thislist))
thislist.insert(1,"papaya")
print(thislist)
thislist.remove("apple")
print(thislist)
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
del thislist
#print(thislist)
#thislist = ["apple","banana","cherry"]
thislist = list(("apple","banana","papaya"))
print(thislist)
thislist.clear()
print(thislist)
thislist = ["apple","banana","cherry"]
mylist = list(thislist)
print(mylist)
mylist.clear()
print(mylist)
mylist =thislist.copy() 
mylist.reverse()
print(mylist)
mylist.sort()
print(mylist)
print(mylist.index("cherry"))
print(mylist.count("apple"))
mylist.extend(thislist)
print(mylist)
