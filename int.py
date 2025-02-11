from collections import deque


def min_operations_to_one(N):
    """ 最小回数で N を 1 にする操作回数を求める """
    queue = deque([(N, 0)])  # (現在の数, 操作回数)
    visited = set()  # すでに訪れた数を記録

    while queue:
        num, steps = queue.popleft()

        if num == 1:
            return steps

        if num in visited:
            continue
        visited.add(num)

        # 偶数なら割る
        if num % 2 == 0:
            queue.append((num // 2, steps + 1))
        else:
            # 奇数なら +1 or -1
            queue.append((num + 1, steps + 1))
            queue.append((num - 1, steps + 1))


# Example usage
print(min_operations_to_one(15))  # 5
print(min_operations_to_one(8))  # 3
print(min_operations_to_one(1023))  # 10