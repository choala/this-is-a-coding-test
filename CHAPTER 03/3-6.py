n, k = map(int, input().split())
result = 0

while True:
    # N == K 될 때까지 1씩 빼기
    target = (n // k) * k
    result += n - target
    n = target

    if n < k:
        break

    # K로 나누기
    result += 1
    n //= k

result += (n - 1)
print(result)