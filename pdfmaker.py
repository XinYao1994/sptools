# -*- coding:utf-8 -*-
# pip2 install pandas
# pip2 install matplotlib

from pandas import *
import string
import matplotlib
import matplotlib.pyplot as plt  
import numpy as np

label = ["aofalways", "aofno", "aofsec", "IP", "NATIVE", "RDB"];
path_dir = "data/ipredis/"
def ipredis(opcode):
	x = [0, 0, 0, 0, 0, 0];
	if opcode == "read":
		for i in range(len(x)):
			f = open(path_dir + label[i] + "_" + opcode + ".txt", "r")
			str = f.read()
			strlist = str.split('\n')
			strlist = (strlist[::2])[0:4]
			num = 0;
			for j in range(len(strlist)):
				num += float(strlist[j].split('(')[1].split(' ')[0])
			x[i] = num / len(strlist);
	else :
		for i in range(len(x)):
			f = open(path_dir + label[i] + "_" + opcode + ".txt", "r")
			str = f.read()
			strlist = (str.split('\n'))[0:4]
			num = 0;
			for j in range(len(strlist)):
				num += float(strlist[j].split('(')[1].split(' ')[0])
			x[i] = num / len(strlist);
	return x;
	
	
# data = Series(ipredis("read"),index=list('abcde'))#label) #list('abcdefghijklmnop')
# print label
# print list('abcde')
# print data
# data.plot(kind = 'bar', color = 'k',alpha = 1)
plt.figure(figsize=(12,4))
ax = plt.subplot(121)
ax.set_title("read test");
plt.bar(range(6), ipredis("read"), tick_label=label)
# plt.show()
ax = plt.subplot(122)
ax.set_title("append test")
plt.bar(range(6), ipredis("append"), tick_label=label)

plt.show()
	
# Model for painting

# init the image size
# plt.figure(figsize=(4,2)) #image size
# matplotlib.rcParams["savefig.dpi"] save image size
# label: name of line  color: color of line  linewidth: the width of line
# the third parameter: "b--" means blue+"--"
# plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
# plt.plot(x,z,"b--",label="$cos(x^2)$")
# x = np.linspace(0, 10, 1000)
# y = np.sin(x)
# z = np.cos(x**2)

# Live2D
# line, = plt.plot(x, x*x)
# line.set_antialiased(False) do not use, it shows the point non-consensus

# setp methods
# lines = plt.plot(x, np.sin(x), x, np.cos(x))
# plt.setp(lines, color="r", linewidth=2.0)

# mul-pic

# 直方图
# mu = 100
# sigma = 20
# x = mu + sigma*np.random.randn(20000)
# plt.hist(x, bins = 100, color = 'green', normed = True)

# 条形图
# y = [20, 10, 30, 25, 15]
# index = np.arange(5)
# index = [1, 2, 3, 4, 5]
# plt.bar(left=index,height=y,color='green',width=0.5)

# 折线图
# x = np.linspace(-10,10,100)
# y = x**3
# plt.plot(x,y,linestyle='--',color='green',marker='.')

# 点的形状
#"."point","pixel"o"circle"v"triangle_down
#"^"triangle_up"<"triangle_left">"triangle_right"1"tri_down
#"2"tri_up"3"tri_left"4"tri_right"8"octagon
#"s"square"p"pentagon"*"star"h"hexagon1"H"hexagon2
#"+"plus"x"x"D"diamond"d"thin_diamond
# 颜色Color
#b:blue g:green r:red c:cyan
#m:magenta y:yellow k:black w:white
# 线的形状
#- 实线 --虚线 -.点划线 ：点线

# 子图
# plt.subplot(221) #2行2列第1个图
# plt.subplot(212) # 第二整行

# grid
# y = np.arange(1,5)
# plt.plot(y,y*2)
# plt.grid(True,color='g',linestyle='--',linewidth='1')

# legend
#x = np.arange(1,11,1)
#plt.plot(x, x*2)
#plt.plot(x, x*3)
#plt.plot(x, x*4)
#plt.legend(['Normal','Fast','Faster'])

# plt.xlabel("Time(s)")
# plt.ylabel("Volt")
# plt.title("PyPlot First Example")
# plt.ylim(-1.2,1.2)
# show the mark
# plt.legend()
# plt.show()

# using pandas
# 线形图
# 默认情况下，他们所生成的是线型图，该Series的索引会被传给matplotlib，并用于绘制x轴
# s = Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
# s.plot()
# plt.show(s.plot())
# df = DataFrame(np.random.randn(10,4).cumsum(0),columns=['A','B','C','D'],index=np.arange(0,100,10))
# plt.show(df.plot())
# 柱状图
# 在生成的线型图的代码中加上kind='bar'(垂直树状图)或 kind='barch'(水平柱状图)即可生成柱状图，
# 此时，Series和DataFrame的索引将会被用作X或Y的刻度。
# data = Series(np.random.rand(16),index=list('abcdefghijklmnop'))
# data.plot(kind = 'bar', color = 'k',alpha = 1)
# plt.show()
# data.plot(kind = 'bar', color = 'k',alpha = 0.5)
# plt.show()


# df = DataFrame(np.random.rand(6,4),index=['one','two','three','four','five','six'],columns=['A','B','C','D'])
# df.columns.name = 'Genus'
# plt.show(df.plot(kind='bar'))





