---
title: Micropython
parent: Python notes
layout: default
nav_order: 6
---

# MicroPython

A collection of sample code extracts for commonly used tasks within MicroPython when used on a microprocessor such as the RP2040 (Raspberry Pi Pico), ESP32, or Microbit.

## Raspberry Pi Pico pinout diagram

My current recommended IDE for MicroPython is Thonny. It has excellent hardware support for the commonly used devices. Check this [connection guide for the Raspberry Pi Pico](/assets/python/thonny-pico-connection-guide.pdf).

![](https://www.raspberrypi.com/documentation/microcontrollers/images/pico-2-r4-pinout.svg)

## Operate an LED or simple device

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

* You will need to experiment with the values supplied to `.move()` as it varies from device to device.

## Neopixels

Download the [Neopixel library file](/assets/python/neopixel.txt) and save it to your board as `neopixel.py`.

Rotating pattern across 8 LEDs

```python
import time
from neopixel import Neopixel

# Number of LEDs, state library (use 0), GPIO pin, color scheme of LEDs
pixels = Neopixel(8, 0, 28, "GRB")

colors = [
    (255, 0, 0),    # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (127, 0, 255),  # Violet
    (255, 0, 127),  # Pink
    (255, 255, 255) # White
]

while True:
    pixels.clear()
    # Set each LED to a color
    for i in range(len(colors)):
        print(f"Setting LED {i} to {colors[i]}")
        pixels[i] = colors[i]
        pixels.show()
        time.sleep(0.2)
    time.sleep(1)
    # Set each LED to off
    for i in range(len(colors)):
        print(f"Setting LED {i} to off")
        pixels[i] = (0,0,0)
        pixels.show()
        time.sleep(0.2)
    time.sleep(1)
```

## Connect to WiFi

```python
import network
import machine
import time

def connect_to_wifi(SSID, PASSWORD):
    led = machine.Pin("LED", machine.Pin.OUT)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    led.on()
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            print('Waiting for Wi-Fi connection...')
            led.off()
            time.sleep(0.4)
            led.on()
            time.sleep(0.4)
    print('network config:', wlan.ifconfig())
    led.on()
    return wlan.ifconfig()[0]

ip = connect_to_wifi("SSID", "PASSWORD")
```

## Obtain the current time

```python
import time
import machine
import ntptime

# NTP Time Fetching Function
# Assumes WiFi connected device
def set_correct_time():
    while True:
        try:
            # Will set to UTC time
            ntptime.settime()
            break
        except:
            print("Waiting to set time...")
            time.sleep(5)
    # Update for timezone, Hong Kong local time being UTC+8
    rtc = machine.RTC()
    (year, month, day, weekday, hours, minutes, seconds, subseconds) = rtc.datetime()
    hours += 8
    if hours >= 24:
        hours -= 24 # Note: This doesn't change the day!
    # Set the RTC to the local time
    rtc.datetime((year, month, day, weekday, hours, minutes, seconds, subseconds))

set_correct_time()
```

## Request data via HTTP/S

[ntfy.sh](https://ntfy.sh) is a handy little service for obtaining notifications to your mobile device from code. I find it very useful for having MicroProcessor projects use it to advise me of their IP address so I can interact with them.

```python
import json
import machine
import urequests

def send_nfty_message(channel, message, link=None, server="https://ntfy.sh/"):
    print(f"[sending ntfy message] {server+channel} '{message}'")
    if link:
        response = urequests.post(url=server+channel, data=message, headers=[{"action":"view", "label":"Open", "url": link}])
    else:
        response = urequests.post(url=server+channel, data=message)        
    res = response.text
    print(f"[ntfy reply]",response.status_code,res)
    response.close()    
    return res

message = "My IoT device is at @ http://"+ip
send_nfty_message("your-ntfy-channel", message)
```
## Simple web-server

I've written a simple web-server for the use of STC students. [Download it](/assets/python/webserver.txt) and save as `webserver.py`.

There is also an associated `stc` library to contain commonly needed functions that it uses. [Download the stc library](/assets/python/stc.txt) and save as `stc.py`.

```python
import network
import usocket as socket
from machine import Pin
import time
import json
import machine
import ntptime
import webserver # webserver.py
import stc # stc.py

# Constants
SSID = "SSID"  # Adjust as required
PASSWORD = "PASSWORD"  # Adjust as required
LED_PIN = 0  # Adjust as required

# Instantiate the LED pin
led = Pin(LED_PIN, Pin.OUT)

def callback(request):
    print("Received request",request)
    if request == "on":
        led.on()
    if request == "off":
        led.off()
    return

# Main function
def main():
    ip = webserver.connect_to_wifi(SSID, PASSWORD)
    stc.set_correct_time()
    stc.send_nfty_message("your-ntfy-channel", "My IoT lamp @ http://"+ip)
    webserver.start_server("0.0.0.0", 80, "index.html", callback)

# Run the program
if __name__ == '__main__':
    main()
```

## Other resources

* [MicroPython documentation](https://docs.micropython.org/en/latest/library/index.html)
* [Raspberry Pi Pico MicroPython documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
* [Microbit MicroPython documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/)
