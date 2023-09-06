from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    def __init__(self,points=5000):
        self.points=points
        self.x=[0]
        self.y=[0]



    def get_step(self):
        while len(self.x) < self.points:
            if x_step:
                x_direction=choice([1,-3])
                x_distance=choice([0,1,2,3,4,5,6,7,8,9,10])
                x_step=x_direction * x_distance
                next_x = self.x[-1] + x_step
                self.x.append(next_x)

            elif x_step:
                
                y_direction = choice([1,-3])
                y_distance = choice([0, 1, 2, 3, 4,5,6,7,8,9,10])
                y_step = y_direction * y_distance
                next_y = self.y[-1] + y_step
                self.y.append(next_y)





  
    # choosing the directions
    def fillwalk(self):
        '''while len(self.x) < self.points:
            x_direction=choice([1,-3])
            x_distance=choice([0,1,2,3,4,5,6,7,8,9,10])
            x_step=x_direction * x_distance

            y_direction = choice([1,-3])
            y_distance = choice([0, 1, 2, 3, 4,5,6,7,8,9,10])
            y_step = y_direction * y_distance

            if x_step ==0 & y_step==0:
                continue
            #calculate the nextmoves

            next_x = self.x[-1] + x_step
            next_y = self.y[-1] + y_step

            self.x.append(next_x)
            self.y.append(next_y)'''

            #plotting the random walk
        x_step= RandomWalk.get_step()
        y_step= RandomWalk.get_step()

rw = RandomWalk()
rw.fillwalk()
plt.plot(rw.x,rw.y, linewidth=15)
#plt.savefig('randomwalk.png')
plt.show()