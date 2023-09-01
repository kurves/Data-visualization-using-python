
import matplotlib.pyplot as plt
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_values, squares,linewidth=6)


plt.title("square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("sqaures of Value", fontsize=14)
plt.tick_params(axis="both",labelsize=15)
plt.show()


