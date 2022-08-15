import turtle 

from turtle import *



wn = Screen()

wn.bgcolor('black')



t = turtle. Turtle()

t.pencolor('white')



def curve():

       for i in range (200):

             t.rt(1)

             t.fd(1)

       

def heart():

       t.fillcolor('red')

       t.begin_fill()

       t.lt (140)

       t.fd (113)

       curve () 

       t.lt (120)

       curve() 

       t.fd(112)

       t.end_fill()



heart()

t.ht()



def write(message,pos):

       x,y=pos

       t.penup()

       t.goto(x,y)

       t.color('white')

       style=("Stencil Std", 18, "italic")

       t.write(message, font=style)


write('R',(-35,95))

write('U',(-20,95))

write('B',(-5,95))

write('E', (10,95))

write('S', (25,95))

write('H', (40,95))



wn.mainloop()