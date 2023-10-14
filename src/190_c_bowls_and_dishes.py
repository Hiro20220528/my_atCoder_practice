N, M = map(int, input().split())

constranits = [list(map(int, input().split())) for _ in range(M)]

K = int(input())

choises = [list(map(int, input().split())) for _ in range(K)]

ans_max = 0
for bit in range(2**K):
    plates = [0 for _ in range(N)]
    # bitが0の時C
    # bitが1の時D
    # を選択するとする
    
    # 各桁が0 or 1か判断する
    for i in range(K):
        if (bit >> i) & 1 == 0:
            # C
            plates[choises[i][0]-1] += 1
        else:
            # D
            plates[choises[i][1]-1] += 1
        
    each_max = 0    
    # 満たされている条件を数える
    for a, b in constranits:
        if plates[a-1] > 0 and plates[b-1] > 0:
            each_max += 1
            
    ans_max = max(ans_max, each_max)
print(ans_max)