---
title: ESP32 CYD
parent: MicroPython notes
layout: default
nav_order: 10
---

# ESP32 Cheap Yellow Display
{: .no_toc }

- TOC
{:toc} 

![](/docs/micropython/cyd.png)

## Specifications

The CYD-clone we are using at STC is as follows:

* ESP32-WROOM-32
    * Wifi Bluetooth
    * Dual-core MCU 240MHZ processor
    * 520KB SRAM
    * 448K ROM 
    * 4MB Flash storage
* 240x320 display, 16bit colour display ILI9341
* Resistive touchscreen XPT2046
* Backlight control
* Speaker circuit
* Photosensitive circuit
* RGB-LED
    * Red LED: Pin 4
    * Green LED: Pin 17
    * Blue LED: Pin 16
* TF card interface
* Temperature & humidity sensor DHT11
* Power: 5V at 115mA
* GPIOs available: GPIO 35, GPIO 22, GPIO 21, and GPIO 27
* Vendor: [TZT store](https://www.tztstore.com/goods/show-7983.html), [Aliexpress](https://www.aliexpress.com/item/1005008176009397.html)

## Pin out

![](/docs/micropython/cyd-interfaces.png)

## MicroPython driver libraries

* [ili9341.py](/docs/micropython/ili9341.py) for the display
* [xpt2046.py](/docs/micropython/xpt2046.py) for the touchscreen
* [xglcd_font.py](/docs/micropython/xglcd_font.py) text rendering for the display
* [Unispace12x24.c](/docs/micropython/Unispace12x24.c) sample font for the display
* [stc.py](/docs/micropython/stc.py) Utility functions for STC projects (connect to wifi, get current time, send ntfy message)

## Sample setup code

```python
import machine
import os
from time import sleep
import stc
from ili9341 import Display, color565
from xglcd_font import XglcdFont
from xpt2046 import Touch

#########################################################
## Set up hardware - Do not make changes to this section
#########################################################

# Display and touchscreen
spi_1 = machine.SPI(1, baudrate=10000000, sck=machine.Pin(14), mosi=machine.Pin(13), miso=machine.Pin(12))
display = Display(spi_1, dc=machine.Pin(2), cs=machine.Pin(15), rst=machine.Pin(15), width=320, height=240, rotation=0)
touchscreen = Touch(spi_1, cs=machine.Pin(33), int_pin=machine.Pin(36), width=320, height=240)
# Font
unispace_font = XglcdFont('Unispace12x24.c', 12, 24)
# Backlight
backlight = machine.Pin(27, machine.Pin.OUT)
backlight.on()
# Onboard LED
red_led = machine.Pin(4, machine.Pin.OUT)
blue_led = machine.Pin(16, machine.Pin.OUT)
green_led = machine.Pin(17, machine.Pin.OUT)
red_led.on() # These LED controls are inverted :/
green_led.on()
blue_led.on()
# Color objects for TFT. Color codes are BGR
color = {}
color["white"] = color565(255, 255, 255)
color["grey"] = color565(64, 64, 64)
color["black"] = color565(0, 0, 0)
color["red"]  = color565(0, 0, 255)
color["green"]  = color565(0, 255, 0)
color["blue"]  = color565(255, 0, 0)
color["yellow"]  = color565(0, 255, 255)
color["magenta"]  = color565(255, 0, 255)
color["cyan"]  = color565(255, 255, 0)

#########################################################
## Start up code goes here
#########################################################

# Wifi networks - You may want to add your home wifi to this?
# for example: NETWORKS = [("SCWiFi","wifi1234"),("homewifi","password")]
NETWORKS = [("SCWiFi","wifi1234")]
connect_on_start = True

if __name__=="__main__":
    # Connect to wifi
    display.clear(color['black'])
    display.draw_text(0, 0, 'Connecting to wifi...', unispace_font, color['grey'], color['black'])
    ip = stc.connect_to_wifi(NETWORKS)

    # Fetch the current time
    if ip: # Only if we have a wifi connection
        display.clear(color['black'])
        display.draw_text(0, 0, 'Fetching time...', unispace_font, color['grey'], color['black'])
        stc.set_correct_time()

#########################################################
## Your main code goes here
#########################################################

if __name__=="__main__":
    display.clear(color['black'])
    display.draw_image('welcome.raw',140,0,180,240) # x, y, w, h
    display.draw_text(0, 0, 'Welcome to', unispace_font, color['cyan'], color['black'])
    display.draw_text(0, 25, 'Sha Tin College', unispace_font, color['cyan'], color['black'])
    display.draw_text(0, 50, 'Digital Design', unispace_font, color['cyan'], color['black'])
    display.draw_text(0, 100, 'TAMAGOTCHI', unispace_font, color['cyan'], color['black'])

    while True:
        green_led.on()
        sleep(0.5)
        green_led.off()
        sleep(0.5)
```

## Reference

