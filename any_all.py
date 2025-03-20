
# https://docs.python.org/ja/3.13/library/functions.html#any
# iterable のいずれかの要素が真ならば True を返します。iterable が空なら False を返します。以下のコードと等価です:


def any(iterable):
    for element in iterable:
        if element:
            return True
    return False


# iterable の全ての要素が真ならば (もしくは iterable が空ならば) True を返します。以下のコードと等価です:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


# zip() + any() / all() を組み合わせると、リストのペアの比較などが簡単になる

a = [1, 2, 3]
b = [1, 2, 4]
print(all(x == y for x, y in zip(a, b)))  # False


# filter() と any() を組み合わせて条件を満たすか確認

numbers = [1, 2, 3, 4]
print(any(filter(lambda x: x > 3, numbers)))  # True
