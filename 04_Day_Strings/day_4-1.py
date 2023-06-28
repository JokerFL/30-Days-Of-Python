# letter = 'p'
# print(letter)
# print(len(letter))
# greeting = 'hello,world!'
# print(greeting)
# print(len(greeting))
# sentence = "I hope you are enjoying 30 day of Python Challenge"
# print(sentence)
#
# # 多行字符串是使用三个单引号（''）或三个双引号（“”）创建的。
# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)
# # Another way of doing the same thing
# multiline_string = """I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python."""
# print(multiline_string)

# #字符串连接
# first_name = 'joker'
# last_name = 'kuang'
# space = ' '
# full_name = first_name+space+last_name
# print(full_name)  #joker kuang
# print(len(first_name))  #5
# print(len(last_name))  #5
# print(len(first_name) > len(last_name))  #False
# print(len(full_name))  #11


# # 转义字符
# print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break 换行
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces 一个tab距离或者4个空格距离
# print('Day 1\t3\t5')
# print('Day 2\t3\t5')
# print('Day 3\t3\t5')
# print('Day 4\t3\t5')
# print('This is a backslash symbol (\\)')  #To write a backslash
# print('In every programming language it starts with \"Hello,world!\"')  # to write a double quote inside a single quote(在单引号中加双引号)

# # Strings only
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# format_string = 'I am %s %s. I teach %s' %(first_name,last_name,language)
# print(format_string)

# #Strings and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# format_string = 'The area of circle with a radius %d is %.2f.'%(radius,area)
# print(format_string)
#
# python_libraries = ['Django','Flask','NumPy','Matplotlib','Pandas']
# format_string = 'The following are python libraries:%s'%(python_libraries)
# print(format_string)

# # 新的字符串格式  （str.format）
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# format_string = 'I am {} {}.I teach {}'.format(first_name, last_name, language)
# print(format_string)
#
# a = 4
# b = 3
# print('{}+{}={}'.format(a, b, a + b))
# print('{} / {} = {:.2f}'.format(a, b, a / b))


# # f-字符串
# a = 4
# b = 3
# print(f'{a}+{b}={a + b}')
# print(f'{a}/{b}={a/b:.2f}')

# python字符串的字符序列
# language = 'Python'
# a,b,c,d,e,f = language # unpacking sequence characters into variables
# print(a) # P
# print(b) # y
# print(c) # t
# print(d) # h
# print(e) # o
# print(f) # n
#
# language = 'Python'
# first_letter = language[0]
# print(first_letter)
# second_letter = language[1]
# print(second_letter)
# last_index = len(language) - 1
# last_letter = language[last_index]
# print(last_letter)


# # #分割字符串
# language = 'Python'
# first_three = language[0:3]  #[0,3)
# print(first_three)
# last_three = language[3:6]
# print(last_three)
# # Another way
# last_three = language[-3:]  #同样表示后三个字符([-3:]表示从倒数第3个字符开始到末尾的子字符串。)
# print(last_three)
# last_three = language[3:]  #[3:] 表示从索引3开始到末尾的子字符串。
# print(last_three)


# # Reversing a String(反转字符)
# # [::] 切片操作符 [开始位置:结束位置:步长]
# greeting = 'Hello,World!'
# print(greeting[::-1]) #表示从greeting这个字符串中提取一个子序列，该子序列包含了原始字符串的所有字符，并以相反的顺序排列


# #切片时跳过字符 Skipping Characters While Slicing
# language = 'Python'
# pto = language[0:6:2]
# print(pto)


# #capitalize（）：将字符串的第一个字符转换为大写字母
# challenge = 'thirty days of python'
# print(challenge.capitalize()) # 'Thirty days of python'


# #count（）：返回字符串count中出现的子字符串（substring，start=..，end=..）。
# # start是计数的起始索引，end是最后一个计数的索引。
# #count()方法区分大小写，在列表中计算特定元素、字符的出现次数：
# challenge = 'thirty days of python'
# print(challenge.count('y'))  #3
# print(challenge.count('y',7,14))  #1
# print(challenge.count('th')) #2


# # endswitch（）：检查字符串是否以指定的结尾结束
# challenge = 'thirty days of python'
# print(challenge.endswith('on'))   # True
# print(challenge.endswith('ton')) # False


# # expandtabs（）：用空格替换制表符，默认制表符大小为8。它采用制表符大小参数
# challenge = 'thirty\tdays\tof\tpython'
# print(challenge.expandtabs())   # 'thirty  days    of      python'
# print(challenge.expandtabs(12)) # 'thirty    days      of        python'
# print(challenge.expandtabs(10)) # 'thirty    days      of        python'


## find（）：返回子字符串第一次出现的索引，如果未找到，则返回-1
# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0


