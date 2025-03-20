s = [int(input()) for _ in range(3)]

print( "OK" if any(s < 20 for s in s) else "NO")