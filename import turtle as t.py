import turtle as t
t.speed(5813)
t.bgcolor("black")
list1=["purple","red","orange","blue","green"]
for i in range(500):
    t.color(list1[i%5])
    t.pensize(i/40+1)
    t.forward(i)
    t.left(35)

t.done()    