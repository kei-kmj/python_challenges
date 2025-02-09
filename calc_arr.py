# 配列に含まれる値による計算処理（5種類のサンプルコード）
# 1. 配列内の合計を求める（sum）
#ポイント: sum() を使うことで 配列の合計 を簡単に取得可能

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)  # 150
print(total)

# 2. 配列内の平均値を求める
# ポイント: sum() と len() を組み合わせると 平均値 を求められる。

average = sum(numbers) / len(numbers)  # 30.0
print(average)

# 3. 配列内の最大・最小値を求める
# ポイント: max() で最大値、min() で最小値を取得可能。
max_value = max(numbers)  # 50
min_value = min(numbers)  # 10
print(max_value, min_value)

# 4. 偶数だけを抽出して合計を求める
# ポイント: リスト内包表記 を使い、偶数のみ抽出して合計。
num = [10, 21, 30, 43, 50]
even_sum = sum(n for n in num if n % 2 == 0)  # 90
print(even_sum)

