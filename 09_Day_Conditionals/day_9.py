"""
条件
默认情况下，Python脚本中的语句从上到下依次执行。如果处理逻辑需要，则可以通过两种方式更改执行的顺序流程：
条件执行：如果某个表达式为true，则执行一个或多个语句块
重复执行：只要某个表达式为真，一个或多个语句块就会被重复执行。在本节中，我们将介绍if、else和elif语句。我们在前几节中学习到的比较运算符和逻辑运算符在这里会很有用。

如果条件
在python和其他编程语言中，关键字if用于检查条件是否为真并执行块代码。记住冒号后面的缩进。
"""
# # syntax
# condition = True
#
# if condition:
#     # 当条件为真时执行以下代码块
#     print("这部分代码在条件为真时运行")
#     # 可以在这里添加更多代码
#
# # 可以在这里添加其他代码


# a = 3
# if a > 0:
#     print('A is a positive number')
# A is a positive number

"""
正如您在上面的示例中看到的，3大于0。条件为true，并执行了块代码。
但是，如果条件为false，则我们看不到结果。为了看到虚假条件的结果，我们应该有另一个块，它将是else。
"""

"""
if else
如果条件为true，则执行第一个块，否则运行else条件。
"""
# a = 3
# if a < 0:
#     print('A is a negative number')
# else:
#     print('A is a positive number')
"""
上面的条件证明是错误的，因此执行了else块。如果我们的情况超过两个呢？我们可以用-elif。
"""


"""
如果Elif Else
在我们的日常生活中，我们每天都在做决定。我们不是通过检查一个或两个条件，而是通过检查多个条件来做出决定。
和生活一样，编程也是充满条件的。当我们有多个条件时，我们使用elif。
"""
# a = 0
# if a > 0:
#     print('A is a positive number')
# elif a < 0:
#     print('A is a negative')
# else:
#     print('A is zero')


"""
简写语法格式：
"""
# syntax
# code if condition else code

# a = 3
# print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed


"""
嵌套条件
条件可以嵌套
"""
# a = 3
# if a > 0:
#     if a % 2 == 0:
#         print('A is a positive and even integer')
#     else:
#         print('A is a positive number')
# elif a == 0:
#     print('A is zero')
# else:
#     print('A is a negative number')
#我们可以通过使用逻辑运算符和来避免编写嵌套条件。


"""
if语句和逻辑判断符
"""
a = -4
if a > 0 and a % 2 == 0:
    print('A is an even an positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')


"""
if and or 逻辑运算符
"""
# user = 'James'
# access_level = 3
# if user == 'admin' or access_level >= 4:
#     print('Access granted!')
# else:
#     print('Access denied!')













































































