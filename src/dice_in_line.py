N, K = map(int, input().split())

P = list(map(int, input().split()))

ans = 0
h = [(1+i)/2 for i in P]

# print(h)

e = 0
for i in range(N):
# for i in range(N+1 - K):
          # print(i)
          e += h[i]
          if i+1 >= K:
                    ans = max(ans, e)
                    # print(ans)
                    e -= h[i+1 - K]
          
print(ans)