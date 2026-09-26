# 字符串编码
# 本质上就是二进制数据与语言文字的一一对应关系
# 1.2Unicode:所有字符都是2个字节,
# 好处:字符与数字之间转换速度更快一些
# 坏处:占用空间大

# 1.3UTF-8:精准,对不同的字符用不同的长度表示
# 优点：节省空间
#缺点:字符与数字的转换速度较慢,每次都需要计算字符要用多少个字节来表示。

# # 字符串编码转换
# a = 'hello'
# print(a,type(a))
# # str,字符串是以字符为单位进行处理
# # 编码
# a1 = a.encode()
# print("编码后：",a1)
# print(type(a1))
# # bytes,以字节为单位进行处理
# # 解码
# a2 =  a1.decode()
# print(a2,type(a2))
# # 注意: 对于bytes,只需要直到它跟字符串类型之间的互相转换

# st ="这里是六星教育"
# st1 = st.encode("utf-8")
# print(st1,type(st1))
# st2 = st1. decode("utf-8")
# print(st2,type(st2))

# 2.字符串常见操作
# 2.1 + 字符串拼接
#print(10+10)#20,整型相加,+是算数运算符
# print("10”+'10')#1010,字符串相加,+是字符串拼接
# name1 ="六星"
# name2="教育"
# print(name1+ name2)
# print(name1, name2,sep="")

# 2.2* 重复输出
# print("好好学习,天天向上\n"*5)
# 注意:需要输出多少次*后面就写多少
# print('&\t'*10)

# 2.2 成员运算符
# 作用:检查字符串中是否包含了某个子字符串(即某个字符或多个字符)
# in:如果包含的话,返回True,不包含返回False
#not in:如果不包含的话,返回True,包含返回False
# name = 'bingbing'
# print('b' in name)      # True
# print('a' in name)      # False
# print('b' not in name)  # False
# print('a' not in name)  # True
# print('bin' in name)    # True
# print ('binb' in name)  # False


# 2.3下标
# Python中下标从0开始
# 作用:通过下标能够快速找到对应的数据
#格式:字符串名[下标值]
# name = 'sixstar'
# #从左往右数,下标从0开始
# print (name[0])
# print (name[1])
# print (name[2])
# print (name[3])
# print (name[4])
# print (name[5])
# print (name[6])
# print(name[7]) #报错,取值的时候不要超出下标范围
#从右往左数,下标从-1开始,-1,-2 ...
# print(name[-1])
# print(name[-2])
# print (name [-8])   #报错,超出索引范围

