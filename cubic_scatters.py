
import matplotlib.pyplot as plt

input_value=[1,2,3,4,5]
cubes=[1,8,27,64,125]
plt.scatter(input_value,cubes,c=cubes,cmap=plt.cm.Purples)

plt.title("cubic scatters",fontsize=15)
plt.xlabel("Values",fontsize=15)
plt.ylabel("cubes",fontsize=15)
plt.tick_params(axis='both',which='major',labelsize=15)


plt.show()
