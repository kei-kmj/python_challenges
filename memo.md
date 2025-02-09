from main import weather

```python
# スペース区切りの一行目の入力値を取得
number, passing_score = map(int, input().split())
```

```python
# 変数で指定した行分の入力値を取得
# リスト内包表記：[式 for 変数 in イテラブル]
# num = [1, 2, 3, 4, 5]
# product_num = [n * 2 for n in num] // [2, 4, 6, 8, 10]

scores = [input() for _ in range(5)]
```

```python
# 序数を扱いながら、量を計算する
# A（開始値）と B（終了値）を持つ範囲を、下限 から 上限 の間に制限 する。
# マイナス（負の値）が発生する場合は 0 にする ことで、範囲外の計算を無効にする。
max(0, min("上限", "B") - max("下限", "A"))

# 時給計算（9時～17時の勤務時間）
start, end = [8,20]
worked_hours = max(0, min(end, 17) - max(start, 9))

# 温度管理（20度～25度の範囲）
max_temp, min_temp = [15, 30]
valid_temp = max(0, min(min_temp, 25) - max(max_temp, 20))

# 配送エリア（1000m～2000mの範囲）
min_distance, max_distance = [500, 3000]
valid_distance = max(0, min(max_distance, 2000) - max(min_distance, 1000))
```

```python
# スライス表記
# s[start:stop:step]
# start: 開始位置,デフォルトは0
# stop: 終了位置,デフォルトはリストの長さで、リストの最後の要素を含まない
# step: ステップ数,デフォルトは1
s = "abcdef"
print(s[0:6:2])  # → 'ace'  (0, 2, 4 の文字を取得)

sr = "abcdef"
print(sr[::-1])  # → 'fedcba'  (逆順)
```

```python
# next()はイテレータから次の要素を取得する

iterator = iter([10, 20])
print(next(iterator))  # → 10
print(next(iterator))  # → 20

# 値がなくなったときにデフォルト値を返す
print(next(iterator, "default"))  # → 10
print(next(iterator, "default"))  # → 20
print(next(iterator, "default"))  # → default

# 条件を満たす最初の値を取得する
numbers = [5, 12, 18, 25]
result = next(x for x in numbers if x > 10)

print(result)  # → 12
```

```python
# next()とタプルを使って、条件に合致する値を取得する
# タプルはイミュータブル
grades = [(90, "A"), (75, "B"), (60, "C")]
score = 80

# gradesをthreshold, letterに分割代入し、scoreがthreshold以上のletterを取得
grade = next(letter for threshold, letter in grades if score >= threshold)
print(grade)  # → "B"
```

```python
# divmod(m, n) は (m // n, m % n) の タプルを返す。
m, n = 10, 3
print(divmod(m, n))
```

```python
# arr.count(x) は、リスト arr に含まれる要素 x の数を返す。
weather = ["Sunny", "Sunny", "Rainy", "Sunny"]
weather.count("Rain")
```

```python
# dict.get(key, default) は、辞書 dict から key に対応する値を取得し、存在しない場合は default を返す。
text = "404"
print({"2": "ok", "4": "error"}.get(text[0], "unknown"))  # → "error"
```

```python
# %を使って、ループする数値を計算できる
# 時間計算
# 8時間前を求める
hour, minute = 16, 30
print(f"{(hour - 8) % 24}:{minute}")

# 12時間制に変換
hour = 18
print(hour % 12 or 12) 

# 曜日の計算
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
today = 3  # 水曜日
days_later = 10
print(days[(today + days_later) % 7])  # → "Sat"

# 円形リストの計算
colors = ["Red", "Green", "Blue"]
index = 5
print(colors[index % len(colors)]) # → "Green"
```
    
