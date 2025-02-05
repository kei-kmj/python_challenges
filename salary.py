day_rate, night_rate, other_rate = map(int, input().split())
n = int(input())
work_time = [list(map(int, input().split())) for _ in range(n)]

salary = sum(
    # お仕舞が17以降の場合でも、17時までの時間を計算する
    # 始まりが9時前の場合でも、9時からの時間を計算する
    # 20時始まりなどの場合、そもそも9時から17時までの時間がないので、0となる
    max(0, min(end, 17) - max(start, 9)) * day_rate +
    max(0, min(end, 22) - max(start, 17)) * night_rate +
    max(0, min(end, 24) - max(start, 22)) * other_rate +
    max(0, min(end, 9) - max(start, 0)) * other_rate
    for start, end in work_time
)

print(salary)


