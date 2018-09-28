
#drawtime.py
import turtle
def drawGap():
    turtle.pu()
    turtle.fd(5)
def drawline(draw):
    drawGap()
    turtle.pd()if draw else turtle.pu()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawdigit(digit):
    drawline(True)if digit in[2,3,4,6,8,9]else drawline(False)
    drawline(True)if digit in[0,1,3,5,6,7,8,9]else drawline(False)
    drawline(True)if digit in[0,2,3,5,6,8,9]else drawline(False)
    drawline(True)if digit in[0,2,6,8]else drawline(False)
    turtle.left(90)
    drawline(True)if digit in[0,4,5,6,8,9]else drawline(False)
    drawline(True)if digit in[0,2,3,5,6,7,8,9]else drawline(False)
    drawline(True)if digit in[0,1,2,3,7,8,9]else drawline(False)
    turtle.left(180)
    turtle.fd(40)
import time,turtle
def drawDate(date):
    turtle.pencolor('red')
    for i in date:
        if i=='-':
            turtle.write('年',font=('Arial',25,'normal'))
            turtle.fd(60)
        elif i=='=':
            turtle.write('月',font=('Arial',25,'normal'))
            turtle.fd(60)
        elif i=='+':
            turtle.write('日',font=('Arial',25,'normal'))
            turtle.fd(60)
        else:
            drawdigit(eval(i))
def main():
    turtle.setup(1200,800)
    turtle.pu()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
main()
