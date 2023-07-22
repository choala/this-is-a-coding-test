import sys
input = sys.stdin.readline

n = int(input())
direction = list(input().rstrip().split())
        
def checkRange():
    if coord[0] > 0 and coord[0] < 6 and coord[1] > 0 and coord[1] < 6:
        return True
    else:
        return False

coord = [1, 1]
for d in direction:
    if d == 'L':
        coord[1] -= 1
        if not checkRange():
            coord[1] += 1
            
    elif d == 'R':
        coord[1] += 1
        if not checkRange():
            coord[1] -= 1
            
    elif d == 'U':
        coord[0] -= 1
        if not checkRange():
            coord[0] += 1
    else:
        coord[0] += 1
        if not checkRange():
            coord[0] -= 1
        
print(coord[0], coord[1])
