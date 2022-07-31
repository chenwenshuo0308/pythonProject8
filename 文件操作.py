# # 打开文件
#
# file = open("test.txt", "r+")
# # file = open("test.txt", "w")
# # file = open("test.txt", "a")
# imagefile = open("girl.jpg", "rb")
# tofile0 = open("woman.jpg", "wb")
# # 查看文件权限
# if file.writable():
#     # if file.readable():
#     # 读写文件
#     # context = file.read()
#     # print(context)
#     file.write("\n#stratwrite")
#     # 操作文件
#
#     # print(imagefile)
#     # image = imagefile.read()
#
#     # content = image[0:len(image)]
#     # tofile0.write(content)
#     # +读写模式文件r+ w+ a+ rw+ rb+ wb+
#
#     # 操作
#     # file.seek(2, 0)  # 位移
#     # print(file.tell())  # 查看文件位置
#     # context = file.read()
#     # print(file.tell())
#     # print(context)
#
#     # 读详细介绍
#     # txt = file.read(5)  # 读取文件长度
#     # print(txt)
#     # txr = file.readline()  # 读取一行
#     # print(txr)
#     # txr = file.readline()
#     # print(txr)
#     # txr = file.readline()
#     # print(txr)
#     # content = file.readlines()  # 读取所有内容成为列表
#     # print(content, type(content))
#     # 文件可迭代
#     # print(isinstance(file, collections.abc.Iterator))
#     # content = file.readlines()
#     # for i in content:
#     #     print(i)
# # 关闭文件
# file.flush()
# file.close()
# imagefile.close()
# tofile0.close()

# os.rename("pythonfunction", "python文件")
# os.renames()#多级修改
# os.remove("c.txt")#删除文件
# os.rmdir("python文件")#删除空目录
# os.removedirs()#递归删除，删除路径所有内容，不能为空
# os.mkdir()#创建文件目录
# print(os.getcwd())
# print(os.listdir())
