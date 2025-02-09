
def sum_of_min_in_rows(numbers):
    return sum(min(row) for row in numbers)


num = [
    [987654, 123456, 654321],
    [234567, 876543, 345678],
    [567890, 678901, 789012]
]

print(sum_of_min_in_rows(num))