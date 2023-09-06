from random import randint
import pygal
import matplotlib.pyplot as plt



class Die():

    def __init__(self, sides=6):
        self.sides=sides

    def roll(self):
        return randint(1,self.sides)

#roll a 6sided die and a 10sided die

die1 =Die()
die2 =Die()

results =[]
for num in range(36):
    result= die1.roll() * die2.roll()
    results.append(result)
print(results)

#analyze reults
freqs=[]
max_res= die1.sides * die2.sides
print(max_res)
for value in range(1,max_res+1):
    fre= results.count(value)
    freqs.append(fre)
print(freqs)


#visulaize the results

hist =pygal.Bar()
hist.title="Rolling a d6 and a d10  dice"
hist.x_label=["1","2","3","4","5","6","8","9","10","12","15","16","18","20","24","25","30","36"]
#hist.x_label=[x for x in range(1,37)]
hist.x_title="Result of roll"
hist.y_title="Frequency of the roll results"
 
hist.add('D6'+ 'D6',freqs)
hist.render_to_file("dice_visual.svg")

plt.bar(results,freqs,linewidth=5)
plt.xlabel('results')
plt.ylabel('frequency')
plt.show()
