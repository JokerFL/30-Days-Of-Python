"""
Python中有四种集合数据类型：
列表：是一个有序、可更改（可修改）的集合。允许重复成员。
元组：是一个有序的、不可更改或不可修改（不可变）的集合。允许重复成员。
集合：是一个无序、未索引和不可修改的集合，但我们可以向集合中添加新项。不允许有重复的成员。
Dictionary[字典]：是一个无序、可变（可修改）和索引的集合。没有重复的成员。

列表是不同数据类型的集合，它们是有序的和可修改的（可变的）。列表可以为空，也可以具有不同的数据类型项。
"""


# 创建list的两中方式：

# #1、Using list built-in function :  lst = list()
# empty_list = list()
# print(len(empty_list))   # 这是一个空列表，所以返回的是0
#
# # 2、Using square brackets.[] :  lst = []
# empty_list = []
# print(len(empty_list))   # 这是一个空列表，所以返回的是0



# # Lists with initial values. We use len() to find the length of a list.
# fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
# web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# # Print the lists and its length
# print('Fruits:', fruits)
# print('Number of fruits:', len(fruits))
# print('Vegetables:', vegetables)
# print('Number of vegetables:', len(vegetables))
# print('Animal products:',animal_products)
# print('Number of animal products:', len(animal_products))
# print('Web technologies:', web_techs)
# print('Number of web technologies:', len(web_techs))
# print('Countries:', countries)
# print('Number of countries:', len(countries))


# # 列表索引
# fruits = ['banana', 'orange', 'mango', 'lemon']
# first_fruit = fruits[0] # we are accessing the first item using its index
# print(first_fruit)      # banana
# second_fruit = fruits[1]
# print(second_fruit)     # orange
# last_fruit = fruits[3]
# print(last_fruit) # lemon
# # Last index
# last_index = len(fruits) - 1
# last_fruit = fruits[last_index]

# # 使用负索引访问列表项，负索引表示从末尾开始，-1表示最后一项，-2表示倒数第二项。
# fruits = ['banana', 'orange', 'mango', 'lemon']
# first_fruit = fruits[-4]
# last_fruit = fruits[-1]
# second_last = fruits[-2]
# print(first_fruit)      # banana
# print(last_fruit)       # lemon
# print(second_last)      # mango


# # 使用“unpacking”操作符，可以将列表中的每个项分配给单独的变量。
# # 列表中先一一分配，最后剩下的都分配到rest容器中
# lst = ['item','item2','item3', 'item4', 'item5']
# #  *rest 是一个包含lst列表剩余项的列表。*rest 则用于收集剩下的元素，并将它们作为列表赋给变量 rest。
# first_item, second_item, third_item, *rest = lst
# print(first_item)     # item1
# print(second_item)    # item2
# print(third_item)     # item3
# print(rest)           # ['item4', 'item5']


# # First Example
# fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
# first_fruit, second_fruit, third_fruit, *rest = fruits
# print(first_fruit)     # banana
# print(second_fruit)    # orange
# print(third_fruit)     # mango
# print(rest)           # ['lemon','lime','apple']
# # Second Example about unpacking list
# first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# print(first)          # 1
# print(second)         # 2
# print(third)          # 3
# print(rest)           # [4,5,6,7,8,9]
# print(tenth)          # 10
# # Third Example about unpacking list
# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic, es ,ex = countries
# print(gr)  #Germany
# print(fr)  #France
# print(bg)  #Belgium
# print(sw)  #Sweden
# print(scandic)  #['Denmark', 'Finland', 'Norway']
# print(es)  #Iceland
# print(ex)  #Estonia
#
# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic, es = countries
# print(gr)  #Germany
# print(fr)  #France
# print(bg)  #Belgium
# print(sw)  #Sweden
# print(scandic)  #['Denmark', 'Finland', 'Norway', 'Iceland']
# print(es) #Estonia

"""
所以，*scandic就是一个包括了剩余部分的一个列表
"""


"""
从列表中剪切项目
    正索引：我们可以通过指定开始、结束和步骤来指定一系列正索引，返回值将是一个新列表。
    （start=0，end=len（lst）-1（最后一项），step=1的默认值）
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[0:4] # it returns all the fruits
# print(all_fruits)
#
# # this will also give the same result as the one above
# # [] 取前不取后
# all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
# print(all_fruits)
#
# orange_and_mango = fruits[1:3] # it does not include the first index
# print(orange_and_mango)
#
# orange_mango_lemon = fruits[1:]
# print(orange_mango_lemon)
#
# orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
# print(orange_and_mango)



# # ['banana', 'orange', 'mango', 'lemon']
# #     -4        -3       -2        -1
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[-4:] # it returns all the fruits
# print(all_fruits)
#
# orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
# print(orange_and_mango)
#
# orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
# print(orange_mango_lemon)
#
# # 步长为-1，列表元素反转
# reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
# print(reverse_fruits)


"""
修改列表
列表是一个可变或可修改的有序项目集合。让我们修改水果列表。
利用索引值来定位列表元素从而修改该列表内的元素值
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits[0] = 'avocado'
# print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
# fruits[1] = 'apple'
# print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
# last_index = len(fruits) - 1
# fruits[last_index] = 'lime'
# print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']


