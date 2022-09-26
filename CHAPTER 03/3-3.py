n, m = map(int, input().split())
smallList = []

for i in range(n):
    smallest = 100
    tmp = map(int, input().split())
    smallList.append(min(tmp))

print(max(smallList))