print("p12")

# 絕對不行, 不同類型
# print(" 數字:" + 3.14)
# 帶入多個參數
print("數字:", 3.14)

# print("parint("數字:", 3.14)") 為什麼不能這樣寫？
print("可以得到 數字：3.14")

#  先定義 a
a =100


# abs 有回傳值, 我們可以直接用舊名字 a 來接他
a = abs(-2 * a)
print("絕對值:", a)


# pow 需要兩個參數, 兩個參數之間我們用逗號隔開
a = pow(a, 2)
print("次方運算:", a)


# bmi: (體重)/(身高公尺)^2
# 其實也可以使用 ** 來做次方
bmi = 75 / pow(1.75, 2)
print("BMI:", bmi)


# 四捨五入到小數第二位
bmi = 75 / (1.75 ** 2)
print("BMI(四捨五入到小數第二位):", round(bmi, 2))

# 這裡初學者不用練習,當要使用精確運算的話,我們會使用 Decimal 但事實上,使用時機非常非常少,大概只有計算機 APP 需要
from decimal import *
print(Decimal("3.14") + Decimal("3"))

print("p14")
b = "hello"
print("原本:", b)
b = b + " fat pig"
print("串連:", b)
print("長度:", len(b))

# 記得座號從 0 開始
# [座號] -> 拿到背後的字
c = "hello python"
print("第三個字:", c[2])

# 利用反向座號直接拿最後一個字, 就不用寫 a[len(a) - 1] 了
print("最後一個字:", c[-1])

# 也可以拿某一個字到某一個字
# 要記得第二個數字要多 +1
print("第三個字-第七個字:", c[2:7])

print("p15")
a = "hello python"

# 2->4->6->8
print(a[2:9:2])

# 如果前面什麼都不寫代表從頭, 後面什麼都不寫代表尾巴
print(a[:])
print("這個不懂")

# 從頭到尾, 並且三個一拿
print(a[::3])

print("第一行\n第二行")
print("L\nO\nV\nE")

print("p15的參考網址不能用")

print("p16")

# 先準備一個字串
a = "hellohellohello"

# 使用 replace(取代的專屬技能)
b = a.replace("hello", "goodbye")

# 這裡要稍微注意, 你會發現 a 並沒有變動, 而是回傳一個新的答案
print("原本的沒改變:", a)
print("回傳新的答案:", b)

# 所以如果你要 a 後面換成新的可以這樣寫 a = a.replace
# replace 如果帶入第三個參數的話可以指定只取代幾個
a = a.replace("hello", "goodbye", 2)
print("設定回去:", a)

print("練習")
# 先準備一個字串
a = "PigPigPig"

# 使用 replace(取代的專屬技能)
b = a.replace("Pig", "Love")

# 這裡要稍微注意, 你會發現 a 並沒有變動, 而是回傳一個新的答案
print("豬豬豬:", a)
print("愛愛愛:", b)

# 所以如果你要 a 後面換成新的可以這樣寫 a = a.replace
# replace 如果帶入第三個參數的話可以指定只取代幾個
a = a.replace("Pig", "Love", 1)
print("最愛豬豬:", a)


# 再來練習兩個大小寫的轉換:
# 1. upper: 轉成大寫
# 2. lower: 轉成小寫

# 這裡要注意, 由於他已經知道自己的所有東西, 所有不需參數
print("轉成大寫", "pig".upper())
print("轉成小寫", "PIG".lower())

print("p17")

# 直接使用 True False
print("直接使用:", True)

# 數字運算產生布林
print("大於:", 5 > 3)
print("相等:", 2 == 2)

# 文字運算產生布林 (要記得大寫小寫是完全不同的)
print("文字相等:", "hello" == "HELLO")
print("文字包含:", "hel" in "hello")

print("p18")

print("and 結合:", True and False)
print("or 結合:", True or False)

# 請運用你對運算子的天然直覺
print("複雜結合:", 5 >= 3 + 2 and True)

print("這段不懂")


