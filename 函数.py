# def fuc1():
#     # 函数体
#     result = 1
#     print(result)
#
#
# fuc1()


# # 带参数函数
# def fuc2(x):
#     result = x ** 2
#     return result
#
#
# print(fuc2(2))
#
#
def mean(x, y):
    result = (x - y) ** 2
    return result


#
# # 元组参数
# def fuc3(*args):
#     result = 0
#     for v in args:
#         result += v
#     # 拆包
#     print(*args)
#     return result
#
#
# print(fuc3(1, 2, 3, 4))
#
#
# # 字典
# def fuc4(**args):
#     # result = 0
#     # for v in args:
#     #     result += v
#     result = type(args)
#     print(result)
#     return result
#
#
# fuc4(age=1, weight=3)
# # fuc4()

# def function1(a, b):
#     print(a)
#     print(b)
#
#
# def test(**args):
#     result = function1(**args)
#     print(result, type(result))
#
#     return result
#
#
# test(a=18, b=3)

# 缺省参数
# result = sorted([2, 4, 52, 6, 7, 1])
# print(result)
#
#
# # 默认参数
# def hit(person="lyh"):
#     print("我想打：%s" % person)
#
#
# hit("cws")


# def change(number):
#     number = 666
#     print(number, id(number))
#
#
# b = 10
# print(b, id(b))
# change(b)


# def hecha(x, y):
#     he = x + y
#     cha = x - y
#     return {he, cha}
#
#
# he, cha = hecha(3, 4)
# print(he, cha)

def function():
    '''这是一个三方函数
    功能，参数，返回值'''
    return 0

# 递归函数
# 阶乘
# def jiecheng(number):
#     if number == 1:
#         return 1
#     else:
#         return number * (number - 1)
#
#
# print(jiecheng(6))
