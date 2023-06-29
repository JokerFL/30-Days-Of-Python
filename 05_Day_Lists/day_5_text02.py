# Exercises: Level 2

"""
1、The following is a list of 10 students ages:
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 2、Sort the list and find the min and max age

# 3、Add the min age and the max age again to the list

# 4、Find the median age (one middle item or two middle items divided by two)

# 5、Find the average age (sum of all items divided by their number )

# 6、Find the range of the ages (max minus min)

# 7、Compare the value of (min - average) and (max - average), use abs() method

"""
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# # 2、对列表进行排序，找到最小和最大年龄
# ages.sort()
# print(ages)
# print("最小年龄为：", ages[0])
# print("最大年龄为：", ages[len(ages) - 1])

# # 3、再次将最小年龄和最大年龄添加到列表中
#
# ages.insert(0, '19')
# ages.insert((len(ages) - 1), '26')
# print("插入最大值和最小值：", ages)

# # 4、找出年龄中位数（一个中间项目或两个中间项目除以二）
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorted_ages = sorted(ages)  # 对列表进行排序，默认顺序（加reverse = true，则表示倒序）
# print(sorted_ages)
# n = len(sorted_ages)
# if n % 2 == 1:  # 列表长度为奇数
#     median = sorted_ages[n // 2]  # 得到中间数的索引，该索引对应的就是中位数
# else:  # 列表长度为偶数
#     middle_right = n // 2  # 中间右侧元素的索引
#     middle_left = middle_right - 1  # 中间左侧元素的索引
#     median = (sorted_ages[middle_right] + sorted_ages[middle_left]) / 2  # 中位数是两个元素的平均值
# print(median)


# # 5、求平均年龄（所有项目的总和除以其数量）
# total = sum(ages)
# print(total)

# # 6、查找年龄范围（最大值减去最小值）
# sorted_ages = sorted(ages)
# max = sorted_ages[len(sorted_ages)-1]
# mix = sorted_ages[0]
# print("年龄范围：",max - mix)

# # 7、比较以下两个值：(最小值 - 平均值) 和 (最大值 - 平均值) 的值，使用abs（）方法
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# # 计算平均值
# average = sum(ages)/len(ages)
# # 计算差值
# min_diff = abs(min(ages) - average)
# max_diff = abs(max(ages) - average)
#
# print("最小值与平均值的差值：",min_diff)
# print("最大值与平均值的差值：",max_diff)


# # 1、Find the middle country(ies) in the countries list  在国家列表中查找中间国家
# countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
#
# # 获取国家列表的长度
# length = len(countries)
#
# # 确定中间位置的索引
# middle_index = length // 2
#
# # 使用索引获取中间的国家
# middle_country = countries[middle_index]
#
# print("Middle country:", middle_country)



# 2、Divide the countries list into two equal lists if it is even if not one more country for the first half.
# 将一个国家列表分成两个相等的列表（如果列表长度为偶数），或者第一半多一个国家（如果列表长度为奇数）

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n = len(countries)
half = n // 2

if n % 2 == 0:  # 列表长度为偶数
    first_half = countries[:half]
    second_half = countries[half:]
else:  # 列表长度为奇数
    first_half = countries[:half+1]
    second_half = countries[half+1:]

print(first_half)
print(second_half)



# 3、['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
# 将列表 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'] 的前三个国家解包为单独的变量，并将剩下的国家作为一个单独的列表（scandic_countries）。
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1,country2,country3,*scandic_countries = countries

print(country1)
print(country2)
print(country3)
print(scandic_countries)