n = int(input())
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direc = ['L', 'R', 'U', 'D']

x, y = 1, 1
for plan in plans:
    for i in range(len(direc)):
        if plan == direc[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x = nx
    y = ny
    
print(x, y)
