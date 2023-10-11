# H, W, N = map(int, input().split())

# x_list = [0 for _ in range(N)]
# y_list = [0 for _ in range(N)]


# for i in range(N):
#   A, B = map(int, input().split())
#   x_list[i] = A
#   y_list[i] = B

# # x_sort = sorted(set(x_list))
# # y_sort = sorted(set(y_list))


# xtoi = {}
# ytoi = {}
# for index, (x, y) in enumerate(zip(sorted(set(x_list)), sorted(set(y_list)))):
#   xtoi[x] = index+1
#   ytoi[y] = index+1

# for (x, y) in zip(x_list, y_list):
#   print(xtoi[x], ytoi[y])

H, W, N = map(int, input().split())

x_list = [0 for _ in range(N)]
y_list = [0 for _ in range(N)]

for i in range(N):
  A, B = map(int, input().split())
  x_list[i] = A
  y_list[i] = B

# 座標圧縮のための辞書を作成
xtoi = {x: i+1 for i, x in enumerate(sorted(set(x_list)))}
ytoi = {y: i+1 for i, y in enumerate(sorted(set(y_list)))}

for (x, y) in zip(x_list, y_list):
  print(xtoi[x], ytoi[y])
