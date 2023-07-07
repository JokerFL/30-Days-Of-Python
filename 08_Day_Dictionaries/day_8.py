
"""
字典
字典是无序的、可修改的(可变的)成对(键:值)数据类型的集合。

创建字典
要创建字典，可以使用大括号、{}或dict()内置函数。
"""
# syntax
empty_dict = {}
# Dictionary with data values   带有数据值的字典
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
# 上面的字典显示，值可以是任何数据类型:字符串、布尔值、列表、元组、集合或字典。


"""
字典的长度
它检查字典中'key: value'对的数量。
"""
# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(len(dct)) # 4
#
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
# print(len(person)) # 7


"""
访问字典项
我们可以通过引用它的键名来访问Dictionary项。
"""
# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct['key1']) # value1
# print(dct['key4']) # value4
#
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript','React','Node','MongoDB','Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# print(person['first_name'])     #Asabeneh
# print(person['country'])        #Finland
# print(person['skills'])         #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
# print(person['skills'][0])      #JavaScript
# print(person['address']['street'])  #Space street
# print(person['city'])           #KeyError: 'city'


"""
如果键不存在，则按键名访问项会引发错误。
为了避免这个错误，我们首先必须检查一个键是否存在，或者我们可以使用get方法。
如果键不存在，get方法返回None，这是一个NoneType对象数据类型。
"""
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
# print(person.get('first_name')) # Asabeneh
# print(person.get('country'))    # Finland
# print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
# print(person.get('city'))   # None


"""
向字典中添加项目
我们可以向字典中添加新的键值对
"""
# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct['key5'] = 'value5'
#
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#         }
# }
# person['job_title'] = 'Instructor'
# person['skills'].append('HTML')
# print(person)


"""
修改字典中的项
我们可以修改字典中的项目
"""
# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct['key1'] = 'value-one'
#
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
# person['first_name'] = 'Eyob'
# person['age'] = 252
# print(person)


"""
检查字典中的关键字
我们使用in运算符来检查字典中是否存在关键字
"""
# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print('key2' in dct) # True
# print('key5' in dct) # False


"""
从字典中删除键值对
pop（key）：删除具有指定键名称的项：
popitem（）：删除最后一项
del：删除具有指定密钥名称的项
"""
# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct.pop('key1') # removes key1 item
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct.popitem() # removes the last item
# del dct['key2'] # removes key2 item
#
#
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
# person.pop('first_name')        # Removes the firstname item
# print(person)
# person.popitem()                # Removes the address item
# print(person)
# del person['is_married']        # Removes the is_married item
# print(person)                   # KeyError: 'is_married'


"""
将字典更改为项目列表
items（）方法将dictionary更改为元组列表。
"""
# #syntax
# dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
# print(dct.items())


"""
清除词典
如果我们不想要字典中的项，我们可以使用clear（）方法来清除它们
"""
# #syntax
# dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
# print(dct.clear())      #None


"""
删除词典
如果我们不使用这本字典，我们可以把它完全删除
"""
# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# del dct


"""
复制词典
我们可以使用copy（）方法复制字典。使用复制可以避免原词典的变异。
"""
# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct_copy)


"""
将字典键作为列表获取
keys（）方法将字典的所有键作为列表提供给我们。
"""
# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# keys = dct.keys()
# print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])


"""
将字典值作为列表获取
values方法将字典中的所有值作为列表提供给我们。
"""
# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# values = dct.values()
# print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])









































