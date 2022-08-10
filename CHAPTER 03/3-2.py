n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

biggest_1 = data[n - 1]
biggest_2 = data[n - 2]

sum = biggest_1 * k * (m // k) + biggest_2 * (m % k)

print(sum)