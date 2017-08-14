#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle as t

t.setup(800, 600)
wn = t.Screen()
colors = [ "blue" , "green" , "purple" , "cyan" , "magenta" , "violet" ]

t.reset()
t.bgcolor("black")
t.speed(100)
t.tracer(0, 0)
for i in range(45):
    t.color(colors[i % len(colors)])
    t.pendown()
    t.fd(2 + i * 5)
    t.left(45)
    t.width(i)
    t.penup()

t.update()

t.reset()

t.color("red")
for angle in range(0, 360, 15):
    t.seth(angle)
    t.circle(100)
t.update()

t.color("red")
for angle in range(0, 360, 15):
    t.seth(angle)
    t.circle(100)

t.update()

# import turtle as t

radio = 150
quintas = ("C", "G", "D", "A", "E", "B",
           "F#/Gb", "Db", "Ab", "Eb", "Bb", "F")
correccion = (20, 20, 21, 25, 29, 31,
              31, 36, 33, 31, 25, 20)

t.penup()
# para que el círculo quede centrado en (0, 0)
t.goto(0, - radio)
t.pendown()
t.circle(radio)
t.penup()
t.goto(0, 0) # regresamos al centro
t.left(90)
t.pendown()

for quinta in range(12):
    t.forward(radio)
    t.penup()
    t.forward(correccion[quinta]) # separamos del círculo el punto de escritura
    t.write(quintas[quinta], font=("Arial", 10, "bold")) # negrita
    t.goto(0, 0)
    t.right(30) # giramos 30 grados (360 dividido entre 12)
    t.pendown()

t.hideturtle() #para que no se vea la tortuga en la imagen final



wn.exitonclick()
