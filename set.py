thisset = {"apple","banana","cherry"}
print(thisset)
for x in thisset:
  print(x)
if "cherry" in thisset:
  print("Yes, 'cherry' is in thisset")
thisset.add("orange")
print(thisset)
thisset.update(["mango","grapes"])
print(thisset)
print(len(thisset))
thisset.remove("grapes")
print(thisset)
