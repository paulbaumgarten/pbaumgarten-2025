---
title: Python Imaging Library
parent: Python notes
layout: default
nav_order: 6
---

# Python Imaging Library (PIL)
{: .no_toc }

- TOC
{:toc} 

The Python Imaging library will allow you to load and manipulate JPG, PNG and other common image formats. (note: Also compare to OpenCV). Install the "Pillow" library.

Import

```py
from PIL import Image, ImageDraw, ImageFont
```

Creating and opening images, get image information

```py
# Create new image
img1 = Image.new("RGBA", (1920, 1080))
# Open an image
img1 = Image.open("my picture.png")

# Get image information
width, height = img1.size
mode = img1.mode # Modes: 1 (1bit pixels), L (8bit grey), RGB, RGBA, CMYK, HSV 
```

Save an image

```py
# Save an image
img1.save("myphoto new copy.png", "png")
```

Display an image using operating system default application

```py
# Display image with system viewer
img1.show()
```

Common tasks

```py
# Cropping
boundaries = (200, 50, 400, 200)  # x, y, x+w, y+h
img2 = img1.crop(boundaries)

# Resize
img2 = img1.resize((300, 200))

# Rotate (clockwise)
img2 = img1.rotate(45, expand=True, fillcolor="#ff00ff")

# Paste 1 image into another
img1.paste(img2, (100,100)) # Paste at location within img1 
img1.paste(img2, (100,100), img2) # Use alpha channel of img2 for transparency of paste 
img1.show()

# Change mode
img2 = img1.convert(mode="1") # Convert to black & white

# Get/set individual pixels
img1.getpixel((x,y))
img1.putpixel((x,y), (r,g,b))

# Write text onto image
draw = ImageDraw.Draw(img1)
font = ImageFont.truetype("Roboto-Light.ttf", 48)
draw.text((x,y), "Message", "#ff00ff", font=font) 

# Drawing on an image
draw = ImageDraw.Draw(img1) # Attach drawing obj to img1
draw.line((x1,y1,x2,y2), fill=(255,255,0), width=1)
draw.rectangle((x,y,width,height), fill="#000000", width=1)
draw.ellipse((x,y,width,height), outline="#ffff00", width=5)
```
