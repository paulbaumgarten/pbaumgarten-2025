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

### Text file download - Load into string

```py
import requests

response = requests.get("https://codingquest.io/api/puzzledata?puzzle=1")
if response.status_code == 200:
    print(response.text)
```

### Text file download - Save to file

```py
import requests

response = requests.get("https://codingquest.io/api/puzzledata?puzzle=1")
if response.status_code == 200:
    with open("file.txt", "w") as f:
        f.write(response.text)
```

### JSON download

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

### Binary download – Small files (less than 1MB)

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

### Binary download – Larger files (over 1MB)

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

### Upload a file

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

