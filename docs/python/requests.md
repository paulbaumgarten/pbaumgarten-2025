---
title: Requests (HTTP/S)
parent: Python notes
layout: default
nav_order: 6
---

# HTTP/S Requests
{: .no_toc }

- TOC
{:toc} 

The requests library provides a convenient means to interact with websites, such as to download or upload files. Install the `requests` library and import it for all these recipes.

## Text file download - Load into string

```py
import requests

response = requests.get("https://codingquest.io/api/puzzledata?puzzle=1")
if response.status_code == 200:
    print(response.text)
```

## Text file download - Save to file

```py
import requests

response = requests.get("https://codingquest.io/api/puzzledata?puzzle=1")
if response.status_code == 200:
    with open("file.txt", "w") as f:
        f.write(response.text)
```

## JSON download

```py
import requests

# Tomorrow's weather forecast for Hong Kong
url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
parameters = { "dataType": "fnd", "lang": "en" }
response = requests.get(url, params=parameters)
if response.status_code == 200: # 200 = Normal/OK
    # Convert json response to list/dictionary structure
    data = response.json() 
    day = data['weatherForecast'][0]['week']
    max_temp = data['weatherForecast'][0]['forecastMaxtemp']['value']
    min_temp = data['weatherForecast'][0]['forecastMintemp']['value']
    wind = data['weatherForecast'][0]['forecastWind']
    summary = data['weatherForecast'][0]['forecastWeather']
    print("The weather for",day)
    print("Minimum",min_temp,"Maximum",max_temp)
    print(summary)
    print("Wind:",wind)
```

## Binary download – Small files (less than 1MB)

```py
import requests, os

# Download a small binary file
response = requests.get("https://cataas.com/cat") # Random cat image
if response.status_code == 200:
    with open('cat.png', 'wb') as f:
        f.write(response.content)
    os.startfile("cat.png") # Open with default Windows application
    # subprocess.call(('open', filepath)) # Mac ... import subprocess
```

## Binary download – Larger files (over 1MB)

```py
import requests, os

url = "https://apod.nasa.gov/apod/image/2105/MWTree_Toledano_6016.jpg"
response = requests.get(url, stream=True) # note the stream=True
chunk_size = 2048 # number of bytes to download at a time
if response.status_code == 200:
    with open('galaxy_tree.jpg', 'wb') as f:
        for chunk in response.iter_content(chunk_size):
            f.write(chunk)
    os.startfile("galaxy_tree.jpg") # Windows
```

## Upload a file

```py
# Simple file upload
f = { 'file': open('report.pdf', 'rb') }
r = requests.post("https://httpbin.org/post", files=f)

# ... or to manually specify a filename and content_type
f = { 'file': 
      ( "newname.pdf", 
        open('report.pdf', 'rb'), 
        "application/pdf", 
        {"Expires": "0"} 
      )
    }
r = requests.post("https://httpbin.org/post", files=f)

# ... or to upload a string as a file
f = { 'file': ("newname.pdf", data_string, "application/pdf", {"Expires": "0"} ) }
r = requests.post("https://httpbin.org/post", files=f)
```

## Using ntfy

<img style="float: right; width: 200px" src="/assets/python/ntfy.jpg">

[Ntfy.sh](https://ntfy.sh) is a cool service that allows you to quickly and easily send notifications to your phone from code. You can either use the service provided by [ntfy.sh](https://ntfy.sh), or self-host it if you have a server to install it on, obtain it from here [https://github.com/binwiederhier/ntfy](https://github.com/binwiederhier/ntfy).

While you can sign up for a free service using the `ntfy.sh` server, the free service does limit you in that channels can not be made private. Anyone who knows your channel name can (a) subscribe to receive messages sent to that channel, and (b) send messages to that channel. Therefore it is recommended that (a) you don't use ntfy.sh for anything private, and (b) you host your own service if possible (it is fairly easy to set up).

```py
import requests, json

CHANNEL = "my-channel"

# Use a self-hosted ntfy server
def test1():
    response = requests.post("https://ntfy.yourdomain.com/"+CHANNEL, 
        data="Test 😀".encode(encoding='utf-8'))
    print(response)

# Send header information with a clickable link
def test2():
    requests.post("https://ntfy.sh/"+CHANNEL,
        data="Test link to my website",
        headers={ "Click": "https://pbaumgarten.com/" })

# Send header information with two action buttons
def test3():
    requests.post("https://ntfy.sh/",
        data=json.dumps({
            "topic": CHANNEL,
            "message": "You left the house. Turn down the A/C?",
            "actions": [
                {
                    "action": "view",
                    "label": "Website",
                    "url": "https://pbaumgarten.com/",
                    "clear": True
                },
                {
                    "action": "http",
                    "label": "Other",
                    "url": "https://pbaumgarten.com",
                    "body": "{\"boo\": 65}"
                }
            ]
        })
    )
```
