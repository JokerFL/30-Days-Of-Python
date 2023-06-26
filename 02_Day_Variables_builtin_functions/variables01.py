import math

# python中的变量
first_name = 'joker'
last_name = 'kuang'
country = 'China'
city = 'beijing'
age = 20;
is_married = True
skills = ['HTML', 'css', 'js', 'React', 'Python']
person_info = {
    'firstname': 'joker',
    'lastname': 'kuang',
    'country': 'China',
    'city': 'beijing'
}

# 打印储存在变量中的值
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Person information:', person_info)

# 使用input()
# first_naem = input("What is your name:")
# age = input('How old are you?')

# print(first_naem)
# print(age)

# 数据类型
first_naem02 = 'jokk'
last_name = 'kk'
country = 'China'
age = 20

# 输出数据类型
print(type('China'))
print(type(first_name))
print(type(10))
print(type(3.14))
print(type(1 + 1j))  # complex
print(type(True))
print(type([1, 2, 3, 4]))  # list
print(type({'name': 'Asabeneh', 'age': 250, 'is_married': 250}))  # dict
print(type((1, 2)))  # tuple
print(type(zip([1, 2], [3, 4])))

# Using the len() built-in function, find the length of your first name
print('Last_name length:', len(last_name))  # kk

# Compare the length of your first name and your last name
if len(first_name) > len(last_name):
    print("firstname is longer than lastname")
elif len(first_name) < len(last_name):
    print("lastname is longer than firstname")
else:
    print("firstname and lastname have the same length")

"""
Declare 5 as num_one and 4 as num_two
  1、Add num_one and num_two and assign the value to a variable total
  2、Subtract num_two from num_one and assign the value to a variable diff
  3、Multiply num_two and num_one and assign the value to a variable product
  4、Divide num_one by num_two and assign the value to a variable division
  5、Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
  6、Calculate num_one to the power of num_two and assign the value to a variable exp
  7、Find floor division of num_one by num_two and assign the value to a variable floor_division
"""

# 1、Add num_one and num_two and assign the value to a variable total
num_one = 5
num_tow = 4
total = num_one + num_tow
print(total)

# 2、Subtract num_two from num_one and assign the value to a variable diff（从num_one减去num_two，并将其值赋给变量diff）
diff = num_one - num_tow
print(diff)

# 3、Multiply(相乘) num_two and num_one and assign the value to a variable product
product = num_one * num_tow
print(product)

# 4、Divide num_one by num_two and assign the value to a variable division
division = num_one / num_tow
print(division)

# 5、Use modulus division to find num_two divided by num_one and assign the value to a variable remainder(modulus division（取模除法）也被称为取余法)
remainder = num_one % num_tow
print(remainder)

# 6、Calculate num_one to the power of num_two and assign the value to a variable exp(计算num_one的num_two次方，并将其值赋给变量exp)
exp = num_one ** num_tow
print(exp)

# 7、Find floor division of num_one by num_two and assign the value to a variable floor_division(Floor division（地板除法）是一种除法运算，它返回除法的整数商，舍弃小数部分。)
floor_division = num_one // num_tow
print(floor_division)

"""
The radius of a circle is 30 meters.（一个圆形半径为30）
  1、Calculate the area of a circle and assign the value to a variable name of area_of_circle（求面积记为area_of_circle）
  2、Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle（记周长为circum_of_circle）
  3、Take radius as user input and calculate the area.(以半径作为用户输入，计算面积。)
"""

radius = 30
# 1、Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circie = math.pi * radius ** 2
print("圆的面积：",area_of_circie)

# 2、Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = math.pi * radius * 2
print("圆的周长：",circum_of_circle)

#3、Take radius as user input and calculate the area.(用input让用户输入半径大小)
# try:
#     radius01 = int(input("请输入圆的半径："))
#     area_of_circie01 = math.pi * radius01 ** 2
#     print(area_of_circie01)
# except ValueError:
#     print("无效的整数表示")
    
while True:
    try:
        radius01 = int(input("请输入圆的半径："))
        area_of_circie01 = math.pi * radius01 ** 2
        print(area_of_circie01)
        break
    except ValueError:
        print("无效的整数表示")



# 构造一个自定义半径的方法
def area_of_circle02(radius02):
    try:
        radius01 = int(input("请输入圆的半径："))
        area_of_circie01 = math.pi * radius01 ** 2
        print(area_of_circie01)
    except ValueError:
        print("无效的整数表示")

# 调用该函数
# area_of_circle02(12)

"""
1、Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
(使用内置的输入函数获取用户的姓、名、国家和年龄，并将值存储到相应的变量名中)
2、Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
(2、在Python shell或文件中运行help('keywords')来检查Python保留字或关键字)
"""

# 1、Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name03 = input("请输入你的姓：");
last_name03 = input("请输入你的名：");
country03 = input("请输入你的国家：");
age03 = int(input("请输入你的年龄；"));

#输出
print("用户的姓为：",first_name03)
print("用户的名为：",last_name03)
print("用户的国家为：",country03)
print("用户的年龄为：",age03)

# 2、Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

"""