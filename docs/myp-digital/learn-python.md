---
title: Learn Python with Turtle
parent: MYP Digital Design
layout: default
nav_order: 7
---

# Learn Python with Turtle

## Lesson 1 - Getting started

<iframe width="480" height="320" src="https://www.youtube.com/embed/psUyOZqdToU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Exercises

* Can you make a zig-zag line?
* Can you make a tic-tac-toe board?

## Lesson 2 - Loops

<iframe width="480" height="320" src="https://www.youtube.com/embed/ZvIL2opTC9U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Exercises

* Can you create a triangle using a loop?
* Can you create a hexagon using a loop?
* Can you create a grid of squares?

## Lesson 3 - Simple calculations and circles

<iframe width="480" height="320" src="https://www.youtube.com/embed/Qwar6hGz-y4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Exercises

* Draw a house in a landscape scene, with a door, window, clouds and a sun.

## Lesson 4 - User input

## Lesson 5 - Make decisions

## Lesson 6 - Lists


-----

## Turtle command cheatsheet

This cheatsheet is your quick guide to the most useful Python Turtle commands. 

### Getting Started

| Command | What It Does | Example |
| :--- | :--- | :--- |
| `import turtle` | This is the very first thing you need to do\! It brings the turtle library into your program. | `import turtle` |
| `t = turtle.Turtle()` | Creates a turtle for you to control. We'll call it 't'. | `t = turtle.Turtle()` |

### Moving the Turtle 🚶‍♂️

These commands tell your turtle where to go. The number inside the parentheses is the number of "steps" or "degrees."

| Command | What It Does | Example |
| :--- | :--- | :--- |
| `t.forward(steps)` | Moves the turtle forward. | `t.forward(100)` |
| `t.backward(steps)` | Moves the turtle backward. | `t.backward(50)` |
| `t.right(degrees)` | Turns the turtle to its right. | `t.right(90)` |
| `t.left(degrees)` | Turns the turtle to its left. | `t.left(45)` |
| `t.goto(x, y)` | Moves the turtle to a specific location on the screen. | `t.goto(50, -20)` |
| `t.circle(radius)` | Draws a circle. The radius is how big it is. | `t.circle(50)` |

### Changing the Pen ✍️

These commands control whether the turtle draws a line or not.

| Command | What It Does | Example |
| :--- | :--- | :--- |
| `t.penup()` | Lifts the pen up. The turtle can move without drawing. | `t.penup()` |
| `t.pendown()` | Puts the pen back down. The turtle will start drawing again. | `t.pendown()` |
| `t.pensize(size)` | Changes how thick the line is. | `t.pensize(5)` |
| `t.color("color_name")` | Changes the color of the pen. Use quotes\! | `t.color("red")` |

### Filling Shapes 🎨

You can use these commands to fill in a shape with a color.

| Command | What It Does | Example |
| :--- | :--- | :--- |
| `t.begin_fill()` | Starts the "filling" process. | `t.begin_fill()` |
| `t.end_fill()` | Stops filling. Everything between this and `begin_fill()` will be filled. | `t.end_fill()` |
| `t.fillcolor("color_name")` | Chooses the color to fill with. | `t.fillcolor("blue")` |

### Helpful Reminders 💡

  * **Variables:** A variable is like a container for information. You can use it to store numbers or text. `size = 100` or `my_color = "red"`.
  * **Loops:** A `for` loop is used to repeat code a certain number of times. It's super useful for drawing shapes\!
    ```python
    # This will repeat the code inside 4 times
    for i in range(4):
        t.forward(50)
        t.left(90)
    ```
  * **Selection:** An `if` statement lets your program make a decision.
    ```python
    # This checks if the color is "red"
    if my_color == "red":
        t.color("red")
    ```
