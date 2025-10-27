"""
20251003
程序是数据和指令的有序集合，写程序就是用数据和指令控制计算机做我们想让它做的事情

计算机的基础知识：
1）硬件系统：由5大部件构成，包括：运算器、控制器、存储器、输入设备和输出设备。
2）变量和类型：变量是数据的载体，是一块用来保存数据的内存空间，变量的值可以被读取和修改，是所有运算和控制的基础。
    1.整型（int）：
    2.浮点型（float）：浮点数，也就是小数，因为按照科学记数法表示时，一个浮点数的小数点位置是可变的
    3.字符串型（str）：字符串是以单引号或双绰号包裹起来的任意文本
    4.布尔型（bool）：布尔型只有Ture、False两种值，要么是True，要么是False
3)变量命名：
    1.规则1:变量名由字母、数字和下划线构成，数字不能开头，这里谫的字母指的是Unicode字符，Unicode称为万国码，但变量名尽量只使用英文字母；
    2.规则2:Python是大小写敏感的编程语言，大写和小写是两个不同的变量
    3.规则3:变量名不要跟Python的关键字重名，尽可能避开Python的保留字，
        例如is, if, else, for, while, True, False, int, print, input, str, math, os
    4.惯例1:变量名通常使用小写英文字母，多个单词用下划线进行连接；
    5.惯例2:受保护变量用单个下划线开头；
    6.惯例3:私有变量用两个下划线开头；

"""

"""
print("下面是整型int的示例")
print(0b100)
print(0o100)
print(100)
print(0x100)

print("下面是浮点型float的示例")
print(123.456)
print(1.23456e2)

print("下面是str的示例")
print('hello')
print("hello")
print('世界')

print("下面是bool的示例")
# print(Ture)
# print(False)
"""


#以下为变量的使用教程

"""
使用变量保存数据并进行加减乘除运算

a = 45
b = 12

print(a, b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
"""

"""
使用type函数检查变量的类型

a = 100
b = 123.45
c = 'hello world'
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
"""

"""
通过Python内置的函数来改变变量的类型，如
int(), 将一个数值或字符串转换成整数，可以指定进制；
float(), 将一个字符串（在可能的情况下）转换成浮点数；
str(), 将指定的对象转换成字符串形式，可以指定编码方式；
chr(), 将整数（字符编码）转换成对应的（一个字符）的字符串
ord()，将（一个字符的）字符串转换成对应的整数（字符编码）
"""

#变量的类型转换操作

a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello,wordk'
g = True

print(float(a))
print(int(b))
print(int(c))
print(int(c, base=16))
print(int(d, base=2))
print(float(e))
print(bool(f))
print(int(g))
print(chr(a))

# print(ord(d)) #ord() expected a character
print(ord('d'))