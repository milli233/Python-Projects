## First non repeating character

s = input().strip()

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

result = -1
for ch in s:
    if freq[ch] == 1:
        result = ch
        break

print(result)


## find the second largest unique number

arr = list(map(int, input().split()))

unique = list(set(arr))   # duplicates removed

if len(unique) < 2:
    print(-1)
else:
    unique.sort(reverse=True)
    print(unique[1])

### without sorting

arr = list(map(int, input().split()))

largest = float('-inf')     #self initialization
second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif second < num < largest:
        second = num

if second == float('-inf'):
    print(-1)
else:
    print(second)

##
