---
title: Pygame
parent: Python notes
layout: default
nav_order: 6
---

# Pygame library
{: .no_toc }

- TOC
{:toc} 

## Installation

Install and import the `pygame-ce` library to be able to create rich 2D games such as platformers.

## Basic structure

Basic structure of a Pygame revolves around a main game loop. An example follows

```py
import pygame, time, random
from pygame.locals import *
pygame.init()                                # Initialise pygame system
pygame.mixer.init()                          # Initialise audio system
window = pygame.display.set_mode((500,500))  # Window size
fps = pygame.time.Clock()                    # Start the clock

# Declare variables - eg: colors, images, sounds, fonts
black = pygame.Color("#000000")
orange = pygame.Color("#f79052")
pink = pygame.Color("#e96daa")
alive = True
x,y=250,250

# Main game loop
while alive:
    window.fill(black)      # Clear the screen each frame

    # Process events
    for event in pygame.event.get():
        if event.type == QUIT:
            alive = False
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos

    # Insert your main game code
    pygame.draw.circle(window, orange, (x, y), 20, 0)
    pygame.draw.circle(window, pink, (x, y), 40, 20)

    # Render the graphics
    pygame.display.update()  # Actually does the screen update
    fps.tick(25)             # Run the game at 25 frames per second

# Loop over, game over
pygame.quit()
```

This will create a simple program that will move the bulleye to whatever location on the screen you click.

![](/assets/python/image19.png)
 
## Detecting key presses

Get a Python list of all keys being pressed.

```py
keyspressed = pygame.key.get_pressed()
```

Check the list to see if a particular key is being pressed.

```py
if keyspressed[ord("a")]:
   print("Pressing A")
if keyspressed[K_RETURN]:
   print("Pressing ENTER")
```

Check for key-press or key-release events. These events only occur once when the key is first pressed and then when it is released.

```py
for event in pygame.event.get():
   if event.type == KEYDOWN:
      if event.key == K_SPACE:
         print("SPACEBAR was pressed")
   if event.type == KEYUP:
      if event.key == K_SPACE:
         print("SPACEBAR was released")
```

Codes for common keys

```py
K_UP        # Up arrow
K_DOWN      # Down arrow
K_LEFT      # Left arrow
K_RIGHT     # Right arrow
K_RETURN    # Return/enter
K_SPACE     # Space bar
K_DELETE    # Delete key
K_a         # Letter 'a'
K_1         # Number '1'
```

## Detecting mouse action

```py
for event in pygame.event.get():
   if event.type == MOUSEMOTION:     # Mouse movement
      x,y = event.pos
   if event.type == MOUSEBUTTONDOWN: # Mouse click
      x,y = event.pos
      print("clicked at ",x,y)
   if event.type == MOUSEBUTTONUP:   # Mouse release
      x,y = event.pos
      print("released at ",x,y)
```
 
## Music and sound effects

To play background music. Use an MP3 file. Do not place this in the game loop!

```py
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)         # 0 = play once, -1 = loop
```

To load a short sound effect into a variable. Use WAV files for sound effects. Do this before the game loop.

```py
hurt_sound = pygame.mixer.Sound('ouch.wav')
```

Then within the game loop, use this to initiate the sound effect when you want it.

```py
hurt_sound.play()
```

## Images

Assign a variable the content of an image file. Use PNG if you require transparency, otherwise JPG is ok. Do this before the game loop.

```py
player_image = pygame.image.load("image.jpg")
```

Then within the game loop, to draw the image. The x/y coordinates refer to the screen location to place the top/left of the image.

```py
window.blit(player_image, (x, y))
```

To create an animated sequence, load images into a Python list.

```py
# Create a list of images for walking left
player_move = [
   pygame.image.load("walk01.png"),
   pygame.image.load("walk02.png"),
   pygame.image.load("walk03.png"),
   pygame.image.load("walk04.png")
]
# Which frame number we are currently displaying
player_move_frame = 0

Then display a different image from the list each frame.

# Draw the player --- Uses one image from our list of images
window.blit(player_move[ player_move_frame ], (x,y))           
# Increment the frame number
player_move_frame = (player_move_frame + 1) % len(player_move)
```
 
Some useful image modification functions.

```py
# Resize to 200 x 100 pixels
resized_image = pygame.transform.scale(original_image, (200, 100))
# Rotate 90 degrees counter-clockwise 
rotated_image = pygame.transform.rotate(original_image, 90) 
```

## Text

Create a variable for the font and size you wish to display. Do not put in your game loop.

```py
arial_24 = pygame.font.SysFont("Arial", 24) # Variable to write Arial size 24pt fonts
```

Use the `render()` function to create an image based on your message. This can be inside your loop.

```py
label = arial_24.render("Hello Python!", 1, white)  # Create an image containing text
window.blit(label, (300, 50))                       # Blit the image to screen
```

## Drawing shapes

