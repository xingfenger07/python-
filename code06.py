# 1.元组 tuple
# 1.1基本格式:元组名=(元素1,元素2,元素3 ... )
# 所有元素包含在小括号内,元素与元素之间用,隔开,不同元素也可以是不同的数据类型
# tua = (1,2,3,'a','b')
# print(type(tua))
# tua = ()    #定义空元组
# tub=('a') #只有一个元素的时候,末尾必须加上,否则返回唯一的值的数据类型
# print (type (tub))

#1.2元组与列表的区别
# 1.元组只有一个元素末尾必须加,列表不需要
# li = [1]
# print(type(li))
# 2. 元组只支持查询操作,不支持增删改操作

# tua = (1,2,3,1)
# print(tua[2])   #元组也有下标,从左往右,从0开始
# tua[2] = 'a'    #报错.元组不支持修改操作
# count()、index()、len()跟列表的用法相同
# print(tua.index(2))
# print(tua.count(1))
# print(len(tua))
# print (tua[1:])

# 1.3 应用场景
# 函数的参数和返回值
# 格式化输出后面的()本质上就是一个元组
# name = 'bingbing'
# age = 18
# print("%s的年龄是:%d"%(name,age))
# info = (name, age)
# print(type(info))
# print("%s的年龄是:%d"% info)
#数据不可以被修改，保护数据的安全

# 2. 字典
#2.1基本格式:字典名={键1:值1,键2,值2 ... }
#键值对形式保存,键和值之间用:隔开,每个键值对之间用,隔开
# dic = {'name':'bingbing','age':18}
# print(type (dic))
#字典中的键具备唯一性,但是值可以重复
# dic2={'name':'bingbing','name':'susu'}#不会报错,键名重复前面的值会被后面的值著
# print (dic2)
# dic3={'name':'bingbing','name2':'bingbing' }
# print (dic3)

# 2.2字典常见操作
# 2.2.1 查看元素
# 变量名[键名]
# dic = {'name':'bingbing','age':18}
# print(dic[2])#不可以根据下标,字典中没有下标,查找元素需要根据键名,键名相当于下标
# print(dic['age']) # 18
# print(dic['sex']) #报错,键名不存在
#变量名.get(键名)
# dic = {'name':'bingbing','age':18}
# print(dic.get('name'))          #bingbing
# print(dic.get("tel"))           # None -- 键名不存在,返回None
# print(dic.get("tel",'不存在'))   #不存在 ———如果没有这个键名，返回自己设置的默认值

# 2.2.2 修改元素
# 变量名[键名]=值
# dic = {'name':'bingbing','age':18}
# dic['age']=20 #列表通过下标修改,字典通过键名修改
# print (dic)

# 2.2.3 添加元素
# 变量名[键名]=值
#注意:键名存在就修改,不存在就新增
# dic = {'name':'bingbing','age':18}
# dic['tel'] = 1244668   # 此时没有tel键,新增进字典
# print (dic)
# dic['tel'] =12345       # 此时已经有tel键了,修改tel对应的值
# print (dic)
# dic['remark'] = "在线征婚"
# print(dic)
# dic['remark']="是个好人"
# print(dic)

#2.2.4删除元素
# del
# 删除整个字典 del 字典名
# dic = {'name' :'bingbing','age' : 18}
# del dic
# print(dic)    #报错,已经被删除了,找不到这个字典
#删除指定键值对,键名不存在就会报错 del 字典名[键名]
# dic = {'name':'bingbing','age':18}
# del dic['age']
# # del dic['tel']  #没有指定的键就会报错
# print (dic)

# clear():清空整个字典里面的东西,但保留了这个字典
# dic = {'name':'bingbing','age':18}
# dic.clear()
# print(dic)
#pop()删除指定键值对,键不存在就会报错
# dic ={'name':'bingbing','age':18}
# dic.pop("age")
# dic. pop('tel')  #报错，不存在键名
# # dic. pop ()    #报错，没有指定键名
# dic. popitem()   #3.7之前版本是随机删除一个键值对，3.7之后默认删除最后一个键值对
# print (dic)
