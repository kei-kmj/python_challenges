def calculate_total_distance(movements):
    """ Calculate the total movement distance from a list of coordinates. """
    total_distance = 0.0

    for i in range(1, len(movements)):
        x1, y1 = movements[i - 1][1], movements[i - 1][2]
        x2, y2 = movements[i][1], movements[i][2]
        total_distance += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(total_distance, 2)

# Example usage
movements = [
    [0, 0, 0],
    [1, 3, 4],
    [2, 6, 8],
    [3, 7, 8]
]

print(calculate_total_distance(movements))  # 10.00