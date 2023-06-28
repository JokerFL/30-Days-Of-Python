# 1、Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# 1、将字符串“Thirty”、“Days”、“Of”、“Python”连接为单个字符串“Thirdy Days Of Python”。
# a='Thirty'
# b='Days'
# c='Of'
# d='Python'
# space = ' '
# e = a+space+b+space+c+space+d
# print(e)

# 2、Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# 2、将字符串“Coding”、“For”、“All”连接为单个字符串“Coding For All”。
# a='Coding'
# b='For'
# c='All'
# space = ' '
# e = a+space+b+space+c
# print(e)


# 3、Declare a variable named company and assign it to an initial value "Coding For All".
# 3、声明一个名为company的变量，并将其赋给一个初始值“Coding For All”。
company = 'Coding For All'

# 4、Print the variable company using print().
# 4、使用Print（）打印可变公司。
print(company)

# 5、Print the length of the company string using len() method and print().
# 5、使用len（）方法和Print（）打印公司字符串的长度。
print(len(company))

# 6、Change all the characters to uppercase letters using upper() method.
# 6、使用upper（）方法将所有字符更改为大写字母。
print(company.upper())

# 7、Change all the characters to lowercase letters using lower() method.
# 7、使用lower（）方法将所有字符更改为小写字母。
print(company.lower())

# 8、Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# 8、使用capitalize（）、title（）、swapcase（）方法来格式化字符串Coding For All的值。
print(company.capitalize())  # 将字符串的首字母转换为大写，而将其他字符转换为小写。
print(company.title())  # 每个单词首字母大写
print(company.swapcase())  # 带小写反转

# 9、Cut(slice) out the first word of Coding For All string.
# 9、剪下“ Coding For All ”字符串的第一个单词。
cut = company[6:]
print("切割第一个单词：", cut)  # 切割第一个单词：  For All

# 10、Check if Coding For All string contains a word Coding using the method index, find or other methods.
# 10、使用方法index、find或其他方法检查“Coding For All”字符串是否包含单词“Coding”。
print(company.index('Coding'))  # 0 未报错
print(company.find('Coding'))  # 0 未显示-1

# 11、Replace the word coding in the string 'Coding For All' to Python.
# 11、将字符串“coding For All”中的单词coding替换为Python。
print(company.replace('Coding', 'Python'))

# 12、Change Python for Everyone to Python for All using the replace method or other methods.
# 12、使用replace方法或其他方法将Python for Everyone更改为Python for All。
company01 = 'Python for Everyone'
print(company01.replace('Everyone', 'All'))

# 13、Split the string 'Coding For All' using space as the separator (split()) .
# 13、使用空格作为分隔符拆分字符串“Coding For All”（Split（））。
company02 = 'Coding For All'
print("空格拆分：", company02.split())  # 空格拆分： ['Coding', 'For', 'All']
print("逗号拆分：", company02.split(","))  # 此处没有逗号  输出：空格拆分： ['Coding For All']
company03 = 'Coding,For,All'
print("03逗号拆分：", company03.split(","))  # 此处有逗号  输出：空格拆分： 03逗号拆分： ['Coding', 'For', 'All']

# 14、"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company04 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(company04.split(','))

# 15、What is the character at index 0 in the string Coding For All.
# 15、“Coding For All”字符串中索引0处的字符是什么。
string = "Coding For All"
character = string[0]
print(character)

# 16、What is the last index of the string Coding For All.
# 16、“Coding For All”这个字符串的最后一个索引是什么。
string = "Coding For All"
character = string[-1]
print(character)

# 17、What character is at index 10 in "Coding For All" string.
# 17、“Coding For All”字符串中索引10处的字符是什么。
string = "Coding For All"
character = string[10]
print("索引10处的字符是:", character)

# 18、Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python For Everyone'
words = phrase.split()
acronym = ''.join(word[0].upper() for word in words)
print("acronym:", acronym)  # PFE

# 19、Create an acronym or an abbreviation for the name 'Coding For All'.
phrase = 'Coding For All'
words = phrase.split()
acronym = ''.join(word[0].upper() for word in words)
print("acronym:", acronym)  # CFA

# 20、Use index to determine the position of the first occurrence of C in Coding For All.
# 20、使用索引来确定C在“Coding For All”中第一次出现的位置。
"""
使用index()方法或find()方法来查找字符"C"在字符串"Coding For All"中第一次出现的位置。返回的结果为索引值，表示该字符在字符串中的位置。在这种情况下，字符"C"位于索引0处，因此输出结果为0。
需要注意的是，如果指定的字符在字符串中不存在，index()方法将引发ValueError异常，而find()方法将返回-1。因此，在实际使用时，请根据需要进行适当的错误处理。
"""
# 方法一：
string = "Coding For All"
index = string.index("C")
print(index)  # 0

# 方法二：
string = "Coding For All"
index = string.find("C")
print(index)

# 21、Use index to determine the position of the first occurrence of F in Coding For All.
# 21、使用索引来确定“Coding For All”中F第一次出现的位置。
string = "Coding For All"
index = string.find("F")
print(index)

