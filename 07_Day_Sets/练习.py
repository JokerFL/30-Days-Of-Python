# expandtabs（）：用空格替换制表符，默认制表符大小为8。它采用制表符大小参数
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(12)) # 'thirty    days      of        python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

