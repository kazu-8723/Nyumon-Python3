#6-1
for x in [3, 2, 1, 0]:
    print(x)

#6-2
guess_me = 7
number = 1

# 自分で書いたコード
while number < guess_me:
    print("too low")
    number += 1
    if number == guess_me:
        print("found it")
        break
    elif number > guess_me:
        print("oops")
        break

"""
ループ条件は number < guess_me。
→ 最初から number >= guess_me なら、ループに入らずに一度も実行されません。
number が guess_me に達した時点で break して終了します。
実質的には number が guess_me に追いついたところで終了するループ。
1度も判定されない可能性もあるのでよろしくない。
"""
# 正答例のコード
while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it")
        break
    elif number > guess_me:
        print("oops")
        break
    number += 1

"""
ループ条件は常に True。終了は必ず break で行う。
number >= guess_me の状態から始まっても、必ず一度は if 判定に入ります（その後に break で終わる）。
"""

"""
開始条件の違い

1つ目: number >= guess_me なら一度も実行されない。
2つ目: number >= guess_me でも必ず1回実行される。

コードの見通し

1つ目は「ループ条件が事前に分かっている場合」向き。
2つ目は「必ず一度実行したい」場合や「終了条件をすべて if で書きたい」場合に向いている。

出力の違い例

guess_me = 7
number = 7

1つ目 → ループ条件が偽なので何も出力されず終了。
2つ目 → 「found it」が1回出力されて終了。
"""

#6-3
guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it")
        break
    elif number > guess_me:
        print("oops")
        break