# 22、Use rfind to determine the position of the last occurrence of l in Coding For All People.
# 使用rfind确定l在Coding For All中最后一次出现的位置
string = "Coding For All"
index = string.rfind("l")
print(index)

# 23、Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 23.使用index或find查找单词“because”在以下句子中第一次出现的位置：“You cannot end a sentence with because because because is a conjunction”
string = 'You cannot end a sentence with because because because is a conjunction'
index = string.find("because")
print(index)

# 24、Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 24、用rindex查找单词“because”最后一次出现的位置在下面的句子中：“You cannot end a sentence with because because because is a conjunction”
"""
# rindex()和rfind()都是查找子字符串在字符串中最后一次出现的位置，不同的是，rindex()在所要查找的子字符串不存在是，是返回-1，而rfind()则是引发ValueError异常。
"""

string = 'You cannot end a sentence with because because because is a conjunction'
index = string.rfind("because")
print("最后一次：", index)

string = 'You cannot end a sentence with because because because is a conjunction'
try:
    index = string.rindex("because")
    print("最后一次：", index)
except ValueError:
    print("Substring not found")

# 25、Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 去掉”'You cannot end a sentence with because because because is a conjunction'“中的'because because because'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.replace('because because because', ''))

# 26、Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 26、在下面的句子中，找出单词“because”第一次出现的位置：“You cannot end a sentence with because because because is a conjunction”
string = 'You cannot end a sentence with because because because is a conjunction'
index = string.find("because")
print(index)
# 27、Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 27、删去下列句子中的短语“because because because”：“You cannot end a sentence with because because because is a conjunction”
print(string.replace('because because because', ''))

# 28、Does ''Coding For All' start with a substring Coding?
# 28.“Coding For All”是否以子字符串“Coding”开头？
string = 'Coding For All'
print(string.startswith('Coding'))

# 29、Does 'Coding For All' end with a substring coding?
string = 'Coding For All'
print(string.endswith('Coding'))

# 30、'Coding For All'  , remove the left and right trailing spaces in the given string.
# 30、'Coding For All'删除给定字符串中的左右尾部空格。
print(string.replace(' ', ''))

"""
31、Which one of the following variables return True when we use the method isidentifier():
        30DaysOfPython
        thirty_days_of_python
        isidentifier(): 检查有效的标识符-它检查字符串是否是有效的变量名
"""

challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False

challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True

# 32、The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# 以下列表包含一些python库的名称：['Django'，'Flask'，'Bottle'，'Pyramid'，'Falcon']。使用带有空格字符串的哈希加入列表。
"""
核心代码：libraries_with_hash = [library + ' #' for library in libraries]
在这行代码中，我们使用了一个循环for library in libraries来遍历给定列表libraries中的每个元素。
对于每个元素，我们使用library + ' #'将元素与空格字符串的哈希（#）进行拼接，并将结果添加到新的列表libraries_with_hash中。
"""

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
libraries_with_hash = [library + ' #' for library in libraries]
print(libraries_with_hash)

# 33、Use the new line escape sequence to separate the following sentences
# 使用换行符序列分隔下列句子
"""
I am enjoying this challenge.
I just wonder what is next.
"""
print("I\nam\nenjoying\nthis\nchallenge.")
print("I\njust\nwonder\nwhat\nis\nnext.")

# 34、 Use a tab escape sequence to write the following lines
# 使用制表符转义序列写入以下行
"""
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
"""
string = 'Name\tAge\tCountry\tCity'
word = string.expandtabs(10)
words = word.split('\t')
output = ' '.join(words)
print(output)


"""
让我们逐行解释这段代码的含义：

1. `string = 'Name\tAge\tCountry\tCity'`
   - 这行代码创建了一个字符串变量 `string`，其值为 `'Name\tAge\tCountry\tCity'`。该字符串包含了制表符 `\t` 分隔的四个单词：Name、Age、Country、City。

2. `words = string.split('\t')`
   - 这行代码使用字符串的 `split()` 方法，将 `string` 字符串根据制表符 `\t` 进行分割，并将分割后的单词存储在列表变量 `words` 中。每个制表符 `\t` 都被视为分割标志，用于将字符串拆分为多个单词。

3. `output = ' '.join(words)`
   - 这行代码使用列表的 `join()` 方法，将 `words` 列表中的单词连接成一个新的字符串。使用空格 `' '` 作为连接符，即在每个单词之间插入一个空格。

4. `print(output)`
   - 这行代码打印输出变量 `output` 的值，即连接后的字符串。每个单词之间都有一个空格，而不是原始字符串中的制表符。

综合起来，这段代码的目的是将包含制表符分隔的字符串拆分为单词列表，并使用空格将这些单词连接起来，以生成一个新的字符串。
新字符串中的每个单词之间都有一个空格分隔。输出结果是 `Name Age Country City`，其中每个单词之间都有一个空格。
这样的处理方式可以消除制表符并保持每个单词之间的空格一致。
"""


string = 'Asabeneh\t250\tFinland\tHelsinki'
word = string.expandtabs(10)
words = word.split('\t')
output = ' '.join(words)
print(output)


# Use the string formatting method to display the following:
# 使用字符串格式设置方法可以显示以下内容：
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""
