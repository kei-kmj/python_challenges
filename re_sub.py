import re

# 2つ以上の`-`を`-`に置換する
text = '---あ---い---う---え---お---'
print(re.sub('-{2,}', '-', text)) # -あ-い-う-え-お-

# 第1引数は置換する文字列
# 第2引数は置換後の文字列
# 第3引数は対象の文字列
# 第4引数は最大置換回数
# 第5引数はフラグ

# 第4引数を指定すると、最大置換回数を指定できる
print(re.sub('-{2,}', '-', text, 3)) # -あ-い-う-え---お---

# 第5引数に`re.IGNORECASE`を指定すると、大文字小文字を区別しない
text = 'ABCabc'
print(re.sub('A', 'A', text, flags=re.IGNORECASE)) # ABCAbc

# 第5引数に`re.IGNORECASE`を指定しないと、大文字小文字を区別する
print(re.sub('A', 'A', text)) # ABCabc
