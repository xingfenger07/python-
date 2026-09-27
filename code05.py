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

# 2.4切片
# 含义:指对操作的对象截取其中一部分的操作
# 语法: [开始位置:结束位置:步长]
#包前不包后:即从起始位置开始,到结束位置的前一位结束(不包含结束位置本身)
# st ='abcdefghijk'
# 从左往右
# print(st[0:4])  # abcd
# print(st[4:7])  # efg
# print(st[3:])   # defghijk -- 下标为3之后的全部截取到
# print (st[:7])  # abcdefg, -- 下标为7之前的全部截取到,不包含7
# 从右往左
# print(st[-1:])
# print(st[ :- 1])
# print(st[-1 :- 5])
#步长:表示选取间隔,不写步长,则默认是1
# 步长的绝对值大小决定切取的间隔,正负号决定切取方向。
#正数表示从左往右取值,负数表示从右往左取值。
# st ='abcdefghijk'
# print(st[-1 ::- 1])       # kjihgfedcba
# print(st[-1 :- 5 :- 1] )   # kjih
# print(st[0:7:3])


# 3. 字符串常见操作
# 3.1 查找
# find:检测某个子字符串是否包含在字符串中,如果在就返回这个子字符串开始位置的下标,否则就返回-1
# find(子字符串,开始位置下标,结束位置下标)
#注意:开始和结束位置下标可以省略,表示在整个字符串中查找
# name = 'bingbing'
# print(name.find('i'))       # 1 -- 第一个i的下标为1
# print(name.find('bing'))    #0 -- 检测到第一个bing,b的下标为0
# print(name.find('b',3))     #4
# print (name.find('b',5))    #-1 -- 超出范围,不包含返回-1
# print(name.find('b',3,5))   #4 -- 在下标3-5位置范围内查找
# # 包前不包后
# print(name.find('b',3,4))   #-1

#2.index():检测某个子字符串是否包含在字符串中,如果在就返回这个子字符串开始位置的下标,否则就会报错
# index(子字符串,开始位置下标,结束位置下标)
#注意:开始和结束位置下标可以省略,表示在整个字符串中查找
# name ="我命油我不油天"
# print(name.index("命"))
# print(name.index('命’,2))  #1
# print(name.index("命",1,3))#报错，下标2开始找，没有找到
# 同样遵循包前不包后规则
#和find的区别:find没找到,返回-1,index没找到就会报错

# 3.count():返回某个子字符串在整个字符串中出现的次数,没有就返回0
#count(子字符串,开始位置下标,结束位置下标)
#注意:开始和结束位置下标可以省略,表示在整个字符串中查找
# name ='bingbing'
# print(name. count('b'))      #2
# print (name. count('a'))     #0
# print(name.count('b',1))     #1
# print(name.count('b',1,3))   #0
# print(name.count('b',1,4))   #0 -- 同样遵循包前不包后规则



# 3.3 判断
#1.startswith():是否以某个子字符串开头,是的话就返回True,不是的话就返回False,如果设置开始和结束位置下标
#               则在指定范围内检查
# startswith(子字符串,开始位置下标,结束位置下标)
# st = 'sixstar'
# print (st. startswith('six'))   # True
# print (st. startswith('sex'))   # False
# print (st. startswith('x',2,6)) # True

#2.endswith():是否以某个子字符串结尾,是的话就返回True,不是的话就返回False,如果设置开始和结束位置下标
#               则在指定范围内检查
# endswith(子字符串,开始位置下标,结束位置下标)
# st ='sixstar'
# print (st.endswith('er')) # False

#3.isupper():检测字符串中所有的字母是否都为大写,是的话就返回True
# st = 'sixstar'
# print(st. isupper())    #False
# print('SIX'.isupper())  # True

# 3.2修改元素
# 1.replace():替换
#replace(旧内容,新内容,替换次数)
#注意:替换次数可以省略,默认全部替换
# name='好好学习,天天向上'
# print(name.replace("天",'时'))        # 好好学习,时时向上
# print(name.replace("天",'时',1))      #好好学习,时天向上

# #2.split():指定分隔符来切字符串
# st ='hello, python'
# # print(st.split(','))#['hello','python'], -- 以列表的形式返回
# ## 如果字符串中不包含分割内容,就不进行分割I 会作为一个整体
# print(st.split('a'))  #['hello, python']
# print(st.split('o'))  #['hell', ', pyth', 'n']
# print(st.split('o',1))  #['hell', ', python'] -- 指定只分割一次

