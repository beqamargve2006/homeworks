from turtle import*


#we want to paint a house

#step 1: draw a square

speed(10)

width(5)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of door


#draw windows

penup()
goto(17.5,140)
pendown()

color("brown")
begin_fill()

right(150)
forward(30)
right(90)

forward(45)
right(90)

forward(30)
right(90)
forward(45)




penup()
goto(182.5,140)
pendown()

right(90)
forward(30)

left(90)
forward(45)

left(90)
forward(30)

left(90)
forward(45)

end_fill()

#end of the windows













exitonclick()



