rule = ['D', 'C', 'B', 'A', 'E']

for i in range(3):
  li = list(map(int, input().split()))
  result = sum(li)
  print(rule[result])
