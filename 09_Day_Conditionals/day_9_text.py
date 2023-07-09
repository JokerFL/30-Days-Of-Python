"""
1、Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
If below 18 give feedback to wait for the missing amount of years. Output:
使用输入获取用户输入（“输入您的年龄：”）。
若用户年龄在18岁或以上，请给出反馈：您已经足够大，可以开车了。
如果18岁以下给出反馈，等待失踪的年数。输出：

示例：
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.

"""
# age = int(input("输入您的年龄："))
# if age >= 18:
#     print("您已经足够大，可以开车了")
# else:
#     print("你还需要等待",18-age,"年才能开车")


"""
使用if…else比较my_age和your_age的值。谁年纪大（我还是你）？使用输入（“输入您的年龄：”）获取年龄作为输入。
如果年龄相差1岁，可以使用嵌套条件打印“年”，如果年龄相差较大，可以使用“年”；
如果my_age=your_age，则可以使用自定义文本。输出：
Enter your age: 30
You are 5 years older than me.
"""
# my_age = 25
# your_age = int(input("请输入您的年龄："))
# if your_age > my_age:
#     print("你比我大",your_age - my_age,"岁")
# elif your_age == my_age:
#     print("你和我的年龄一样大！")
# else:
#     print("你比我小",my_age - your_age,"岁")


"""
使用输入提示从用户处获取两个数字。如果a大于b返回a大于b，如果a小于b返回a小于b，否则a等于b。输出：
Enter number one: 4
Enter number two: 3
4 is greater than 3
"""
# a = int(input("请输入第一个数字："))
# b = int(input("请输入第二个数字："))
# if a == b:
#     print("a等于b")
# elif a > b:
#     print("a大于b")
# else:
#     print("a小于b")


"""
写一个代码，根据学生的分数给他们打分：
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
# score = int(input("请输入学生得分："))
# if score >= 80 and score <= 100:
#     print("学生成绩为：A")
# elif score >= 70 and score < 80:
#     print("学生成绩为：B")
# elif score >= 60 and score < 70:
#     print("学生成绩为：C")
# elif score >=50 and score <60:
#     print("学生成绩为：D")
# else:
#     print("学生成绩为：F")


"""
检查季节是秋季、冬季、春季还是夏季。
如果用户输入为：9月、10月或11月，则季节为秋季。
十二月、一月或二月，季节是冬天。
三月、四月或五月，季节是春天
六月、七月或八月，季节是夏天
"""
# month = int(input("请输入当前的月份："))
# if month == 9 or month == 10 or month == 11:
#     print("当前季节是秋季！")
# elif month == 12 or month == 1 or month == 2:
#     print("当前季节是冬季！")
# elif month == 3 or month == 4 or month == 5:
#     print("当前季节是春季！")
# elif month == 6 or month == 7 or month == 8:
#     print("当前季节是夏季！")
# else:
#     print("您输入的数值有误！")


"""
以下列表包含一些水果：
fruits = ['banana', 'orange', 'mango', 'lemon']
如果列表中不存在水果，请将该水果添加到列表中并打印修改后的列表。如果水果存在，请打印（“该水果已存在于列表中”）
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input("请输入水果名称：")
# if fruit in fruits:
#     print("该水果已存在于列表中")
# else:
#     fruits.append(fruit)
#     print(fruits)


"""
这里有一本人名词典。请随意修改！
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
    
1、检查个人字典是否有技能键，如果有，请打印出技能列表中的中间技能。
2、检查人员字典是否有技能键，如果有，检查人员是否有“Python”技能并打印出结果。
3、如果一个人的技能只有JavaScript和React，打印（“他是前端开发人员”），如果该个人的技能有Node、Python、
   MongoDB，打印（‘他是后端开发人员’），如果此人的技能有React、Node和MongoDB，则打印（“她是全栈开发人员’”），
   否则打印（“未知标题”）-为了获得更准确的结果，可以嵌套更多条件！
4、如果此人已婚且居住在芬兰，请按以下格式打印信息：Asabeneh Yetayeh住在芬兰。他结婚了
"""

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# 1、检查个人字典是否有技能键，如果有，请打印出技能列表中的中间技能。
if 'skills' in person:
    skills_list = person['skills']
    print(skills_list)
else:
    print("该个人字典没有skills键。")

# 2、检查人员字典是否有技能键，如果有，检查人员是否有“Python”技能并打印出结果。
if 'skills' in person:
    if 'Python' in skills_list:
        print("该人员skills中有‘Python’")
    else:
        print("该人员skills中没有‘Python’")
else:
    print("该人员没有skills")

"""
3、如果一个人的技能只有JavaScript和React，打印（“他是前端开发人员”），如果该个人的技能有Node、Python、
   MongoDB，打印（‘他是后端开发人员’），如果此人的技能有React、Node和MongoDB，则打印（“她是全栈开发人员’”），
   否则打印（“未知标题”）-为了获得更准确的结果，可以嵌套更多条件！
"""
if 'JavaScript' in skills_list and 'React' in skills_list:
    print("他是前端开发人员")
elif 'Node' in skills_list and 'Python' in skills_list and 'MongoDB' in skills_list:
    print("他是后端开发人员")
elif 'React' in skills_list and 'Node' in skills_list and 'MongoDB' in skills_list:
    print("她是全栈开发人员")
else:
    print("未知标题")
