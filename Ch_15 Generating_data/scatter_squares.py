import matplotlib.pyplot as plt
import random
x_values = range(1,1000)
y_values = [x**2 for x in x_values] 

plt.style.use('seaborn')
fig,ax = plt.subplots()

#Set chart title and label axes 
ax.set_title("Square Numbers", fontsize = 14)
ax.set_xlabel("value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s = 10)
#Set size of tick labels 
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)
plt.show()         