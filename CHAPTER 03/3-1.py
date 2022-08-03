n = 1260
coin_type = [500, 100, 50, 10]
coin_cnt = 0;

for coin in coin_type:
  coin_cnt += n // coin
  n = n % coin

print(coin_cnt)