---
title: Y08 Tamagotchi
parent: MYP Digital Design
layout: default
nav_order: 5
---

# Tamagotchi (Year 8 Digital Design)
{: .no_toc }

* SOI: Designers enhance the form of a product to meet the needs of communities 
* Key concept: Communities
* Related concept: Form
* Context: Identities and relationships (adaptation, form)
* Assessed criteria: A
* Key technology: Shaper3D, ESP32, LCD, Wifi / BLE, MicroPython

Using the form of a wearable or a keychain for your school bag, create a community of interactive STC Tamagotchis. Use wifi / BLE to meet/socialise with other Tamagotchis nearby to earn life points. Design and 3D print your protective case to your own style and needs.

- TOC
{:toc} 

---

## Watch the trailer

<iframe width="560" height="315" src="https://www.youtube.com/embed/5Dts5XKDRlo?si=59rBbYfrHYR8hr5S" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Video 1: Connect your device

<iframe width="560" height="315" src="https://www.youtube.com/embed/xpW7Zvl4ahw?si=RdR6ODUNTkForh62" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Download the all the files you need as a ZIP file

* [cyd-files.zip](/docs/micropython/cyd/cyd-files.zip)

Or download them individually:

* [cyd.mpy](/docs/micropython/cyd/cyd.mpy)
* [ili9341.mpy](/docs/micropython/cyd/ili9341.mpy)
* [tthelp.py](/docs/micropython/cyd/tthelp.py)
* [Unispace12x24.c](/docs/micropython/cyd/Unispace12x24.c)
* [WIFI.mpy](/docs/micropython/cyd/WIFI.mpy)
* [xglcd_font.mpy](/docs/micropython/cyd/xglcd_font.mpy)
* [xpl2046.mpy](/docs/micropython/cyd/xpt2046.mpy)

## Video 2: Text, colours, coordinates

<iframe width="560" height="315" src="https://www.youtube.com/embed/oMKQW4AB3no?si=deShqstL9ruBFbnt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

![](/docs/micropython/cyd/color_reference.png)

## Video 3: Variables, loops, timers

<iframe width="560" height="315" src="https://www.youtube.com/embed/CX551LbtYUU?si=Npyekl8Vi5ZcA9Ql" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Video 4: More loops, detect touch, increase counters

<iframe width="560" height="315" src="https://www.youtube.com/embed/LNCNZ5vPGjM?si=T-2krIn1q14jUDJA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Video 5: If statements, touch coordinates, multiple variables

<iframe width="560" height="315" src="https://www.youtube.com/embed/wOOJNYaEu2Q?si=v3SZzuP_rFK__lOS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Video 6: Creating functions to organise yuor code

<iframe width="560" height="315" src="https://www.youtube.com/embed/uhB7EYO8faA?si=YtW8d4lMPFg_dAMX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Video 7: Converting and displaying images

<iframe width="560" height="315" src="https://www.youtube.com/embed/1_xqVlGk9og?si=vek6Hb1I-r5q4pkY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Code to convert PNG/JPG images to RAW

```python
# Utility to convert images to raw RGB565 format.
from PIL import Image
from struct import pack
from os import path
import os
import sys

def convert_file(in_file, out_file):
    # Sha Tin's CYD devices require BGR format RAW files
    print('Converting: ' + in_file)
    img = Image.open(in_file).convert('RGB')
    pixels = list(img.getdata())
    with open(out_file, 'wb') as f:
        for pix in pixels:
            r = (pix[2] >> 3) & 0b00011111 # 5 bits
            g = (pix[1] >> 2) & 0b00111111 # 6 bits
            b = (pix[0] >> 3) & 0b00011111 # 5 bits
            f.write(pack('>H', (r << 11) + (g << 5) + b))
    print('Saved: ' + out_file)

def convert_all_images_in_folder(folder=None):
    if not folder:
        folder = os.getcwd()
    files = os.listdir()
    for ssource_file in files:
        if ssource_file.lower().endswith(".png") or ssource_file.lower().endswith(".jpeg") or ssource_file.lower().endswith(".jpg"):
            target_file = ssource_file.split(".")[0]+".raw"
            convert_file(ssource_file, target_file)

convert_all_images_in_folder()
```

## Video 8: Connect to wifi, download and display data

<iframe width="560" height="315" src="https://www.youtube.com/embed/ldS4WNeg_jM?si=5pvteciTxKba63yN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

