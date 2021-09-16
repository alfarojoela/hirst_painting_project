from turtle import Turtle, Screen
import turtle as t
import colorgram
import random

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)

# colors = colorgram.extract("hirst_dot_painting.jpg", 34)
#
# color_list = []
# for index in range(33):
#     current_color = colors[index]
#     rgb = current_color.rgb
#     hsl = current_color.hsl
#
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#
#     tuple_of_color = (red, green, blue)
#     color_list.append(tuple_of_color)
#
# print(color_list)
# tim.speed("fastest")
# x = 0.0
# y = 0.0
# for index in range(33):
#     tim.setposition(x, y)
#     tim.fillcolor(color_list[index])
#     tim.begin_fill()
#     tim.circle(10)
#     tim.end_fill()
#     #tim.setheading(tim.heading() + 10)

    #x += 30

rgb_list = [(241, 239, 235), (200, 157, 125), (141, 87, 66), (232, 239, 233), (51, 98, 127), (240, 232, 234), (230, 216, 97), (136, 173, 155), (63, 109, 85), (125, 162, 188), (167, 47, 59), (226, 232, 237), (193, 162, 172), (192, 99, 73), (138, 31, 39), (148, 154, 80), (35, 52, 65), (101, 153, 96), (210, 180, 189), (152, 113, 125), (178, 199, 182), (22, 62, 112), (218, 180, 172), (129, 40, 38), (51, 68, 74), (45, 44, 43), (56, 38, 42), (92, 146, 150), (55, 62, 61), (99, 129, 161), (51, 73, 65), (175, 192, 211), (175, 199, 203)]

# 10 by 10 grid
#radius of each circle 20
#spaced by 50
x = 0
y = 0
tim.speed("fastest")
circles_on_x = 0
circles_on_y = 0
number_of_circles = 0
index = 0
length = len(rgb_list) -1
tim.penup()

while index < length and number_of_circles != 100:

    tim.setposition(x, y)
    tim.fillcolor(rgb_list[index])
    tim.begin_fill()
    tim.circle(20)
    tim.end_fill()
    x += 50

    circles_on_x += 1
    index +=1
    number_of_circles += 1
    if circles_on_x ==10 and number_of_circles != 100:
        circles_on_y +=1
        circles_on_x = 0
        y += 50
        x = 0
    if index == length:
        index = 0
    # if number_of_circles == 100:
    #     break
#
# x = 0
# y = 0
# circles_on_x = 0
# circles_on_y = 0
# number_of_circles = 0
# index = 0
# length = len(rgb_list) -1
# tim.penup()
#
# while index < length and number_of_circles != 100:
#
#     tim.setposition(x, y)
#     tim.fillcolor(rgb_list[index])
#     tim.begin_fill()
#     tim.circle(20)
#     tim.end_fill()
#     x -= 50
#
#     circles_on_x += 1
#     index +=1
#     number_of_circles += 1
#     if circles_on_x ==10 and number_of_circles != 100:
#         circles_on_y +=1
#         circles_on_x = 0
#         y -= 50
#         x = 0
#     if index == length:
#         index = 0
#     # if number_of_circles == 100:
#     #     break
#







screen = t.Screen()
screen.exitonclick()