H, W = map(int, input().split())


grid  = [input().split() for _ in range(H)]


flag = True
for i in range(H):
          if flag == False:
                    break
          for j in range(W):
                    
                    m = grid[i][0][j]
                    # print(m)
                    if m == '#':
                              try:
                                        l = grid[i][0][j-1]
                              except:
                                        l = '.'
                                        pass
                              try:
                                        
                                        r = grid[i][0][j+1]
                              except:
                                        r = '.'
                                        pass
                              try:
                                        u = '.'
                                        u = grid[i-1][0][j]
                              except:
                                        pass
                              try:
                                        d = '.'
                                        d = grid[i+1][0][j]
                              except:
                                        pass
                              finally:
                                        if l == '.' and r =='.' and u =='.' and d == '.':
                                                  flag = False
                                                  break
                    
                    
if flag:                
          print("Yes")  
else:
          print("No")          
                    
                    