---
title: MicroPython notes
layout: default
nav_order: 10
---

# MicroPython notes

## Pin out diagrams

* [Pico W](/docs/micropython/pico-w-pinout.png)
* [ESP-32-S3](/docs/micropython/esp32-s3-pinout.png)

## Speciality hardware

* [ESP32 CYD clone](/docs/micropython/cyd.html)

## Sensors and actuators

### External LED or pin on/off

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

### Detect button press

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

### 9g servo

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

### Neopixels

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

## Other functionality

### Connect to wifi

Requires:

* [stc.py](/docs/micropython/stc.py) Utility functions for STC projects (connect to wifi, get current time, send ntfy message)

```python
import stc

# Provide the SSID and PASSWORD for your Wifi networks
# You may want to add your home wifi to this?
# For example: NETWORKS = [("SCWiFi","wifi1234"),("homewifi","password")]

NETWORKS = [("SCWiFi","wifi1234")]
ip = stc.connect_to_wifi(NETWORKS)
print(f"You are connected using IP address {ip}")
```

### Get current date/time
Requires an active Internet connection over wifi (as per above)

```python
import stc
import time

# Provide the SSID and PASSWORD for your Wifi networks
# You may want to add your home wifi to this?
# For example: NETWORKS = [("SCWiFi","wifi1234"),("homewifi","password")]

NETWORKS = [("SCWiFi","wifi1234")]
ip = stc.connect_to_wifi(NETWORKS)
print(f"You are connected using IP address {ip}")

# Get the current date/time from the internet
# Only needs to be executed once at startup
stc.set_correct_time()

# Use this every time you want to fetch the time
year, month, mday, hour, minute, second, weekday, yearday = time.localtime()
print(f"Current time/date: {hour:02}:{minute:02}:{second:02} {year:04}-{month:02}-{mday:02}")
```

### Send a message via ntfy

```python
import stc
NETWORKS = [("SCWiFi","wifi1234")]
ip = stc.connect_to_wifi(NETWORKS)
print(f"You are connected using IP address {ip}")

stc.send_nfty_message("your-channel", "This is your message")
```

## Other resources

* [MicroPython documentation](https://docs.micropython.org/en/latest/library/index.html)
* [Raspberry Pi Pico MicroPython documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
* [Microbit MicroPython documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/)

