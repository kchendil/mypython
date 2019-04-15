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
