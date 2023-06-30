# Exercises: Level 1
# # 1、Create an empty tuple
# tpl = ()

# # 2、Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# sisters_and_brothers = ('Tom','Emma','John','Liam')

# # 3、Join brothers and sisters tuples and assign it to siblings
# brothers = ("John", "Tom")
# sisters = ("Emma", "Lily")
# siblings = brothers + sisters
#
# print(siblings)


# # 4、How many siblings do you have?
# print(len(sisters_and_brothers))


# # 5、Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# father = "dad"
# mother = "mon"

# # 注意：只能元组与元组相加
# family_members = sisters_and_brothers+(father,mother)
# print(family_members)

# Exercises: Level 2
# # 1、Unpack siblings and parents from family_members  从家庭成员中拆封兄弟姐妹和父母
# sisters_and_brothers = family_members[0:4]
# parents = family_members[4:6]
#
# print(sisters_and_brothers)
# print(parents)

# 2、Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple','banana','pear')
vegetable = ('potato','tomato','onion')
animal = ('pig','dog','cat')
food_stuf_tp = fruits + vegetable + animal
print(food_stuf_tp)


# 3、Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuf_lt = list(food_stuf_tp)
print(food_stuf_lt)


# 4、Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
long = len(food_stuf_lt)
print(long)
print("中间一项:",food_stuf_lt[long // 2])


# 5、Slice out the first three items and the last three items from food_staff_lt list
# 从food_staff_lt列表中切下前三项和后三项
frist_three = food_stuf_lt[0:3]
next_three = food_stuf_lt[-4:-1]
print("前面三项：",frist_three)
print("后面三项：",next_three)

# 6、Delete the food_staff_tp tuple completely   完全删除food_staff_tp元组
del food_stuf_tp


"""
Check if an item exists in tuple: 检查元组中是否存在项：
Check if 'Estonia' is a nordic country  检查“爱沙尼亚”是否为北欧国家

Check if 'Iceland' is a nordic country  检查“冰岛”是否为北欧国家
"""
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# 1、Check if 'Estonia' is a nordic country  检查“Estonia”是否为北欧国家
print('Estonia' in nordic_countries)   #False


# 2、Check if 'Iceland' is a nordic country  检查“Iceland”是否为北欧国家
print('Iceland' in nordic_countries)  #True