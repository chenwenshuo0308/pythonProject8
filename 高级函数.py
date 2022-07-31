# 偏函数
# import functools
#
#
# def test(a, b, c, d):
#     print(a + b + c + d)
#
#
# test(1, 2, 3, 4)
#
# newfunction = functools.partial(test, c=4)
# print(type(newfunction))
# newfunction(a=1, b=3, d=5)
# 高阶函数
# l = [{"name": "cws", "age": 18}, {"name": "crrs", "age": 29}, {"name": "fgj", "age": 19}, {"name": "drh", "age": 28}]
#
#
# def getKey(x):
#     return x["age"]
#
#
# result = sorted(l, key=getKey)
# print(result)


# 返回函数
# def func(flag):
#     '''
#
#     :return: 返回函数调用
#     '''
#
#     def sum(a, b, c):
#         return a + b + c
#
#     def difer(a, b, c):
#         return a - b - c
#
#     if (flag == "+"):
#         return sum
#     else:
#         return difer
#
#
# x = func("+")
# print(x(1, 2, 3), type(x))

# 匿名函数
# """智能一个返回值"""
# lambda x, y: x + y
# print((lambda x, y: x + y)(1, 2))

# 闭包
# def linechonfig(content, lenth):
#     def line():
#         print("--" * lenth + content + "----" * (lenth // 2))
#
#     return line
#
#
# line1 = linechonfig("shabiba", 6)
# line2 = linechonfig("shabiba", 16)
# line1()
# line2()


# 装饰器
# 语法糖
def checkLogin(func):
    def inner(*args, **kargs):
        print("%s登录验证..." % args[0])
        func(*args, **kargs)
        return func

    return inner  # 定义两个功能函数


def checkpass(func):
    def inner(*args, **kargs):
        print("验证密码...")
        func(*args, **kargs)
        return func

    return inner  # 定义两个功能函数


def zsq(char):
    print(char * 50)
    return zsq


@checkLogin  # fss = checkLogin(fss)
@checkpass
def fss():
    print("发说说")


print(fss)


# 语法糖写法
@checkLogin
@checkpass
def ftp():
    print("发图片")


# ftp = checkLogin(ftp)

#
# index = 1
# if index == 1:
#     fss()
# else:
#     ftp()


# 带参数返回值装饰器

@checkLogin
@checkpass
# @zsq("-")
def Login(user, password):
    # print(user, password)
    return user


print(type(Login("cws", 1245)))