# # rfind（）：返回子字符串最后一次出现的索引，如果未找到，则返回-1
# challenge = 'thirty days of python'
# print(challenge.rfind('y'))  # 16
# print(challenge.rfind('th'))  # 17
# print(challenge.rfind('tch'))  # -1

# # format（）：将字符串格式化为更好的输出
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# age = 250
# job = 'teacher'
# country = 'Finland'
# sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
# print(sentence)


# # index（）：返回子字符串的最低索引，其他参数指示起始索引和结束索引（默认为0，字符串长度为-1）。
# # 如果未找到子字符串，则会引发一个值Error。
# challenge = 'thirty days of python'
# sub_string = 'da'
# print(challenge.index(sub_string))
# print(challenge.index(sub_string,9))  #error 报错


# isalnum（）：检查字母数字字符  字符串只包含字母和数字字符：输出True 含有其他字符输出false
# challenge = 'ThirtyDaysPython'
# print(challenge.isalnum()) # True
#
# challenge = '30DaysPython'
# print(challenge.isalnum()) # True
#
# challenge = 'thirty days of python'
# print(challenge.isalnum()) # False, space is not an alphanumeric character
#
# challenge = 'thirty days of python 2019'
# print(challenge.isalnum()) # False


# # isalpha（）：检查所有字符串元素是否都是字母字符（a-z和A-Z）
# challenge = 'thirty days of python'
# print(challenge.isalpha()) # False, space is once again excluded
# challenge = 'ThirtyDaysPython'
# print(challenge.isalpha()) # True
# num = '123'
# print(num.isalpha())      # False



# #isdecimal(): Checks if all characters in a string are decimal (0-9)
# challenge = 'thirty days of python'
# print(challenge.isdecimal())  # False
# challenge = '123'
# print(challenge.isdecimal())  # True
# challenge = '\u00B2'
# print(challenge.isdigit())   # False
# challenge = '12 3'
# print(challenge.isdecimal())  # False, space not allowed


# # isdigit（）：检查字符串中的所有字符是否都是数字（0-9和其他一些unicode字符表示数字）
# challenge = 'Thirty'
# print(challenge.isdigit())
# challenge = '30'
# print(challenge.isdigit())
# # "\u00B2"代表Unicode字符编码的表示形式。具体地说，它表示上标数字 "2" 可以表示平方  5\u00B2等于5**2等于25
# challenge = '\u00B2'
# print(challenge.isdigit())


# # isnumeric（）：检查字符串中的所有字符是数字还是与数字相关
# # 就像isdigit（）一样，只接受更多符号，比如½）
# num = '10'
# print(num.isnumeric()) # True
# num = '\u00BD' # ½
# print(num.isnumeric()) # True
# num = '10.5'
# print(num.isnumeric()) # False


# # isidentifier（）：检查有效的标识符-它检查字符串是否是有效的变量名
# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, because it starts with a number
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True


# # islow（）：检查字符串中的所有字母字符是否都是小写
# challenge = 'thirty days of python'
# print(challenge.islower()) # True
# challenge = 'Thirty days of python'
# print(challenge.islower()) # False



# # isupper（）：检查字符串中的所有字母字符是否为大写
# challenge = 'thirty days of python'
# print(challenge.isupper()) #  False
# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper()) # True


# # join（）：返回连接的字符串
# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = ' '.join(web_tech)
# print(result) # 'HTML CSS JavaScript React'
#
# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = '# '.join(web_tech)
# print(result) # 'HTML# CSS# JavaScript# React'


# #strip（）：删除从字符串开头和结尾开始的所有给定字符
# challenge = 'thirty days of pythoonnn'
# print(challenge.strip('noth')) # 'irty days of py'


# # replace（）：用给定字符串替换子字符串  经coding替代python
# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding')) # 'thirty days of coding'


# # split（）：使用给定的字符串或空格作为分隔符拆分字符串
# # 默认是以空格进行分割
# challenge = 'thirtydays of python'
# print(challenge.split()) # ['thirty', 'days', 'of', 'python']
# # 以逗号进行分割
# challenge = 'thirty, days, of, python'
# print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']


# # title（）：返回带标题大小写的字符串
# # 每个代词首字母大写
# challenge = 'thirty days of python code'
# print(challenge.title()) # Thirty Days Of Python


# # swapcase（）：将所有大写字符转换为小写字符，将所有小写字符转换为大写字符
# challenge = 'thirty days of python'
# print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
# challenge = 'Thirty Days Of Python'
# print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON


# # startswitch（）：检查字符串是否以指定字符串开头
# challenge = 'thirty days of python'
# print(challenge.startswith('thirty')) # True
#
# challenge = '30 days of python'
# print(challenge.startswith('thirty')) # False











































