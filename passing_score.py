number, passing_score = map(int, input().split())

scores = [tuple(map(int, input().split())) for _ in range(number)]

for i, (points, absent) in enumerate(scores, start=1):
    if max(points - absent * 5, 0) >= passing_score:
        print(i)