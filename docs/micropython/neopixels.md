---
title: Neopixels
parent: MicroPython notes
layout: default
nav_order: 20
---

# Neopixels

Using the MicroPython Neopixel library

```python
from machine import Pin
import neopixel
import time

# Neopixel (Status LED)
pixel = neopixel.NeoPixel(Pin(48), 1)  # GPIO48, 1 Neopixel

while True:
    pixel[0] = (0,0,255) # Blue
    pixel.write()
    time.sleep(0.3)
    pixel[0] = (0,0,0) # Black
    pixel.write()
    time.sleep(0.3)
```

