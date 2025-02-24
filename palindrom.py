n = int(input())
strings = [input() for _ in range(n)]

count = 0

for s in strings:
    for t in strings:
        if s + t == (s + t)[::-1]:
            count += 1


print(count)