```py
# parameters: window, color, (from-coordinates), (to-coordinates), thickness
pygame.draw.line(window, blue, (50, 60), (50, 160), 10)

# parameters: window, color, (x, y, width, height), thickness
pygame.draw.rect(window, green, (52, 160, 120, 40) )

# parameters: window, color, (center x,y), radius, thickness
pygame.draw.circle(window, white, (110, 110), 40, 10)

# parameters: window, color, (x, y, width, height), thickness
pygame.draw.ellipse(window, pink, (220, 100, 80, 40), 10)

# parameters: window, color, (list of coordinate pairs of vertices), thickness
pygame.draw.polygon(window, red, ((20,20), (52,60), (172,60), (200,20)), 5)
```
 
## Detecting collisions

Pygame uses rectangles to detect collisions by looking for any overlap between the rectangles.

```py
player = Rect(player_x, paddle_y, 60, 20) # x, y, width, height
enemy  = Rect(enemy_x,  enemy_y,  60, 20) # x, y, width, height
if player.colliderect(enemy):
   print("ouch!")
```

To detect collision between one rectangle and a list of rectangles (such as a player and a list of obstacles)

```py
player = Rect(player_x, paddle_y, 60, 20) # x, y, width, height
enemies = [
   Rect(100, 100, 60, 20), # x, y, width, height
   Rect(200, 100, 60, 20), # x, y, width, height
   Rect(300, 100, 60, 20), # x, y, width, height
   Rect(400, 100, 60, 20)  # x, y, width, height
   ]
if player.collidelist(enemies) >= 0:
   which_enemy = player.collidelist(enemies)
   print("ouch!")
   print("You hit item",which_enemy,"in the list")
```

To detect collision between one sprite (image) and another, you need to create rectangles that represent the size and location of the sprites.

```py
player_image = pygame.image.load("goodie.png")
player_location = [0,0] # x,y
enemy_image = pygame.image.load("baddie.png")
enemy_location = [0,500] # x,y
```

...then to detect collision within the game loop, it might look like this…

* Note: The `image.get_rect()` function knows the width and height of the image but not its location, which is why that must be provided via the parameter `topleft=(x,y)`

```py
player_rect = player_image.get_rect(topleft=player_location)
enemy_rect = enemy_image.get_rect(topleft=enemy_location)
if player_rect.colliderect(enemy_rect):
   print("ouch!")
```

## Sample Snake game

```py
import pygame, sys, random
from pygame.locals import *
pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")
colors = {"snake":(196,196,0), "background":(0,0,0), "fruit":(255,0,255)}
windowSize = (0,0,500,500)
gridSize=(25,25)            # Number of blocks to divide the screen into
blockSize = windowSize[2]/gridSize[0]
gameRunning = True
snakeTail = []
snakeXY = [(10,10)]
fruitXY = [5,5]
currentXY = [10,10]
directionXY = [0,0]
score = 0
while gameRunning:
    # Check for user interaction
    for event in pygame.event.get():
        if event.type == QUIT:
            gameRunning = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                directionXY = [-1,0]
            elif event.key == K_RIGHT:
                directionXY = [1,0]
            elif event.key == K_UP:
                directionXY = [0,-1]
            elif event.key == K_DOWN:
                directionXY = [0,1]
            elif event.key == K_ESCAPE:
                gameRunning = False
    window.fill(colors['background'])    # Reset (blank) the window
    # New location for the front of the snake
    currentXY = [ currentXY[0]+directionXY[0], currentXY[1]+directionXY[1] ]
    if len(snakeXY) > 1 and currentXY in snakeXY[1:]:      # Colliding with another part of the snake
        gameRunning = False
    if currentXY[0] < 0 or currentXY[0] >= gridSize[0] or currentXY[1] < 0 or currentXY[1] >= gridSize[1]:
        gameRunning = False       # Travelled off edge of screen
    # Move the snake 1 square along
    snakeXY.insert(0, currentXY)  # Add new block to the snake body
    snakeXY.pop()                 # Remove the end peice of the snake body 
    # Pixel coordinates of the piece of fruit
    fruitPixel = (fruitXY[0]*blockSize, fruitXY[1]*blockSize, blockSize, blockSize)
    fruitCollide = False
    for piece in snakeXY:
        # Pixel coordinates for this peice of the snake
        snakePiecePixel = (piece[0]*blockSize, piece[1]*blockSize, blockSize, blockSize)
        # Draw this piece of the snake
        pygame.draw.rect(window, colors["snake"], snakePiecePixel)
        # Is this part of the snake colliding with the fruit?
        if Rect(snakePiecePixel).colliderect(fruitPixel):
            fruitCollide = True
            break
    if fruitCollide:
        snakeXY.append(currentXY)        # Increase snake body length
        # Generate new location for the fruit
        fruitXY = [random.randint(1, gridSize[0]-1), random.randint(1, gridSize[1]-1)]
        score += 1 # Increase score by 1
    pygame.draw.rect(window, colors['fruit'], fruitPixel)    # Draw fruit
    pygame.display.update() # Send frame to screen
    fps.tick(10)
pygame.quit()
print("Thanks for playing snake clone by Paul Baumgarten.")
print(f"Your score: {score}.")
```
