import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
ddeok = list(map(int, sys.stdin.readline().rstrip().split()))
ddeok.sort(reverse=True)

cutter = ddeok[0]
get = 0

while get != m:
    get = 0
    cutter -= 1
    for i in ddeok:
        if i > cutter:
            get += i - cutter
    
print(cutter)
