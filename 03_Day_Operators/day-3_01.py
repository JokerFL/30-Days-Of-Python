# print(True)
# print(False)

# 运算符
# print('Addition:', 1 + 2)
# print('Subtrction:', 2 - 1)
# print('Multiplication:', 2 * 3)
# print('Division:', 4 / 2)
# print('Division:', 7 / 2)
# print('Division without the remainder:', 7 // 2)  #Division without the remainder 表示不带余数的除法
# print('Division without the remainder:', 7 // 3)
# print('Modulus:', 3 % 2)
# print('Exponentiation:', 2 ** 3)  #表示2的3次方


# Float number
# print('Floating Point Number, PI',3.14)
# print('Multiplying complex number:',(1 + 1j)*(1-1j))

# Declaring the variable(声明变量)
# a = 3
# b = 2
# #Arithmetic operations(算术运算) and assigning the result to a variable(将结果分配给变量)
# total = a + b
# diff = a - b
# product = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponetial = a ** b
#
# #输出
# print(a)
# print(b)
# print(total)
# print('a+b=',total)
# print('a-b=',diff)
# print('a*b=',product)
# print('a/b=',division)
# print('a%b=',remainder)
# print('a//b=',floor_division)
# print('a**b=',exponetial)


# #Comparison Operators(比较运算符)
# print(3 > 2)     # True, because 3 is greater than 2
# print(3 >= 2)    # True, because 3 is greater than 2
# print(3 < 2)     # False,  because 3 is greater than 2
# print(2 < 3)     # True, because 2 is less than 3
# print(2 <= 3)    # True, because 2 is less than 3
# print(3 == 2)    # False, because 3 is not equal to 2
# print(3 != 2)    # True, because 3 is not equal to 2
# print(len('mango') == len('avocado'))  # False
# print(len('mango') != len('avocado'))  # True
# print(len('mango') < len('avocado'))   # True
# print(len('milk') != len('meat'))      # False
# print(len('milk') == len('meat'))      # True
# print(len('tomato') == len('potato'))  # True
# print(len('python') > len('dragon'))   # False


# # Comparing something gives either a True or False
#
# print('True == True: ', True == True)
# print('True == False: ', True == False)
# print('False == False:', False == False)
# #is,is not,in,not in的用法
# print('1 is 1', 1 is 1)                   # True - because the data values are the same
# print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
# print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
# print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
# print('coding' in 'coding for all') # True - because coding for all has the word coding
# print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 ** 2)   # True
#
# #and,or
# print(3 > 2 and 4 > 3) # True - because both statements are true
# print(3 > 2 and 4 < 3) # False - because the second statement is false
# print(3 < 2 and 4 < 3) # False - because both statements are false
# print('True and True: ', True and True)
# print(3 > 2 or 4 > 3)  # True - because both statements are true
# print(3 > 2 or 4 < 3)  # True - because one of the statements is true
# print(3 < 2 or 4 < 3)  # False - because both statements are false
# print('True or False:', True or False)
# print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
# print(not True)      # False - Negation, the not operator turns true to false
# print(not False)     # True
# print(not not True)  # True
# print(not not False) # False


# 练习一：Declare your age as integer variable(将你的年龄声明为整数变量)
import datetime

# age = 10

# 练习二：Declare your height as a float variable（身高声明为浮点变量）
# hight = 120.9

# 练习三：Declare a variable that store a complex number
# 1、实部是3，虚部是4
# z = complex(3, 4)
# 2、Python会认为3是实部，4j是虚部，其中j表示虚数单位
# z = 3 + 4j

# 练习四：Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# 练习四：编写一个脚本，提示用户输入三角形的底部和高度，并计算该三角形的面积（面积=0.5 x b x h）。
# bootom = float(input("请输入底部长度："))
# hight = float(input("请输入高度："))
# area = 0.5 * bootom * hight
# print(area)

# 练习五、Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# a = int(input("请输入三角形的第一条边："))
# b = int(input("请输入三角形的第二条边："))
# c = int(input("请输入三角形的第三条边："))
# perimeter = a + b + c
# print(perimeter)


# 练习六、Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# 使用提示获取矩形的长度和宽度。计算其面积（面积=长度x宽度）和周长（周长=2 x（长度+宽度））
# length = int(input("请输入矩形的长："))
# width = int(input("请输入矩形的宽："))
# area = length * width
# perimeter = (length + width) * 2
# print(area)
# print(perimeter)

# 练习七、Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# 使用提示获取圆的半径。计算面积（面积=pi x r x r）和周长（c=2 x pi x r），其中pi=3.14。
# radius = int(input("请输入圆的半径："))
# area = 3.14 * radius ** 2
# perimeter = 2 * radius * 3.14
# print(area)
# print(perimeter)

