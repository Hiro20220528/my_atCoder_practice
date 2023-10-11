# 解法
"""
1. 全部 W にする
2. 全部 R もしくは右端以外 R にする
3. 左 R | 右 W に並び替える
"""
import math

N = int(input())
S = input()

stones = list(S)

# print(stones)
r_count = 0
w_count = 0

for i, stone in enumerate(stones):
    if stone == 'R':
        r_count += 1
    else:
        w_count += 1

# print(r_count, w_count)

w_part = 0
for i in range(r_count):
    part = stones[i]
    # print(part)
    if part == 'W':
        w_part += 1

print(w_part)
    
        


    
