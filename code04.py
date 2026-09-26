#while循环
# i = 1
# while i <= 10:
#     print('wc')
#     i += 1
# 条件不为零或False,条件一直为真,就会一直执行,从而形成一个死循环

# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i = i + 1
# print('计算结果是:',sum)


# for 循环
#可迭代对象就是要去遍历取值的整体,现在的话只需要记住字符串就是可迭代对象
# str = 'helloworld'
# for i in str:  #i是临时变量,可以随便写
#     print(i)

# 3.2 range ()
#用来记录循环次数,相当于一个计数器
# for i in range(1,6): #从1开始,从6结束,遵循包前不包后规则
#     print (i)

# 包前不包后:包含开始位置的数字,不包含结束位置的数字
# range()里面只写一个数,这个数就是循环的次数,默认从0开始
# 写两个数,前面的数字代表开始位置,后面的数字代表结束位置

# s = 0
# for i in range(1,101):
#     # print(i)
#     s += i
# print(s)

# break和continue 都是专门在循环中使用的关键字
# i= 1
# while i <= 5:
#     print(f"小红在吃第{i}个苹果")
#     if i == 3:
#         print('吃饱了不吃了')
#         break # 结束break所在的循环
#     i += 1
# i = 1
# while i <= 5:
#     print(f"小明在吃第{i}个苹果")
#     if i == 3:
#         print(f"吃到了一条大虫子,第{i}个苹果不吃了")
#         #在continue之前,一定要修改计数器,否则会陷入死循环
#         i += 1
#         continue
#     i += 1

# for i in range(5):
#     if i == 3:
#         # break  # i=3时结束当前所在循环
#         continue  #跳过3,结束了在3时的循环,继续执行下一次循环
#     print(i)


