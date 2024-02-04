m = int(input("Enter rows"))
n = int(input("enter columns"))

arr = list()
for i in range(m):
    temp = list()
    for j in range(n):
        temp.append(int(input("")))
    arr.append(temp)

target = int(input("enter target value"))
flag = False
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == target:
            flag = True
            break

print(flag)



