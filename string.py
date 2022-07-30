# string1 = "acde"
# string2 = '''ssfvajs'''
# print(string1, type(string1))
# print(string2, type(string2))
# name = r"我是\'cws\'\n在吉林大学"
# print(name, type(name))
# name = "我叫%s" % ("cwws")
# print(name * 5)
# print(name[0])
# print(name[0:len(name):2])
# print(name[4:1:-1])
# print(name[::1])
# str1 = "shafjkeflasblhejbgkh"
# # print(str1.find("f", 5, 20))
# # print(str1.index("sha"))
# # print(str1.replace("s", "z"))
# str2 = "shafj keflasblh ejGHOSh"
# # print(str2.capitalize())
# # print(str2.title())
# print(str2)
# print("|" + str2.lstrip("ke") + "|")

# split分割字符
# info = "cws-18-13131313-jlu"
# result = info.split("-")
# print(result)
# print(type(result))
# print(info.partition("-"))
# iteam = ['cws', '18', '13131313', 'jlu']
# print(info.join(iteam))
# # 判定是否字符串字符
# print(info.startswith("cws"))
# print(info.endswith("jlu"))

# naumlist = list(range(0, 100))
# print(naumlist)
# print((type(naumlist)))

# 可迭代对象
# nlist = [1, 2.3, 4, 5]
# result = isinstance(nlist, collections.abc.Iterable)
# print(result)
# result1 = isinstance(nlist, collections.abc.Iterator)
# print(result1)


# 斐波那契
# nlist = [1, 2, 3, 4, 5]
# print([1, 2, 3, 4, 5] == nlist)


s = "hofhaok askhf aks"

# nlist = [1, 2, 3, 4, 5]
# result = nlist.sort(reverse=True)
# print(result, nlist)
# ntul = 1, 2, 3, "abc"
# ntul2 = ([1, 2, 3], 2, 3)
# # print(type(ntul2))
# # print(ntul.count(1))
# idx = ntul.index(2)
# print(idx)
# print(len(ntul2))
person = {"age": "18", "name": "saf", 1: 2, 1: 2}
# print(person["age"])
#
# person["height"] = 60
# print(person, id(person))
# person.pop("age")
# print(person, id(person))
# person.clear()
# print(person, id(person))
# del person
# print(person, id(person))

# result = person.get("age")
# result = person.setdefault(("university", "jlu"))
# print(result, person)
# key = person.keys()
# print((key))
# kvs = person.items()
# print(kvs)
# for i in kvs:
#     print((i))
#     print(len(i))

# sets = {1, 2, 3, 4, "abc"}
# print(type(sets))
# a = frozenset("abcd")
# print(a, type(a))

l = [1, 1, 2, 3, 4, 4]
a = set(l)
# print(a, type(a))
# a.pop()
# a.discard(3)
# print(a, type(a))

# its = iter(a)
# # print(next(its))
# # print(next(its))
# for v in its:
#     print(v)


list1 = [1, 1, 2, 3, 4, 4]
a = set(list1)
b = frozenset([1, 2, 4])
# result = a.intersection(b)
# result = a.union(b)
# result = b.union(a)
# result = b.update(a)
# result = a.difference(b)
# print(a, b)
# print(result, type(result))
print(a.issubset(b))
print(a.isdisjoint(b))
print(a.issuperset(b))
