n = int(input())

# range(n, 0, -1) は、n から 1 までの降順の数列を生成するイテラブル（range オブジェクト）を作成
arr = range(n,0,-1)

# *arr は「アンパック演算子 *」を使って range オブジェクトの要素を展開
# sep（セパレーター）は print() のオプションで、引数の間に挿入される区切り文字を指定
print(*arr, sep="\n")