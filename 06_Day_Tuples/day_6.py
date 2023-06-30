# Creating a Tuple


# # 构造语法
# empty_tuple = ()
#
# # 或者使用构造函数
# empty_tuple = tuple()


# # 具有初始值的元组
# tpl = ('item1','item2','item3')
#
# fruits = ('banana','orange','mango','lemon')


# # 元组长度
# tpl = ('item1','item2','item3')
# print(len(tpl))


"""
访问元组项目
正索引与列表数据类型类似，我们使用正索引或负索引来访问元组项
"""
# # 1、示例
# tpl = ('item1','item2','item3')
# first_item = tpl[0]
# second_item = tpl[1]
#
# #2、示例
# fruits = ('banana','orange','mango','lemon')
# first_fruit = fruits[0]
# second_fruit = fruits[1]
# last_index = len(fruits) - 1
# last_fruit = fruits[last_index]


"""
负索引负索引是指从结尾开始，-1表示最后一项，-2表示倒数第二项，列表/元组长度的负数表示第一项。
"""
# tpl = ('item1', 'item2', 'item3','item4')
# first_item = tpl[-4]  #item1
# second_item = tpl[-3]  #item2
#
# fruits = ('banana', 'orange', 'mango', 'lemon')
# first_fruit = fruits[-4]    #banana
# second_fruit = fruits[-3]   #orange
# last_fruit = fruits[-1]     #lemon


"""
切片元组
我们可以通过指定一系列索引来分割一个子元组，这些索引在元组中从哪里开始，从哪里结束，返回值将是一个具有指定项的新元组。
"""
# 正指数范围
# tpl = ('item1', 'item2', 'item3','item4')
# all_items = tpl[0:4]         # all items
# all_items = tpl[0:]         # all items
# middle_two_items = tpl[1:3]  # does not include item at index 3
# print(all_items)
# print(middle_two_items)

# fruits = ('banana', 'orange', 'mango', 'lemon')
# all_fruits = fruits[0:4]    # all items
# all_fruits= fruits[0:]      # all items
# orange_mango = fruits[1:3]  # doesn't include item at index 3
# orange_to_the_rest = fruits[1:]

#负指数范围
# tpl = ('item1', 'item2', 'item3','item4')
# all_items = tpl[-4:]         # all items
# middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
# print(middle_two_items)         #('item2', 'item3')

# fruits = ('banana', 'orange', 'mango', 'lemon')
# all_fruits = fruits[-4:]    # all items
# orange_mango = fruits[-3:-1]  # doesn't include item at index 3
# orange_to_the_rest = fruits[-3:]


"""
将元组更改为列表
我们可以将元组更改为列表，也可以将列表更改为元组。
元组是不可变的。如果我们想修改一个元组，我们应该将其更改为列表。
"""
# 语法格式
# tpl = ('item1', 'item2', 'item3','item4')
# lst = list(tpl)

# fruits = ('banana', 'orange', 'mango', 'lemon')
# fruits = list(fruits)
# fruits[0] = 'apple'
# print("这是列表：",fruits)     # ['apple', 'orange', 'mango', 'lemon']
# fruits = tuple(fruits)
# print("这是元组：",fruits)     # ('apple', 'orange', 'mango', 'lemon')


"""
检查元组中的项目
我们可以使用in检查元组中是否存在项，它返回一个布尔值。
"""
# Syntax
# tpl = ('item1', 'item2', 'item3','item4')
# 'item2' in tpl # True

# fruits = ('banana', 'orange', 'mango', 'lemon')
# print('orange' in fruits) # True
# print('apple' in fruits) # False
# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment[“tuple”对象不支持项分配]


"""
连接元组
我们可以使用+运算符连接两个或多个元组
"""
# syntax
# tpl1 = ('item1', 'item2', 'item3')
# tpl2 = ('item4', 'item5','item6')
# tpl3 = tpl1 + tpl2

# fruits = ('banana', 'orange', 'mango', 'lemon')
# vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)


"""
删除元组
不可能删除元组中的单个项，但可以使用del删除元组本身。
"""
# # syntax
# tpl1 = ('item1', 'item2', 'item3')
# del tpl1
#

# fruits = ('banana', 'orange', 'mango', 'lemon')
# del fruits

# # 删除项应该时转换为列表，删除项后再转换回来
# fruits = list(fruits)
# fruits.remove('orange')
# fruits = tuple(fruits)
# print(fruits)






















































































































