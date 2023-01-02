n = input()
direc = input().split()
coord_x = 1
coord_y = 1

for i in range(len(direc)):
    if direc[i] == "L":
        if not (coord_y - 1 < 1):
            coord_y -= 1
    if direc[i] == "R":
        if not (coord_y + 1 < n):
            coord_y += 1
    if direc[i] == "U":
        if not (coord_x - 1 < 1):
            coord_x -= 1
    if direc[i] == "D":
        if not (coord_x + 1 > n):
            coord_x += 1

print(coord_x, coord_y)
