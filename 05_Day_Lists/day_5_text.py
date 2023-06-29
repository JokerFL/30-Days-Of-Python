# # 1、Declare an empty list
# # 声明一个空列表
# my_list = []
# # 或者
# lst = list()  # 使用 append() 方法向其中添加元素lst.append('apple')

# # 2、Declare a list with more than 5 items
# fur = ['a', 'b', 'c', 'd', 'e']

# # 3、Find the length of your list
# print(len(fur))  # 5

# # 4、Get the first item, the middle item and the last item of the list
# first_item = fur[0]
# middle_item = fur[2]
# last_item = fur[len(fur) - 1]
# print(first_item)  # a
# print(middle_item)  # c
# print(last_item)  # e

# # 5、Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
# mixed_data_types = ['name', 'age', 'height', 'marital status', 'address']

# # 6、Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# # 7、Print the list  using print()
# print(mixed_data_types)
# print(it_companies)

# # 8、Print the number of companies in the list  打印列表中的公司数量
# print(len(it_companies))  # 7

# # 9、Print the first, middle and last company
# first_company = it_companies[0]
# middle_company = it_companies[3]
# last_company = it_companies[6]
# print(first_company)
# print(middle_company)
# print(last_company)

# # 10、Print the list after modifying one of the companies
# it_companies[0] = 'yahoo'
# print(it_companies)

# # 11、Add an IT company to it_companies  添加append
# it_companies.append('Tiktok')
# print(it_companies)

# # 12、Insert an IT company in the middle of the companies list  插入insert
# it_companies.insert(4, 'Baidu')
# print(it_companies)

# # 13、Change one of the it_companies names to uppercase (IBM excluded!)
# world01 = it_companies[0]  # 获取要修改元素的索引
# world = world01.capitalize()  # capitalize() 方法将单词的首字母转换为大写。
# print(world)  # 验证是否首字母大写
# it_companies[0] = world  # 将首字母大写的元素替换列表中对应索引的值
# print(it_companies)  # 打印输出

# # 14、Join the it_companies with a string '#;  '
# it_companies.append('#')
# print(it_companies)

# # 15、Check if a certain company exists in the it_companies list.
# print(it_companies.index('Yahoo'))

# # 16、Sort the list using sort() method
# it_companies.sort()  # 顺序  ['#', 'Amazon', 'Apple', 'Baidu', 'Google', 'IBM', 'Microsoft', 'Oracle', 'Tiktok', 'Yahoo']
# print(it_companies)

# # 17、Reverse the list in descending order using reverse() method    reverse() 按降序反转列表
# it_companies.sort(reverse=True)
# print(it_companies)  # 倒序  ['Yahoo', 'Tiktok', 'Oracle', 'Microsoft', 'IBM', 'Google', 'Baidu', 'Apple', 'Amazon', '#']

# # 18、Slice out the first 3 companies from the list  #18、从名单中剔除前3家公司
# del it_companies[0:3]
# print(it_companies)

# # 19、Slice out the last 3 companies from the list  #19、从名单中剔除最后3家公司
# del it_companies[-3:]
# print(it_companies)

# # 20、Slice out the middle IT company or companies from the list
# del it_companies[1:3]
# print(it_companies)

# # 21、Remove the first IT company from the list    从名单中删除第一家IT公司
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# it_companies.pop(0)
# print(it_companies)

# # 22、Remove the middle IT company or companies from the list
# del it_companies[2:4]
# print(it_companies)

# # 23、Remove the last IT company from the list
# it_companies.pop()
# print(it_companies)

# # 24、Remove all IT companies from the list
# it_companies.clear()
# print(it_companies)

# 25、Destroy the IT companies list   #25、销毁IT公司名单
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# del it_companies
# print(it_companies)


# 26、Join the following lists:
"""
加入以下列表：
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""
it_companiesed = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
all_list = it_companiesed + front_end + back_end
print("all_list:", all_list)

# 27、After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
# 27、在加入问题26的名单之后。复制联接列表并将其分配给变量full_stack。然后在Redux之后插入Python和SQL。
full_stack = all_list.copy()
print(full_stack.index('Redux'))
full_stack.insert(12,'Python')
full_stack.insert(13,'SQL')
print("all_list:", full_stack)





































