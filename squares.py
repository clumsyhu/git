from random import choice
import matplotlib.pyplot as plt
class Randomwalk():
    def __init__(self,point=5000):
        self.point=point
    def walk(self):
        self.x_values=[0]
        self.y_values=[0]
        while len(self.x_values)<self.point:
            x_dir=choice([1,-1])
            x_dis=choice([0,1,2,3,4,5,6])
            x_walk=x_dir*x_dis
            y_dir=choice([1,-1])
            y_dis=choice([0,1,2,3,4,5,6])
            y_walk=x_dir*y_dis
            if x_walk==0 and y_walk==0:
                continue
            next_x=self.x_values[-1]+x_walk
            next_y=self.y_values[-1]+y_walk
            self.x_values.append(next_x)
            self.y_values.append(next_y)
rw=Randomwalk()
rw.walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()
        
