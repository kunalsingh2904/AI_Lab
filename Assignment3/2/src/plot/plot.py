import matplotlib.pyplot as plt

x = list(range(100))
temp = 1000
y = []

for time in x:
    y.append(temp)
    temp = temp - ((time / 100) ** 2)

plt.plot(x,y)
plt.savefig('temp3.png')
