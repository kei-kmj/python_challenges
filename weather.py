a = int(input())

weather = next(value for threshold, value in [(71, "rainy"), (31, "cloudy"), (0, "sunny")] if a >= threshold)

print(weather)