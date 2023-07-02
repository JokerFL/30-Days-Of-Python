"""
集合：
集合是项目的集合。Set是无序和未索引的不同元素的集合。在Python中，集合用于存储唯一项，
并且可以找到集合之间的并集、交集、差集、对称差集、子集、超集和不相交集。
"""

# 创建一个集合
# 我们使用花括号｛｝来创建一个集合或者使用set（）内置函数。

# # Creating an empty set
# # syntax
# st = {}
# # or
# st = set()


# # 创建包含初始项的集合
# st = {'item1', 'item2', 'item3', 'item4'}
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}


# # Getting Set's Length
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# len(fruits)


"""
访问集合中的项目
我们使用循环来访问项目。我们将在循环部分看到这一点
"""
# # 检查项目
# # 为了检查列表中是否存在项目，我们在成员资格运算符中使用。
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# print('mango' in fruits ) # True


"""
将项目添加到集合
一旦创建了一个集合，我们就不能更改任何项目，我们还可以添加其他项目。
"""
# # Add one item using add()
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.add('lime')

# # 使用update（）添加多个项目，update（）允许将多个项目添加到一个集合中。update（）接受一个列表参数。
# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.update(['item5','item6','item7'])
# print(st)    #输出的这个集合不是固定的，里面的元素位置是随机打乱排列的
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
# fruits.update(vegetables)
# print(fruits)   #输出的这个集合不是固定的，里面的元素位置是随机打乱排列的


"""
从集合中删除项目
我们可以使用remove（）方法从集合中移除一个项。
如果找不到该项，remove（）方法将引发错误，因此最好检查给定集合中是否存在该项。
但是，discard（）方法不会引发任何错误。
"""
# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.remove('item2')
# print(st)


# # pop（）方法从列表中移除一个随机项，并返回移除的项。
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.pop()  # removes a random item from the set
# print(fruits)

# fruits = {'banana', 'orange', 'mango', 'lemon'}
# removed_item = fruits.pop()
# print(removed_item)  #打印随机删除的项


# # 清除集合中的项目
# # 如果我们想清除或清空集合，我们使用clear方法。
# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.clear()
# print(st)   # set()
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.clear()
# print(fruits) # set()


"""
删除集合
如果我们想删除集合本身，我们使用del运算符。
"""
# # syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# del st
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# del fruits
# print(fruits)  #NameError: name 'fruits' is not defined


"""
正在将列表转换为集合
我们可以将列表转换为集合，也可以将集合转换为列表。将列表转换为集合将删除重复项，并且只保留唯一项。
"""
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}


"""
连接集
我们可以使用union（）或update（）方法连接两个集合。
"""
# # 并集此方法返回一个新集
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item5', 'item6', 'item7', 'item8'}
# st3 = st1.union(st2)
# print(st3)
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
# print(fruits.union(vegetables))

# # Update此方法将一个集合插入到给定的集合中
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item5', 'item6', 'item7', 'item8'}
# st1.update(st2) # st2 contents are added to st1
# print(st1)
#
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
# fruits.update(vegetables)
# print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}


# # 查找交叉点项目
# # 交集返回两个集合中的一组项。参见示例
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item3', 'item2'}
# st1.intersection(st2) # {'item3', 'item2'}
# print(st1.intersection(st2))  #返回交集项
#
# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
# print(whole_numbers.intersection(even_numbers))
#
# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.intersection(dragon)     # {'o', 'n'}
# print(python.intersection(dragon))


# # 检查子集和父集
# # 集合可以是其他集合的子集或父集：
#
# # 子集：issubset（）
# # 父集：issuperset（）
#
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# st2.issubset(st1) # True
# print(st2.issubset(st1))
# st1.issuperset(st2) # True
# print(st1.issuperset(st2))
#
# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.issubset(even_numbers) # False, because it is a super set
# print(whole_numbers.issubset(even_numbers))
# whole_numbers.issuperset(even_numbers) # True
# print(whole_numbers.issuperset(even_numbers))
#
# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.issubset(dragon)     # False
# print(python.issubset(dragon))


# # 检查两个集合之间的差异
# # 它返回两组之间的差值。
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# st2.difference(st1) # set()
# print(st2.difference(st1))
# st1.difference(st2) # {'item1', 'item4'} => st1\st2
# print(st1.difference(st2))
#
# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
# print(whole_numbers.difference(even_numbers))
#
# python = {'p', 'y', 't', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# print(python.difference(dragon))
# dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# print(dragon.difference(python))


"""
求两个集合之间的对称差
它返回两个集合之间的对称差。这意味着它返回一个包含两个集合中所有元素的集合，
除了两个集合中都存在的元素，数学上是:(a \B)∪(B\ a)
symmetric_difference()返回的是该集合包含出现在两个集合中的所有元素，但不包含同时出现在两个集合中的元素。
"""
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# # it means (A\B)∪(B\A)
# st2.symmetric_difference(st1) # {'item1', 'item4'}
# print(st2.symmetric_difference(st1))
#
#
# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# some_numbers = {1, 2, 3, 4, 5}
# whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}
# print(whole_numbers.symmetric_difference(some_numbers))
#
# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# print(python.symmetric_difference(dragon))


"""
连接集
如果两个集合没有一个或多个公共项，我们称它们为不相交集合。
我们可以使用isdisjoint（）方法来检查两个集合是联合的还是不相交的。
如果两个集合没有共同元素，isdisjoint()方法返回True，否则返回False。
"""
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1)

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}








































































































































































