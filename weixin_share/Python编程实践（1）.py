# -*- coding: utf-8 -*-
# 作者：数据化分析
# 版本：1.0
# 书名：《Python编程：从入门到实践》
# 使用Python版本：Python 3
# 代码：「第 2 章 变量和简单数据类型 」的〖动手试一试〗

# 2-3 个性化消息: 将用户的姓名存到一个变量中，
# 并向该用户显示一条消息。
# 为方便输入，个人喜欢用单引号定义字符串
wxid = 'isjhfx'
print('您好，欢迎关注「数据化分析」，' +
      '微信号：' + wxid)
# ---运行结果---
# 您好，欢迎关注「数据化分析」，微信号：isjhfx

# 2-4 调整名字的大小写: 将一个人名存储到一个变量中，
# 再以小写、大写和首字母大写的方式显示这个人名。
name = 'jimmy'
print(name.lower())
print(name.upper())
print(name.title())
# ---运行结果---
# jimmy
# JIMMY
# Jimmy

# 2-5 名言: 找一句你钦佩的名人说的名言，
# 将这个名人的姓名和他的名言打印出来。
# 如果要输出双引号，那么外面用单引号，反之亦然
print('马克思曾经说过：' +
      '“友谊像清晨的雾一样纯洁, ' +
      '奉承并不能得到友谊, ' +
      '友谊只能用忠实去巩固它。” ')
# ---运行结果---
# 马克思曾经说过：“友谊像清晨的雾一样纯洁, 奉承并不能得到友谊, 友谊只能用忠实去巩固它。”

# 2-6 名言2: 重复练习2-5，
# 但将名人的姓名存储在变量famous_person 中，
famous_person = '马克思'
# 再创建要显示的消息，
# 并将其存储在变量message 中，然后打印这条消息。
# 为了方便在手机上显示，用\续行
message = '曾经说过：' + \
          '“友谊像清晨的雾一样纯洁, ' + \
          '奉承并不能得到友谊, ' + \
          '友谊只能用忠实去巩固它。” '
print(famous_person + message)
# ---运行结果---
# 马克思曾经说过：“友谊像清晨的雾一样纯洁, 奉承并不能得到友谊, 友谊只能用忠实去巩固它。”

# 2-7 剔除人名中的空白: 存储一个人名，
# 并在其开头和末尾都包含一些空白字符。
# 务必至少使用字符组合"\t" 和"\n" 各一次。
one_person = " \t \n  \t 数据化分析  \n"
# 打印这个人名，以显示其开头和末尾的空白。
print(one_person)
# ---运行结果---
#
#       数据化分析
#

# 分别使用剔除函数lstrip() 、rstrip() 和strip()
# 对人名进行处理，并将结果打印出来。
print(one_person.lstrip())
# ---运行结果---
# 数据化分析
#
print(one_person.rstrip())
# ---运行结果---
#
#       数据化分析
print(one_person.strip())
# ---运行结果---
# 数据化分析

# 2-8 数字8: 编写4个表达式，
# 分别使用加法、减法、乘法和除法运算，但结果都是数字8。
print(2 + 6)
print(10 - 2)
print(1 * 8)
# ---运行结果---
# 8
print(16 / 2)
# ---运行结果---
# 8.0

# 2-9 最喜欢的数字: 将你最喜欢的数字存储在一个变量中，
# 再使用这个变量创建一条消息，
# 指出你最喜欢的数字，然后将这条消息打印出来。
favorite_number = 6
print("我最喜欢的数字是：" + str(favorite_number))
# ---运行结果---
# 我最喜欢的数字是：6

# 2-10 添加注释: 选择你编写的两个程序，
# 在每个程序中都至少添加一条注释。

# 2-11 Python之禅:
# 在Python终端会话中执行命令import this ，
# 并粗略地浏览一下其他的指导原则。
# 个人喜欢这句话：Simple is better than complex.
import this

# ---运行结果---
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# 翻译成中文如下：
#
# Python之禅
# 作者：Tim
# Peters
# 翻译：数据化分析（基于网络版本修改）
#
# 优美胜于丑陋（Python以编写优美的代码为目标）
#
# 明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
#
# 简洁胜于繁琐（优美的代码应当是简洁的，不要有繁琐的内部实现）
#
# 繁琐胜于难懂（如果繁琐不可避免，那代码间也不要有难懂的关系）
#
# 扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
#
# 稀疏胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
#
# 可读性很重要（优美的代码是可读的）
#
# 即使特例很实用，也不可破坏这些规则（这些规则至高无上）
#
# 不要忽略任何错误，除非你确定需要这样做（精准地捕获异常）
#
# 当存在模棱两可的时候，不要尝试去猜测
#
# 而是尽量找一种明显的解决方案（如果不确定，就用穷举法）
#
# 虽然这很不容易，因为你不是Python之父
#
# 做好过不做，但也不要瞎做（动手之前要认真思考）
#
# 如果某个方案难以解释，那肯定不是一个好方案
#
# 反之亦然（方案测评标准）
#
# 多加应用命名空间，这是一个好主意（倡导与号召）
