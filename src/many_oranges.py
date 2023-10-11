A, B, W = map(int, input().split())

# W -> kgに直す
W = W * 10**3

CAN_NOT = 'UNSATISFIABLE'

"""
最小値を求める
-> できるだけBを使い残りを調整する
ex: 2000g = 150g * 13 + 1

最大値を求める
-> できるだけAを使う
ex: 2000g = 120g * 16
"""

min_g = float('inf')
max_g = 0
for i in range(10000*10**3):
          if i * A <= W and W <= i * B:
                    min_g = min(min_g, i)
                    max_g = max(max_g, i)
                    
if min_g == float('inf') or max_g == 0:
          print(CAN_NOT)
else:
          print(min_g, max_g)
