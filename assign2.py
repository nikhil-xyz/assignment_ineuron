from collections import Counter

string = str(input("enter string line"))
print(string)
arr = string.split(" ")

freq = Counter(arr)
sorted = list(sorted(freq.items(), key=lambda kv: kv[1]))
print(sorted)
ele = sorted[len(sorted)-1]
print(len(ele[0]))
