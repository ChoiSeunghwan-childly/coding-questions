N, money = map(int, input().split())
coins = []
count = 0

for _ in range(N):
    coins.append(int(input()))

index = 0
for co in coins[:-1]:
    if co < money:
        index += 1
    else:
        break

for i in range(index, -1 , -1):
    if money % coins[i] != money:
        count += int(money / coins[i])
        money %= coins[i]    

print(count)