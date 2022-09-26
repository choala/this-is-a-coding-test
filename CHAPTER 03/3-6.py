n, k = map(int, input().split())
result = 0

while True:
    # N이 K의 배수가 되도록 효율적으로 한 번에 빼기
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