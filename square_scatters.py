import matplotlib.pyplot as plt

input_values=list(range(1,1001))
squares= [x**2 for x in input_values]
plt.scatter(input_values,squares,edgecolor="none",c=squares,cmap=plt.cm.Blues,s=20)
plt.title("Square Scatters", fontsize=22)
plt.xlabel("Values", fontsize=15)
plt.ylabel("Sqaures", fontsize=15)

plt.tick_params(axis="both", which="major", labelsize=15)






#save plots automatically 
#plt.savefig('scatter_squares.png',bbox_inches='tight')

plt.show()

