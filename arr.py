from operator import index

# 配列全体の合計
numbers = [10, 21, 30, 43, 50]
total = sum(numbers)  # 150
print(total)

# 条件付きの合計
# インデックスが奇数の時のみ足す
odd_index_sum = sum(num for i, num in enumerate(numbers) if i % 2 == 1)
print(odd_index_sum)


# 3. 二次元配列（行ごとの合計）
# 各行ごとの合計を求める リスト内包表記。
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sums = [sum(row) for row in matrix]
print(row_sums)

# インデックス毎の合計
# zip(*lists) を使い、列ごとの合計 を求める。
lists = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
index_sums = [sum(values) for values in zip(*lists)]  # [120, 150, 180]
print(index_sums)