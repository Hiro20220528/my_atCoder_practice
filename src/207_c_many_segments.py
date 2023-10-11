N = int(input())

A = [0 for _ in range(N)]

for i in range(N):
          t, l, r = map(int, input().split())
          A[i] = [l, r, t]

A.sort()
print(A)
# for t, l, r in zip(*A):
#           print(t, l, r)