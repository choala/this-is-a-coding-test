def binary_search(have, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if have[mid] == target:
        return target
    elif have[mid] < target:
        return binary_search(have, target, mid + 1, end)
    else:
        return binary_search(have, target, start, mid - 1)

n = int(input())
have = list(map(int, input().split()))
have.sort()
m = int(input())
want = list(map(int, input().split()))

for i in want:
    res = binary_search(have, i, 0, n - 1)
    if res == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
