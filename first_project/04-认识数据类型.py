'''
1.按经验将不同的变量存储不同的类型的数据
2.验证这些数据到底是什么类型 -- 检测数据类型的函数 type(数据)
'''

# int --整型
num1 = 1
# float --浮点型，就是小数
num2 = 1.2
# str --字符串 ，特点数据都要带''
num3 = 'hello word'
# bool -- 布尔型，通常判断使用，布尔型只有两个值 true 和 flase
num4 = 1 > 2
# list --列表
num5 = [1, 2, 3, 'a']
# tuple -- 元组
num6 = (10, 20, 30)
# set --集合
num7 = {'a', 1, 2}
# dict --字典 键值对
num8 = {'name': 'TOM', 'sex': '男'}
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(num5))
print(type(num6))
print(type(num7))
print(type(num8))
