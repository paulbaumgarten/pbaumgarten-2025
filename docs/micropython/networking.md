---
title: Networking
parent: MicroPython notes
layout: default
nav_order: 20
---

# Networking with MicroPython
{: .no_toc }

- TOC
{:toc} 

## Connect to wifi

* Requires [stc.py](/docs/micropython/stc.py) Utility functions for STC projects (connect to wifi, get current time, send ntfy message)

```python
import stc

# Provide the SSID and PASSWORD for your Wifi networks
# You may want to add your home wifi to this?
# For example: NETWORKS = [("SCWiFi","wifi1234"),("homewifi","password")]

NETWORKS = [("SCWiFi","wifi1234")]
ip = stc.connect_to_wifi(NETWORKS)
print(f"You are connected using IP address {ip}")
```

## Get current date/time

* Requires an active Internet connection over wifi (as per above)

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
stc.set_correct_time(timezone_offset_hours=8) # Specify timezone difference from UTC

# Use this every time you want to fetch the time
year, month, mday, hour, minute, second, weekday, yearday = time.localtime()
print(f"Current time/date: {hour:02}:{minute:02}:{second:02} {year:04}-{month:02}-{mday:02}")
```

## Send a message via ntfy

* Requires: Sign up for a channel at [ntfy.sh/app](https://ntfy.sh/app)

```python
import stc
NETWORKS = [("SCWiFi","wifi1234")]
ip = stc.connect_to_wifi(NETWORKS)
print(f"You are connected using IP address {ip}")

stc.send_nfty_message("your-channel", "This is your message")
```

## Internet communication

Use the [urequests](https://pypi.org/project/micropython-urequests/) library

```python
import urequests

# 1. Download TEXT data from a GET HTTPS request
response = urequests.get("https://example.com/text")
text_data = response.text
response.close()
print("Text Data:", text_data)

# 2. Download JSON data from a GET HTTPS request, converted into a Dict
response = urequests.get("https://jsonplaceholder.typicode.com/todos/1")
json_data = response.json()
response.close()
print("JSON Data (GET):", json_data)

# 3. Download JSON data from a POST HTTPS request with header values sent, converted into a Dict
url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Replace with your token
}
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = urequests.post(url, headers=headers, json=payload)
json_data = response.json()
response.close()
print("JSON Data (POST):", json_data)
```

## ESP NOW

ESP NOW is a wireless protocol specifically for ESP devices to create a mesh network.

```python
import machine
import time
import stc
import espnow

# Button
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Connect to wifi
stc.connect_to_wifi([["SCWiFi","wifi1234"]])

# Setup ESPNow
e = espnow.ESPNow()
e.active(True)
peer = b'\xff\xff\xff\xff\xff\xff' # Broadcast address
e.add_peer(peer) # Add as peers any devices you wish to transmit to

# Let's go
points = Points()
while True:
    sender, msg = e.irecv(200)
    if msg:
        print(f"Message received from {sender}: {msg}")
    if button.value():
        print("Broadcasting hello")
        e.send(peer, 'Hello'.encode('utf-8'))
    time.sleep(0.2)
```

Note: To convert a MAC address string like "AB:12:34:CD:56:78" into the format required by the espnow.ESPNow.add_peer() method, which requires a bytes object, you can follow these steps:

```python
mac = "AB:12:34:CD:56:78"
peer = bytes(int(part, 16) for part in mac.split(':'))
print(peer)  # Output: b'\xab\x12\x34\xcd\x56\x78'
```
