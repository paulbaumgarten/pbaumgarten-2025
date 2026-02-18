---
title: Neopixels
parent: MicroPython notes
layout: default
nav_order: 20
---

# Neopixels

Using the MicroPython Neopixel library

```python
import machine
import neopixel
import time

led = neopixel.NeoPixel(machine.Pin(48), 1)
print("Police lights!")
while True:
    led[0] = (255,0,0)
    led.write()
    time.sleep(0.25)
    led[0] = (0,0,255)
    led.write()
    time.sleep(0.25)
```

