# 创建生成器
def test():
    # yield 1  # 生成器函数
    # print("a")
    # yield 2
    # return 0 会产生异常
    # print("b")
    # yield 3

    # print("c")
    for i in range(10):
        res = yield i
        print('当前%d' % i)
        print(res)


g = test()  # 只会产生生成器不会执行
# next方法
# print(next(g))
# print(next(g))

# print(g.__next__())
# print(g.__next__())
# send方法
print(g.send(None))
print(g.send("xiugai"))

# # close方法
# print(g.close())
# print(g.__next__())
