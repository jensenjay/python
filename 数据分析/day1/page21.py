# coding=gbk
import random

from matplotlib import pyplot as plt, font_manager


my_font = font_manager.FontProperties(fname = "C:\Windows\Fonts\STXIHEI.TTF")

y = [random.randint(20, 35) for i in range(120)]
x = [i for i in range(120)]
plt.figure(figsize=(20,8))
_xticks = ["10��{}��".format(i) for i in range(60)]+["11��{}��".format(i) for i in range(60)]
plt.yticks(range(10,50,5))
plt.plot(x,y)
plt.xlabel("ʱ��",fontproperties = my_font)
plt.ylabel("�¶ȣ��棩",fontproperties = my_font)
plt.title("10�㵽12���ÿһ���ӵ�����",fontproperties = my_font)
plt.xticks(x[::3], _xticks[::3],fontproperties = my_font,rotation=270)
plt.grid(alpha=0.5,color = "red",linestyle=":")
plt.legend()
plt.show()