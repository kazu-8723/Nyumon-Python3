#7-1
years_list = [1997, 1998, 1999, 2000, 2001, 2002]

#7-2
print(years_list[3])

#7-3
print(years_list[-1]) #要素の数が如何なる場合でも-1にすればリストの最後の要素を取り出せる

#7-4
things = ["mozzarella", "cinderella", "salmonella"]

#7-5
things[1] = things[1].capitalize() #書き換えるには代入しなければならない
print(things)

#7-6
things[0] = things[0].upper() #upper():全て大文字にする
print(things)

#7-7
things.remove("salmonella") # del things[-1]でも可
print(things)

#7-8
surprise = ["Groucho", "Chico", "Harpo"]

#7-9
surprise[-1] = surprise[-1].lower() #小文字化
surprise[-1] = surprise[-1][::-1] #逆順
surprise[-1] = surprise[-1].capitalize() #先頭文字の大文字化
print(surprise)

#7-10
#自分の書いたコード(通常のfor文)
even = []

for number in range(10):
    if number % 2 == 0:
        even.append(number)

print(even)

#正答例のコード(リスト内包表記)

even = [number for number in range(10) if number % 2 == 0]
print(even)

"""
可読性：
リスト内包表記 → 短くてPythonらしい書き方
通常のfor文 → 初学者や複雑な条件を扱うときに読みやすい
"""

#7-11
start1 = ["fee", "fie", "foe"]
rhymes = [("flop", "get a mop"), ("fore", "turn the rope"), ("fa", "get your ma")]
start2 = "Someone better"

start1_cap = " ".join([word.capitalize() + "!" for word in start1])
"""
[word.capitalize() + "!" for word in start1] は リスト内包表記（list comprehension）。
start1 の各 word に対して word.capitalize() を呼び、先頭を大文字にして（例: "fee" → "Fee"）、
さらに "!" をつけて "Fee!" のような新しいリスト ["Fee!", "Fie!", "Foe!"] を作ります。

" ".join(...) は、リストの要素を " "（空白1つ）でつなげて一つの文字列にします。
結果は "Fee! Fie! Foe!" という文字列になります。これが start1_cap に代入されます。
"""
for first, second in rhymes:
    print(f"{start1_cap} {first.capitalize()}!")
    """
    f"..." は f文字列（フォーマット済み文字列リテラル） です。{} の中に式を書けば評価されて文字列に埋め込まれます。
    ここでは start1_cap（例: "Fee! Fie! Foe!"）をそのまま入れ、続けて first.capitalize()（例: "Flop"）を入れ、
    最後に ! を文字として付けています。
    """
    print(F"{start2} {second}.")
    """
    f文字列 です。小文字の f でも大文字の F でも同じ働きをします（ケースは区別されません）。
    start2（例: "Someone better"）と second（例: "get a mop"）をそのまま連結して、最後にピリオド .を付けています。
    """
