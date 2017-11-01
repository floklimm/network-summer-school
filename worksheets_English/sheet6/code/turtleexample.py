import turtle
import numpy as np

# setze die Geschwindigkeit des Zeichners auf Maximum
turtle.speed(0)

# Hebe den Stift des Zeichners (sodass bei Bewegung
# nicht gezeichnet wird
turtle.penup()

# Bewege den Zeichner zur neuen Startposition
turtle.setpos(-250,250)

# Setze den Stift nieder, sodass nun gezeichnet wird
turtle.down()

# Bewege den Zeichner 30 pixel vorwaerts (zeichne Linie)
turtle.forward(30)

# Drehe den Zeichner 60 Grad nach links
turtle.left(60)

# Gehe 30 Pixel nach vorne (zeichne dabei), drehe 60 Grad nach rechts
turtle.forward(30)
turtle.right(60)

# Bestimme, dass das Zeichenfenster erst bei einem Klick geschlossen wird
turtle.exitonclick()

# Was macht diese Funktion?
def draw_mysterious_thingy(n,base_r=100):
    
    forward_length = 2 * base_r * np.sin(np.pi/n)
    degree = 360./n

    turtle.penup()
    turtle.setpos(0,0)
    turtle.pendown()

    for i in range(n):
        turtle.forward(forward_length)
        turtle.left(degree)