# 练习八、Calculate the slope, x-intercept and y-intercept of y = 2x -2
# 计算y=2x-2的斜率、x截距和y截距
# x = 0
# y_intercept = 2 * x - 2
# print("y的截距为：", y_intercept)
# y = 0
# x_intercept = (y + 2) / 2
# print("x的截距为：", x_intercept)
# # abs() 为绝对值
# slope = abs(y_intercept / x_intercept)
# print("斜率为：",slope)

# 练习九： Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# 斜率为（m=y2-y1/x2-x1）。求点（2，2）和点（6,10）之间的斜率和欧几里得距离
# 计算斜率
# m = (10 - 2) / (6 - 2)
# print("斜率为:", m)
#
# # 计算欧几里得距离{欧几里得距离公式：((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5}
# distance = ((6 - 2) ** 2 + (10 - 2) ** 2) ** 0.5
# print("欧几里得距离为:", distance)

# 练习10、Compare the slopes in tasks 8 and 9.
# 比较任务8和任务9中的斜率。
# a = 2.0
# b = 2.0
#
# if a < b:
#     print("a 小于 b")
# elif a > b:
#     print("a 大于 b")
# else:
#     print("a 等于 b")

# # 11、计算y的值（y = x ^ 2 + 6x + 9）。尝试使用不同的x值，并找出何时y的值为0。
# def equation(x):
#     return x ** 2 + 6 * x + 9
#
#
# # 这段代码使用for循环遍历数字-10到10（包括-10和10），并在每个数字上调用equation函数。如果调用结果等于0，则打印出相应的x值。注意，我们在字符串中使用了格式化字面值，使用{}括起来并在其中嵌入变量x的值。
# for x in range(-10, 10):
#     if equation(x) == 0:
#         print(f"x为{x}时，y的值为0")


# # 12、找到'python'和'dragon'的长度并进行虚假比较。
# string1 = 'python'
# string2 = 'dragon'
#
# if len(string1) == len(string2):
#     print("两者字符长度相等")
# elif len(string1) > len(string2):
#     print("python的长度大于dragon")
# else:
#     print("python的长度小于dragon")


# # 13、使用and运算符检查在'python'和'dragon'中是否都包含'on'。
# print('on' in 'python' and 'on' in 'dragon')


# 14、I hope this course is not full of jargon. 使用in运算符检查句子中是否包含'jargon'。
# print('jargon' in 'I hope this course is not full of jargon. ')


# # 15、在龙和蟒蛇( dragon and python)两者中均没有' on'。
# print('on' not in 'jragon' and 'python')

# # 16、找到文本python的长度并将该值转换为浮点数，然后将其转换为字符串。
# word = 'python'
# print(type(word))
# str1 = float(len(word))
# print(type(str1))
# str_char = str(str1)
# print(str_char)
# print(type(str_char))

# 17、偶数可以被2整除，余数为零。如何使用Python检查一个数字是偶数还是奇数？
# while True:
#     try:
#         num = int(input("请输入一个数字："))
#         if num % 2 == 0:
#             print("该数字为偶数！")
#             break
#         else:
#             print("该数字为奇数！")
#     except ValueError:
#         print("请输入有效数字！")

# 18、检查7除以3的“向下取整除法(//)”是否等于2.7的整数转换值。
# a = 7 // 3
# # 整数取整的两中方法：1、int（取整值）：向下取整 2、round（取整值）：四舍五入取整
# b = int(2.7)
# print(a == b)

# 19、检查'type('10')'是否等于'type(10)'。
# print(type('10') == type(10))  #False  str和int


# 20、检查int('9.8')是否等于10。
# print(int(float('9.8')) == 10)  # 向下取整   False
# print(int(round(float('9.8'))) == 10)  # 向上取整  True


# # 21、编写一个脚本，提示用户输入小时数和每小时费率。计算个人的工资？
# hours = int(input("请输入你的工作小时："))
# rate_per_hour = int(input("请输入你的时薪："))
# weekly_earning = hours * rate_per_hour
# print('你的薪资为：', weekly_earning)

#22、 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# # 获取当前日期
# now = 2023
#
# # 让用户输入出生年份
# birth_year = int(input("请输入您的出生年份："))
#
# # 计算一百年后的日期
# hundred_years_later = birth_year + 100
#
#
# residue_seconds = (hundred_years_later - now)*60*60*24*365
#
# print("您可以活", residue_seconds, "秒")


"""
23、Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
for i in range(1, 6):
    row = []
    for j in range(1, 6):
        if j == 1:
            row.append(str(i))
        elif j == 2:
            row.append("1")
        elif j == 3:
            row.append(str(i**2))
        elif j == 4:
            row.append(str(i**3))
        else:
            row.append(str(i**5))
    print(" ".join(row))