"""
检查列表中的项目
使用in运算符检查项目是否为列表的成员。请参阅下面的示例。
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# does_exist = 'banana' in fruits
# print(does_exist)  # True
# does_exist = 'lime' in fruits
# print(does_exist)  # False




"""
将项目添加到列表
要将项添加到现有列表的末尾，我们使用方法append（）。
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.append('apple')
# print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
# fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
# print(fruits)



"""
将项目插入列表
我们可以使用insert（）方法在列表中的指定索引处插入单个项。
请注意，其他项目会向右移动。insert（）方法接受两个参数：index和要插入的项。
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.insert(2, 'apple') # insert apple between orange and mango
# print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
# fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
# print(fruits)
# # 索引值就是所要插入的元素位置


"""
从列表中删除项目
remove方法从列表中删除指定的项
"""
# fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
# fruits.remove('banana')
# print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
# fruits.remove('lemon')
# print(fruits)  # ['orange', 'mango', 'banana']
# # 直接将要删除的元素值输入到remove()方法中，就可以直接删除（remove()只会删除列表中的第一个匹配项）


"""
使用Pop删除项目
pop（）方法删除指定的索引（如果未指定索引，则删除最后一项）：
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.pop()
# print(fruits)       # ['banana', 'orange', 'mango']
#
# fruits.pop(0)
# print(fruits)       # ['orange', 'mango']



"""
使用Del删除项目
del关键字删除指定的索引，还可以用于删除索引范围内的项。它还可以完全删除列表
"""
# fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits[0]
# print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
#
# del fruits[1]
# print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
#
# del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!（这会删除给定索引之间的项，因此不会删除索引为3的项！）
# print(fruits)       # ['orange', 'lime']
#
# del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined（这应该给出：名称错误：名称“水果”未定义）


"""
清除列表项目
clear（）方法清空列表：
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.clear()
# print(fruits)       # []
# # clear（）与 del 列表名 不一样，前者是将列表内元素清空，后者是直接删除列表这个整体



"""
复制列表
可以通过以下方式将列表重新分配给新变量来复制列表：list2=list1。
现在，list2是list1的引用，我们在list2中所做的任何更改也会修改原来的list1。
但在很多情况下，我们不喜欢修改原件，而是喜欢有一个不同的副本。避免上述问题的方法之一是使用copy（）。
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits_copy = fruits.copy()
# print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
#
# fruits_copy.append('apple')
# print("fruits_copy:",fruits_copy)   # fruits_copy: ['banana', 'orange', 'mango', 'lemon', 'apple']
# print("fruits:",fruits)             # fruits: ['banana', 'orange', 'mango', 'lemon']


"""
加入列表
在Python中，有几种方法可以连接或连接两个或多个列表。
1、加号运算符（+）
2、使用extend（）方法联接extend（（）方法允许在列表中附加列表。
"""

# #1、加号运算符（+）
# positive_numbers = [1, 2, 3, 4, 5]
# zero = [0]
# negative_numbers = [-5,-4,-3,-2,-1]
# integers = negative_numbers + zero + positive_numbers
# print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']



# # 2、使用extend（）方法联接extend（（）方法允许在列表中附加列表。请参阅下面的示例。
# num1 = [0, 1, 2, 3]
# num2= [4, 5, 6]
# num1.extend(num2)
# print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
#
#
# negative_numbers = [-5,-4,-3,-2,-1]
# positive_numbers = [1, 2, 3,4,5]
# zero = [0]
# negative_numbers.extend(zero)
# negative_numbers.extend(positive_numbers)
# print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# fruits.extend(vegetables)
# print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']



"""
计数列表中的项目
count（）方法返回一个项目在列表中出现的次数：
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits.count('orange'))   # 1
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.count(24))           # 3



"""
Finding Index of an Item
The index() method returns the index of an item in the list:
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits.index('orange'))   # 1
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.index(24))           # 2, the first occurrence(只会查找到第一个匹配项)


"""
Reversing a List
The reverse() method reverses the order of a list. 反转列表
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.reverse()
# print(fruits) # ['lemon', 'mango', 'orange', 'banana']
#
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# ages.reverse()
# print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
# # print(ages.reverse())   返回值为None
# # list.reverse()方法会原地反转列表的顺序，并且没有返回值，或者说返回None。
# # 所以当你调用ages.reverse()时，它会修改ages列表本身，并且返回值为None。
# # 因此，print(ages.reverse())会输出None。


"""
排序列表项
要对列表进行排序，我们可以使用sort（）方法或sorted（）内置函数。
sort（）方法按升序对列表项进行重新排序，并修改原始列表。
如果sort（）方法reverse的参数等于true，它将按降序排列列表。
"""
# # sort（）：此方法修改原始列表
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.sort()
# print(fruits) # 按字母顺序排列, ['banana', 'lemon', 'mango', 'orange']
#
# fruits.sort(reverse=True)
# print(fruits) # 降序排列  ['orange', 'mango', 'lemon', 'banana']
#
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# ages.sort()
# print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]
#
# ages.sort(reverse=True)
# print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]


# sorted（）：在不修改原始列表的情况下返回有序列表
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
"""
sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
"""











































































































































































