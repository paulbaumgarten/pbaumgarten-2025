---
title: Micropython
parent: Python notes
layout: default
nav_order: 6
---

# MicroPython
{: .no_toc }

A collection of sample code extracts for commonly used tasks within MicroPython when used on a microprocessor such as the RP2040 (Raspberry Pi Pico), ESP32, or Microbit.

My current recommended IDE for MicroPython is Thonny. It has excellent hardware support for the commonly used devices. 

- TOC
{:toc} 

## Raspberry Pi Pico pinout diagram

* [Connection guide for the Raspberry Pi Pico](/assets/python/thonny-pico-connection-guide.pdf).

![](https://www.raspberrypi.com/documentation/microcontrollers/images/pico-2-r4-pinout.svg)

## ESP32-S3-wroom pinout diagram

Note: The ESP32's we have at STC have their onboard Neopixel at GP48.

![](esp32-s3-pinout.jpg)


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

## Neopixels (Pico W)

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

## Neopixels (ESP-32)

Using the onboard Neopixel library

```python
from machine import Pin, ADC, PWM
import neopixel
import time

# Neopixel (Status LED)
pixel = neopixel.NeoPixel(Pin(48), 1)  # GPIO48

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
    for i in range(len(colors)):
        pixel[0] = colors[i]
        pixel.write()
        time.sleep(0.3)
```

## Connect to WiFi

```python
import network
import machine
import time

def connect_to_wifi(networks):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print(networks)
    for ssid, password in networks:
        print(f"Trying to connect to: {ssid}")
        wlan.connect(ssid, password)
        # Wait for connection or timeout
        for i in range(10):
            if wlan.isconnected():
                print(f"✅ Connected to {ssid}")
                print(f"IP address: {wlan.ifconfig()[0]}")
                return wlan.ifconfig()[0]
            time.sleep(0.5)
        print(f"❌ Failed to connect to {ssid}\n")
        # Disconnect before trying the next one
        wlan.disconnect()
        time.sleep(1)
    print("🚫 Could not connect to any known Wi-Fi networks.")
    return None

NETWORKS = [("SSID", "PASSWORD")]
ip = connect_to_wifi(NETWORKS)
```

## Obtain the current time

```python
import time
import machine
import ntptime

# NTP Time Fetching Function
# Assumes WiFi connected device
def set_correct_time(timezone_offset_hours=8):
    while True:
        try:
            ntptime.settime()
            break
        except:
            print("Fetching the current time/date...")
            time.sleep(5)
    # Update for timezone
    local_time = time.localtime(time.time() + timezone_offset_hours*(60*60))
    # Extract local time from the tuple provided by time.localtime()
    year, month, mday, hour, minute, second, weekday, yearday = local_time
    rtc_weekday = (weekday + 1) % 7  # RTC uses Sunday as 0
    # Update the real time clock to local time
    rtc = machine.RTC()
    rtc.datetime((year, month, mday, rtc_weekday, hour, minute, second, 0))
    print(f"Current time/date: {hour:02}:{minute:02}:{second:02} {year:04}-{month:02}-{mday:02}")

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
NETWORKS = [("SSID","PASSWORD")] # Adjust as required
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
    ip = webserver.connect_to_wifi(NETWORKS)
    stc.set_correct_time()
    stc.send_nfty_message("your-ntfy-channel", "My IoT lamp @ http://"+ip)
    webserver.start_server("0.0.0.0", 80, "index.html", callback)

# Run the program
if __name__ == '__main__':
    main()
```

## CYD Demo code

For the CYD (Cheap Yellow Device)

```python
import machine
#from machine import Pin, SPI, ADC, idle, RTC
import os
import time
import stc
import random
from ili9341 import Display, color565
from xpt2046 import Touch
from xglcd_font import XglcdFont

WIFI = [("SCWiFi", "wifi1234")]
X,Y = 0,0 # Globals to contain coordinates of last touch

def touchscreen_press(x, y):
    global X,Y
    print(f"Touch at x={x}, y={y}")
    X,Y = x,y

### SETUP HARDWARE
spi_1 = machine.SPI(1, baudrate=10000000, sck=machine.Pin(14), mosi=machine.Pin(13), miso=machine.Pin(12))
display = Display(spi_1, dc=machine.Pin(2), cs=machine.Pin(15), rst=machine.Pin(15), width=320, height=240, rotation=0)
touchscreen = Touch(spi_1, cs=machine.Pin(33), int_pin=machine.Pin(36), int_handler=touchscreen_press, width=320, height=240)
backlight = machine.Pin(27, machine.Pin.OUT)
backlight.on()
unispace_font = XglcdFont('fonts/Unispace12x24.c', 12, 24)

# Color codes are BGR
white_color = color565(255, 255, 255)
black_color = color565(0, 0, 0)
red_color = color565(0, 0, 255)
yellow_color = color565(0, 255, 255)
green_color = color565(0, 255, 0)

# Main
if __name__=="__main__":
    display.clear(black_color)
    display.draw_text(0, 0, 'Connecting to wifi...', unispace_font, white_color, black_color)
    stc.connect_to_wifi(WIFI)
    display.clear(black_color)
    display.draw_text(0, 0, 'Fetching time...', unispace_font, white_color, black_color)
    stc.set_correct_time()
    (year, month, mday, hour, minute, second, weekday, yearday) = time.localtime()
    display.draw_text(0, 0, f'{mday:02}/{month:02}/{year:02}, {hour:02}:{minute:02}:{second:02}', unispace_font, white_color, black_color)
    display.draw_text(0, 25, f'Use touchscreen...', unispace_font, white_color, black_color)
    while True: # Play forever
        x,y=X,Y
        (year, month, mday, hour, minute, second, weekday, yearday) = time.localtime()
        display.draw_text(0, 0, f'{mday:02}/{month:02}/{year:02}, {hour:02}:{minute:02}:{second:02}  ', unispace_font, white_color, black_color)
        display.draw_text(0, 25, f'x={x},y={y}                 ', unispace_font, white_color, black_color)
        display.fill_circle(x, y, 10, white_color)
        time.sleep(0.1)
        display.fill_circle(x, y, 10, black_color)
```

## Other resources

* [MicroPython documentation](https://docs.micropython.org/en/latest/library/index.html)
* [Raspberry Pi Pico MicroPython documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
* [Microbit MicroPython documentation](https://microbit-micropython.readthedocs.io/en/v2-docs/)
