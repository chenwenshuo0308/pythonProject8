# 输入
# inhigh = input("please input high:")
# high = float(inhigh)
# inweight = input("please input weight:")
# weight = float(inweight)
# inage = input("please input age:")
# age = float(inage)
# ingender = input("please input gender(1/0):")
# gender = float(ingender)
# # 数据处理
# if not (high > 0 and weight > 0 and age > 0 and (gender == 1 or gender == 0)):
#     print("数据不符合标准")
#     exit(0)
# # 计算体脂率
# # BMI=weight/**high
# else:
#     BMI = weight / (high * high)
#     # 体脂率=1.2BMI+0.23age-5.4-10.8*gender(男1：女0)
#     TZL = 1.2 * BMI + 0.23 * age - 5.4 - 10.8 * gender
#     # 比较阈值男性15-18%女性25-28%
#     MIN = 0.15 + 0.10 * (1 - gender)
#     MAX = 0.18 + 0.10 * (1 - gender)
#     result = MIN < TZL < MAX
#     # 输出
#     print("你的体脂率", result)

condition = True
while condition:
    print("zheshige循环")
    condition = False

notice = "打个人啥啊不过先拉"
for c in notice:
    print(c)

pet = ["cat", "dog", "pig", "wolf"]

for c in pet:
    print(c)