* [Dad joke website](https://icanhazdadjoke.com/api)

## Video 9: Start your project, connect to Virtual Pet API

<iframe width="560" height="315" src="https://www.youtube.com/embed/yp5C1CuTvRI?si=ru4u0JzV1V1Amfqc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```
POST https://api.pbaumgarten.com/pets/register

headers = {
    "X-API-KEY": "PROVIDED BY YOUR TEACHER",
    "Content-Type": "application/json"
}
data = {
    "pet_name": "NAME FOR THE SYSTEM TO REMEMBER FOR YOUR PET"
}

response = {
    "pet_name": "YOUR PET NAME",
    "owner_name: "YOUR NAME",
    "pet_id": "YOUR PET ID NUMBER",
    "points_balance": 0 // balance of points earnt so far
}
```

## Video 10: Show the weather

<iframe width="560" height="315" src="https://www.youtube.com/embed/_n1C7yxj-xg?si=DK80mhzM-dcYkYs7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```
GET https://api.pbaumgarten.com/pets/weather

headers = {
    "X-API-KEY": "PROVIDED BY YOUR TEACHER"
}

response = [
    {
        "Day": "Name of today",
        "Info": "Weather description",
        "Max": "Maximum temperature",
        "Rain": "Likelihood of significant rain":
    },{
        "Day": "Name of tomorrow",
        "Info": "Weather description",
        "Max": "Maximum temperature",
        "Rain": "Likelihood of significant rain":
    }
]
```

## Video 11: Show your timetable

<iframe width="560" height="315" src="https://www.youtube.com/embed/eyg94WUPZXw?si=Uaw0W-xpAoBI099Z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```
    start_dates = {
        (2025,  8, 11): 0,
        (2025, 10, 13): 0,
        (2025, 11, 17): 0,
        (2026,  1,  5): 0,
        (2026,  2, 23): 0,
        (2026,  4, 13): 5
    }
    timetable = [
        ["12 CS",    "10 CS",    "11 CS",    "13 CS",  "9 DD 7"],
        ["13 CS HL", "13 CS HL", "7 DD 3",   "",       "9 DD 1"],
        ["",         "9 DD 3",   "12 CS",    "9X2 WB", ""],
        ["11 CS",    "",         "10 CS",    "",       "12 CS"],
        ["12 CS",    "10 CS",    "13 CS",    "",       "8 DD 2"],
        ["11 CS",    "",         "13 CS HL", "9 DD 3", ""],
        ["12 CS",    "12 CS",    "",         "10 CS",  "11 CS"],
        ["",         "7 DD 3",   "",         "9X2 WB", ""],
        ["13 CS",    "9 DD 1",   "",         "11 CS",  "10 CS"],
        ["12 CS",    "9 DD 7",   "8 DD 2",   "",       "13 CS"]
    ]
```

## Video 12: Feed your pet a virtual meal

<iframe width="560" height="315" src="https://www.youtube.com/embed/0OEfm22sTxk?si=1CTJ6OI8c5oSCNsb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```
POST https://api.pbaumgarten.com/pets/meal

headers = {
    "X-API-KEY": "PROVIDED BY YOUR TEACHER"
}

response if successful = {
    "status": "success",
    "points_balance": 999,
}

response if too soon = {
    "status": "too soon"
}
```

## Video 13: Navigation menu

<iframe width="560" height="315" src="https://www.youtube.com/embed/p8aHxCLPd6k?si=ZJhpTY2p8rXA23F2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Video 14: Say hello to other pets

<iframe width="560" height="315" src="https://www.youtube.com/embed/0L1zMfG-f5c?si=ZTFSJxrz7aYHobzD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```
POST https://api.pbaumgarten.com/pets/hello

headers = {
    "X-API-KEY": "PROVIDED BY YOUR TEACHER"
}

response if successful = {
    "status": "success",
    "responder": "their pet name",
}

response if waiting for another player = {
    "status": "acknowledged"
}
```


```
POST https://api.pbaumgarten.com/pets/hello-check

headers = {
    "X-API-KEY": "PROVIDED BY YOUR TEACHER"
}

response if successful = {
    "status": "success",
    "responder": "their pet name",
}

response no other player = {
    "status": "no responses"
}
```

## Video 15: Paper rock scissors

<iframe width="560" height="315" src="https://www.youtube.com/embed/VKHFcTRa6B0?si=TLSvewQtucoybj8w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```
POST https://api.pbaumgarten.com/pets/prs

headers = {
    "X-API-KEY": "PROVIDED BY YOUR TEACHER"
}

response if successful = {
    "status": "match",
    "result": "win", "tie", or "lose"
    "your_choice": "rock", "paper" or "scissors",
    "their_choice": "rock", "paper" or "scissors",
    "opponent": "their pet name"
}

response if waiting for someone else = {
    "status": "waiting for opponent"
}
```

```
POST https://api.pbaumgarten.com/pets/prs-check

headers = {
    "X-API-KEY": "PROVIDED BY YOUR TEACHER"
}

response if successful = {
    "status": "match",
    "result": "win", "tie", or "lose"
    "your_choice": "rock", "paper" or "scissors",
    "their_choice": "rock", "paper" or "scissors",
    "opponent": "their pet name"
}

response no response = {
    "status": "no opponent found""
}
```

## Video 16: Screensaver mode (inactivity timer)

<iframe width="560" height="315" src="https://www.youtube.com/embed/boLpGRd4Eps?si=lMQPA8yw3yJhI0Xi" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Video 17: Error handling (wifi issues etc)

<iframe width="560" height="315" src="https://www.youtube.com/embed/4SlD_HSgwCA?si=NerQ5gHs4QlKVo6c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

