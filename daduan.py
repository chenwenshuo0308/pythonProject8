# condition = True
# while condition:
# num1 = int(input("请输入第一个数"))
# num2 = int(input("请输入第一个数"))
# num3 = int(input("请输入第一个数"))
# result = num3 + num2 * num1
# print("计算结果是：%d" % result)
# isquit = int(input("是否想要啊推出"))
# if isquit != 1:
#     condition = False


# nums = range(0, 100)
# for num in nums:
#     if num%3==0:
#         print(num)
#     else :
#         print(num/3)

# 乘法表

for number in range(1, 10):
    nums = range(1, number + 1)
    print()
    for num in nums:
        print("%d * %d = %d" % (num, number, num * number), end="\t")
