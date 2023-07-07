# 1、Create an empty dictionary called dog
dog = {}

# 2、Add name, color, breed, legs, age to the dog dictionary
# 将名称、颜色、品种、腿、年龄添加到狗字典中
dog = {'name':'DaHuang','color':'black','breed':'jinmao','legs':'long','age':'4'}


# 3、Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# 创建一本学生词典，并添加first_name、last_name、性别、年龄、婚姻状况、技能、国家、城市和地址作为词典的关键字
Students = {'first_name':'Tom','last_name':'kuang','gender':'man','age':'18','marital status':'No','skills':'Java','country':'China','city':'shanghai','address':'jialidun'}


# 4、Get the length of the student dictionary
print(len(Students))

# 5、Get the value of skills and check the data type, it should be a list
# 获取技能值并检查数据类型，它应该是一个列表
skl = Students['skills']
print(skl)          #Java
print(type(skl))    # <class 'str'>

# 6、Modify the skills values by adding one or two skills
# 通过添加一个或两个技能来修改技能值
Students['skills'] = 'C++'

# 7、Get the dictionary keys as a list
print(Students.keys())

# 8、Get the dictionary values as a list
print(Students.values())

# 9、Change the dictionary to a list of tuples using items() method
# 使用items（）方法将字典更改为元组列表
print(Students.items())

# 10、Delete one of the items in the dictionary
# 删除字典中的一项
Students.pop('first_name')
print(Students)

# 11、Delete one of the dictionaries
del Students
print(Students)


































