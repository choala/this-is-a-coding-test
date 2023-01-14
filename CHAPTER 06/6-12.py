n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b)

for i in range(k):
    a[i], b[n - i - 1] = b[n - i - 1], a[i]

print(sum(a))
