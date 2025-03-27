from turtle import*

#we want to drawe a square

speed(14)
width(7)
color("blue")
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
color("purple")
begin_fill()
left(90)
forward(100)
right(90)
forward(70)
right(90)
forward(100)
end_fill()

#end of door

#drawing a roof

penup()
goto(200,200)
pendown()
color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#end of roof


exitonclick()