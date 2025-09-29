---
title: GPIO
parent: MicroPython notes
layout: default
nav_order: 20
---

# Using GPIO

## External LED or pin on/off

```python
import machine, time

# Using GP28
led = machine.Pin(28, machine.Pin.OUT) 
while True:
    print("blink!")
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)
```

To use the on-board LED of the Pico W, 

```python
led = machine.Pin("LED", machine.Pin.OUT)
```

## Detect button press

```python
import machine, time

led = machine.Pin(28, machine.Pin.OUT)
# Using GP27 and 3.3V for button
button = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_DOWN)
print("Waiting...")
while True:
    if button.value():
        print("Button pressed")
        led.on()
        time.sleep(1)
        led.off()
    time.sleep(0.2)
```

* Note: If you are connecting the button between a GPxx pin and ground, you will need to invert your button.value() check... ie `if not button.value():` and set the pin built-in resistor to `machine.Pin.PULL_UP`.

```python
import machine, time

led = machine.Pin("LED", machine.Pin.OUT)
# Using GP27 and GND for button
button = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
print("Waiting...")
while True:
    if not button.value():
        print("Button pressed")
        led.on()
        time.sleep(1)
        led.off()
    time.sleep(0.2)
```

## 9g servo

Download the [Servo library file](/assets/python/servo.txt) and save it to your board as `servo.py`.

```python
import time
from machine import Pin,PWM
from servo import Servo

sg90_servo = Servo(pin=0) # Update for correct GPxx pin number
button = machine.Pin(2, machine.Pin.IN, Pin.PULL_UP) # Pin 2 and GND
while True:
    if not button.value():   # If button pressed
        print("Button press detected")
        # Servo operation
        sg90_servo.move(35)  # turns the servo to 0°.
        time.sleep(0.9)
        sg90_servo.move(90)  # turns the servo to 90°.
        time.sleep(1)
    time.sleep(0.2)
```
