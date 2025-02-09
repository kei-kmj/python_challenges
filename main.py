students1 = [
  ["Alice", 80, 90, 70],
  ["Bob", 60, 85, 90],
  ["Charlie", 80, 60, 75],
  ["David", 85, 75, 80],
  ["Eve", 90, 80, 85]
]

# 行と列を入れ替える
transposed = list(map(list, zip(*students1)))

for row in transposed:
    print(row)

