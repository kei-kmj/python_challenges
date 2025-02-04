
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
    