# 3.capitalize():第一个字符大写,其他都小写
# st = 'bingBing'
# print(st.capitalize())

# 4.lower():大写字母转为小写
# st = 'bIngBinG'
# print(st.lower())

# 5. upper():小写字母转为大写
# st = 'bIngBinG'
# print (st. upper())

# 4.列表
# 基本格式:
# 列表名 =[元素1,元素2,元素3 .. ]
# 注意:
#所有元素放在[]内,元素与元素之间用,隔开
# 元素之间的数据类型可以各不相同
# li = [1,2,'a',4]
# print(li, type(li))
# # # 列表也可以进行切片操作
# print(li[0:3])
# 列表是可迭代对象,可以for循环遍历取值
# for i in li:
#     print (i)

# 5.列表常见操作
# 5.1 添加元素
# append() extend() insert()
# li = ['one',' two',' three' ]
# li.append("four")       #append整体添加
# li.extend(' four')      # extend 分散添加,将另外一个类型中的元素逐一添加
# li. insert(3,'four')    # 在指定位置插入元素
# li. insert(0,'four')    # 指定位置如果有元素,原有元素就会后移
# li. insert ("four")     # 报错,没有指定下标
# print (li)
# li = [1,2,3]
# li. append(4)
# # li.extend(4)        #报错
# li. insert(3,4)
# print (li)

#5.2 修改元素
# 5.2修改元素
# 直接通过下标就可以进行修改
# 1i = [1,2,3]
# 1i[1] = 'a'
# print (1i)

# 5.3 查找元素
# in:判断指定元素是否存在列表中,如果存在就返回True,不存在就返回False
#not in:判断指定元素是否存在列表中,如果不存在就返回True,存在就返回False
# li = ['a','b','c','d']
# print('e' in li)


#用户输入昵称,昵称重复则不能使用
#定义一个列表,保存已经存在的昵称
# name_list = ['bingbing','susu','zivi']
# while True:
#     name = input("请输入您的昵称:")
#     # 判断昵称是否已经存在
#     if name in name_list:
#         print(f"您输入的昵称{name}已经存在了哦")
#     # 如果昵称不存在
#     else:
#         print(f"昵称{name}已经被您使用")
#     #把新昵称增加到列表
#         name_list.append(name)
#         print(name_list)
#         break

# index:返回指定数据所在位置的下标,如果查找的数据不存在就会报错
# count:统计指定数据在当前列表出现的次数
# 跟字符串中的用法相同

#5.4删除元素
# del
# li=['a','b','c','d']
# # del li  # 删除列表
# del li[2] # 根据下标删除
# print (li)

#pop:删除指定下标的数据,python3版本默认删除最后一个元素
# li = ['a','b','c','d']
# # 1i.pop() #默认删除最后一个元素
# li.pop(2) #不能指定元素删除,只能根据下标进行删除,下标不能超出范围
# print (li)

# remove: 根据元素的值进行删除
# li = ['a','b','c','d']
# li. remove ('d')
# # li. remove('t')   # 报错,列表中不存在这个元素
# li. remove ('b')    # 默认删除最开始出现的指定元素
# print (li)

# 5.5排序
# sort:将列表按特定顺序重新排列,默认从小到大
# reverse:倒序,将列表倒置(反过来)
# li = [1,5,3,2,4]
# li. sort()    # 按照从小到大的顺序排序
# li. reverse()  # 倒序
# print (li)

#5.6列表推导式
# 格式一: [表达式 for 变量 in 列表]
#注意:in后面不仅可以放列表,还可以放range()、可迭代对象
# li = [1,2,3,4,5,6]
# [print(i*5) for i in li] # 前面的i是表达式
# li = []
# for i in range(1,6):
#     # print (i)
#     li. append(i)
# print (li)
# [li.append(i) for i in range(1,6)]
# print (li)
# 格式二:[表达式 for 变量 in 列表 if 条件]
# 把奇数放进列表里面
li = []
# for i in range(1,11):
#     if i % 2 == 1:
#         li.append(i)
# print (li)
# [li.append(i) for i in range(1,11) if i% 2 == 1]
# print (li)

#5.7列表嵌套
#5.7 列表嵌套
#含义:一个列表里面又有一个列表
# li =[1,2,3,[4,5,6]]#[4,5,6]是里面的列表
# print(li[3]) #取出里面的列表
# print(li[3][2]) #取出内列表中的下标为2的元素



