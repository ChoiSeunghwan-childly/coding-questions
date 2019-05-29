# 5585 거스름돈. (그리디)

change = 1000 - int(input())
coins = [1, 5, 10, 50, 100, 500]
index = 0
count = 0

for co in reversed(coins):
    count += int(change / co)
    change %= co

print(count)
