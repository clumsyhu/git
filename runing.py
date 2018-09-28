import matplotlib.pyplot as plt
from random import choice
class Randomwalk():
    def __init__(self,point=20000):
        self.point=point
    def walking(self):
        self.valuewalk_x=[0]
        self.valuewalk_y=[0]
        while len(self.valuewalk_x)<self.point:
            fx_x=choice([-1,1])
            dis_x=choice([0,1,2,3,4,5,6])
            x_step=fx_x*dis_x                       
            fx_y=choice([-1,1])
            dis_y=choice([0,1,2,3,4,5,6])
            y_step=fx_y*dis_y
            if x_step==0 and y_step==0:
                         continue
            next_fw_x=self.valuewalk_x[-1]+x_step
            next_fw_y=self.valuewalk_y[-1]+y_step
            self.valuewalk_x.append(next_fw_x)
            self.valuewalk_y.append(next_fw_y)
while True:
    plt.figure(figsize=(100,100))
    rdw=Randomwalk()
    rdw.walking()
    plt.scatter(rdw.valuewalk_x,rdw.valuewalk_y,c=rdw.valuewalk_y,cmap=plt.cm.Reds,s=2)
    plt.scatter(0,0,c='green',s=100)
    plt.scatter(rdw.valuewalk_x[-1],rdw.valuewalk_y[-1],c='blue',s=50)
    plt.show()                        
    a=input('任意键继续，按q退出')
    while a!='q':
        break
    
    
