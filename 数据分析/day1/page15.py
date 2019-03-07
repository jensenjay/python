from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

plt.figure(figsize=(20,8), dpi=100)
plt.xticks(x)
plt.plot(x,y)
plt.savefig('./page15.png')
plt.show()