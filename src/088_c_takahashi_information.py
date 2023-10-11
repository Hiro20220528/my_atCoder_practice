A = [list(map(int, input().split())) for _ in range(3)]


sum_row = 0
for row in A:
          sum_row += sum(row)
          
if sum_row % 3 == 0 and sum_row // 3 == A[0][0] + A[1][1] + A[2][2]:
          if sum_row // 3 == A[0][2] + A[1][1] + A[2][0]:
                    print('Yes')
          else:
                    print('No')
else:
          print('No')