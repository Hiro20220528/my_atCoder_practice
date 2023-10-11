N = int(input())

A = list(map(int, input().split()))

hash = {}
for num in A:
          hash[num] = hash.get(num, 0) + 1
          
max_count = 0
for key in hash.keys():
          max_count = max(max_count, hash.get(key-1, 0) + hash[key] + hash.get(key+1, 0))
          
print(max_count)