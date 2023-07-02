# Exercises: Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# # 1、Find the length of the set it_companies
# # 1，找出集合it_companies的长度
# print(len(it_companies))  #7


# # 2、Add 'Twitter' to it_companies
# # 在it_companies中添加“Twitter”
# it_companies.add('Twitter')
# print(it_companies)

# # 3、Insert multiple IT companies at once to the set it_companies
# # 3，同时向集合it_companies中插入多个IT公司
# it_companies02 = {'Baidu','Tencent','NetEase'}
# all_companies = it_companies02.union(it_companies)
# print(all_companies)
#
# it_companies.update(it_companies02)
# print(it_companies)

# # 4、Remove one of the companies from the set it_companies
# #4、从设置it_companies中删除其中一个公司
# it_companies.remove('IBM')   #指定删除“IBM”项
# print(it_companies)
#
# it_companies.pop()   #随机删除一项
# print(it_companies)


# # 5、What is the difference between remove and discard
# #五、去除和丢弃有什么区别
# it_companies.clear()   #去除 集合中项被清除
# print(it_companies)
#
# del it_companies   #丢弃 直接整个集合全部删除。返回NameError: name 'it_companies' is not defined错误
# print(it_companies)


# Exercises: Level 2
# 1、Join A and B
# A.update(B)
# print(A)

# C = A.union(B)
# print(C)


# # 可以使用集合的交集操作符&（或使用intersection()方法）来实现"A和B的连接"。交集操作将返回一个包含两个集合中共同元素的新集合。
# A_and_B = A & B
# print(A_and_B)

# # 2、Find A intersection B
# print(A.intersection(B))


# # 3、Is A subset of B
# print(A.issubset(B))


# # 4、Are A and B disjoint sets
# print(A.isdisjoint(B))
# print(B.isdisjoint(A))


# # 5、Join A with B and B with A
# # 可以使用集合的并集操作符|（或使用union()方法）来实现"A与B的连接"和"B与A的连接"。并集操作将返回包含两个集合中所有唯一元素的新集合。
# A_B = A | B     #A与B的连接
# B_A = B | B     #B与A的连接
# print(A_B)
# print(B_A)



# # 6、What is the symmetric difference between A and B
# #六、A和B之间的对称差是什么
# A.symmetric_difference(B)
# print(A.symmetric_difference(B))
#
#
# # 7、Delete the sets completely
# del A


# Exercises: Level 3
# 1、Convert the ages to a set and compare the length of the list and the set, which one is bigger?
#一、将年龄转换为一个集合，比较列表和集合的长度，哪一个更大？
age_set = set(age)
print("集合长度：",len(age_set))  #集合长度： 5
print("列表长度：",len(age))      #列表长度： 8


# 2、Explain the difference between the following data types: string, list, tuple and set
#2、解释以下数据类型之间的区别：字符串、列表、元组和集合
"""
以下是字符串、列表、元组和集合之间的区别：

1. 字符串（String）：
   - 字符串是由字符组成的不可变序列，用于表示文本数据。
   - 字符串可以使用单引号或双引号括起来。
   - 字符串中的字符按照索引访问，但不能修改字符串中的单个字符。
   - 字符串具有丰富的内置方法，可用于字符串的操作和处理。

2. 列表（List）：
   - 列表是由多个元素组成的有序可变序列。
   - 列表可以包含不同类型的元素，例如整数、字符串、甚至其他列表。
   - 列表使用方括号`[]`来定义，元素之间使用逗号分隔。
   - 列表中的元素可以通过索引进行访问、修改、删除或添加。
   - 列表支持切片操作，可以提取子列表。
   - 列表具有丰富的内置方法，可用于列表的操作和处理。

3. 元组（Tuple）：
   - 元组是由多个元素组成的有序不可变序列。
   - 元组可以包含不同类型的元素，类似于列表。
   - 元组使用圆括号`()`来定义，元素之间使用逗号分隔。
   - 元组中的元素可以通过索引进行访问，但不能修改、删除或添加。
   - 元组支持切片操作，可以提取子元组。
   - 元组一般用于存储不可变的数据，如函数返回多个值时。

4. 集合（Set）：
   - 集合是由唯一元素组成的无序集合。
   - 集合中的元素是不可变的（通常为不可哈希的），不能包含可变对象（如列表或字典）。
   - 集合使用花括号`{}`或`set()`函数来定义，元素之间使用逗号分隔。
   - 集合中的元素没有特定的顺序，不支持索引操作。
   - 集合的主要特点是去重，可以快速判断元素是否存在于集合中。
   - 集合具有丰富的内置方法，可用于集合的操作和处理，如并集、交集、差集等。

总结：
字符串用于处理文本数据，是不可变的序列；列表是有序可变序列，可以包含不同类型的元素；元组是有序不可变序列，可以包含不同类型的元素；集合是无序的唯一元素集合，用于快速判断元素的存在性。每种数据类型在不同场景下有不同的用途和特点，选择合适的数据类型可以更有效地处理数据。
"""

# 3、I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
#三、"I am a teacher and I love to inspire and teach people."。这个句子中使用了多少独特的单词？使用split方法和set来获取唯一的单词。
sentence = "I am a teacher and I love to inspire and teach people."

#使用split()方法将句子分割成单词列表
words = sentence.split()
print("单词列表:",words)

#使用set（）方法获取唯一单词
unique_words = set(words)
print("获取唯一单词:",unique_words)

#获取唯一单词数量
count_unique_words = len(unique_words)
print("获取唯一单词数量:",count_unique_words)

















































