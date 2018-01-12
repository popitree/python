shoppingList = ["milk", "pasta", "eggs", "bread", "rice"]
for item in shoppingList:
    if item == 'bread':
        print("<<ignore "+item)
        continue
    print(item)

print("------------")
for item in shoppingList:
    if item == 'bread':
        print("stop at "+item)
        stop_at = item  #better to declare earlier else if stopat : will give error
        break
    print(item)
print("------------")
if stop_at:
    print("\nstopped at::"+stop_at)
print("------------")

#else can follow if and for both
nums = [1,2,3,5]
for i in nums:
    if i == 4:
        continue
else:   #else in this location will be executed only if code not came to break "wont work for continue"
    print('Testing')