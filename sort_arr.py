# 配列要素の並び替え（5種類のサンプルコード）
#1.昇順ソート
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)  # [1, 2, 5, 5, 6, 9]
print(sorted_numbers)
#ポイント: 小さい順に並び替え（デフォルトの sorted()）

#2. 降順ソート
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, reverse=True)  # [9, 6, 5, 5, 2, 1]
print(sorted_numbers)
#ポイント: reverse=True を指定すると、大きい順に並ぶ。

#3. 文字列の長さでソート
words = ["banana", "apple", "cherry", "blueberry"]
sorted_words = sorted(words, key=len)  # ['apple', 'banana', 'cherry', 'blueberry']
print(sorted_words)
#ポイント: key=len で文字列の長さを基準にソート。

#4. 2D 配列のカラム（特定の列）でソート

data = [
    ["Alice", 25],
    ["Bob", 30],
    ["Charlie", 20]
]
sorted_data = sorted(data, key=lambda x: x[1])  # [['Charlie', 20], ['Alice', 25], ['Bob', 30]]
print(sorted_data)
#ポイント: key=lambda x: x[1] で2列目（年齢）を基準にソート。

#5. カスタム順序でソート
priority = {"high": 1, "medium": 2, "low": 3}

tasks = [
    ("task1", "low"),
    ("task2", "high"),
    ("task3", "medium")
]

sorted_tasks = sorted(tasks, key=lambda x: priority[x[1]])
# [('task2', 'high'), ('task3', 'medium'), ('task1', 'low')]
print(sorted_tasks)
#ポイント: key=lambda x: priority[x[1]] を使い、優先度（カスタム順）でソート。

#まとめ
#ソート方法	コード
#昇順ソート	sorted(numbers)
#降順ソート	sorted(numbers, reverse=True)
#文字列の長さ	sorted(words, key=len)
#2Dリストの特定の列でソート	sorted(data, key=lambda x: x[1])
#カスタム順序でソート	sorted(tasks, key=lambda x: priority[x[1]])