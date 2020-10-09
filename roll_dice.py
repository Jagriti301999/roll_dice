import tkinter
import random

canvas_width = 640
canvas_height = 480
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

number = random.randint(1,6)

print("Number {}".format(number))
print("Making dice")

size = 255

x, y = canvas_width / 2, canvas_height / 2
unit = size / 5
radius = size*0.05

p1 = x - size / 2,  y-size / 2 + radius
p2 = x - size / 2 + radius, y - size / 2
p3 = x + size / 2 - radius, y - size / 2
p4 = x + size / 2,  y-size / 2 + radius
p5 = x + size / 2,  y+size / 2 - radius
p6 = x + size / 2 - radius, y + size / 2
p7 = x - size / 2 + radius, y + size / 2
p8 = x - size / 2,  y+size / 2 - radius

canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                      outline="black", fill="black", width=3)

a1 = x - 1.5*unit
a2 = x
a3 = x + 1.5*unit

b1 = y - 1.5*unit
b2 = y
b3 = y + 1.5*unit

center = a2-size/10, b2-size/10, a2+size/10, b2+size/10
topleft = a1-size/10, b1-size/10, a1+size/10, b1+size/10
topright = a3-size/10, b1-size/10, a3+size/10, b1+size/10
midleft = a1-size/10, b2-size/10, a1+size/10, b2+size/10
midright = a3-size/10, b2-size/10, a3+size/10, b2+size/10
botleft = a1-size/10, b3-size/10, a1+size/10, b3+size/10
botright = a3-size/10, b3-size/10, a3+size/10, b3+size/10

if number == 1:
    canvas.create_oval(center, fill='lightblue')
elif number == 2:
    canvas.create_oval(topleft, fill='green')
    canvas.create_oval(botright, fill='green')
elif number == 3:
    canvas.create_oval(topleft, fill='yellow')
    canvas.create_oval(center, fill='yellow')
    canvas.create_oval(botright, fill='yellow')
elif number == 4:
    canvas.create_oval(topleft, fill='purple')
    canvas.create_oval(topright, fill='purple')
    canvas.create_oval(botleft, fill='purple')
    canvas.create_oval(botright, fill='purple')
elif number == 5:
    canvas.create_oval(topleft, fill='pink')
    canvas.create_oval(topright, fill='pink')
    canvas.create_oval(center, fill='pink')
    canvas.create_oval(botleft, fill='pink')
    canvas.create_oval(botright, fill='pink')
else:
    canvas.create_oval(topleft, fill='red')
    canvas.create_oval(topright, fill='red')
    canvas.create_oval(midleft, fill='red')
    canvas.create_oval(midright, fill='red')
    canvas.create_oval(botleft, fill='red')
    canvas.create_oval(botright, fill='red')
    
canvas.mainloop() 
