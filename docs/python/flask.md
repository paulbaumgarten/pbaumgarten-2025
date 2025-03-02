---
title: Flask web server
parent: Python notes
layout: default
nav_order: 6
---

# Flask web server
{: .no_toc }

- TOC
{:toc} 

Install the Flask library to host web-based projects run by Python.

Basic template

```py
from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'code used to secure cookies from tampering'

# Return templates/index.html
@app.route("/")
def index_page():
    return render_template("index.html")

# Return a binary file
@app.route('/promovideo')
def promovideo():
    return send_file("promovideo.mp4")

# Use the URL path to supply a parameter
@app.route('/user/<userid>')
def users(userid):
    return "User page for "+userid

# Get values from a HTML form
@app.route("/page2", methods=['GET','POST'])
def page2():
    # HTML with <input name='person'> will create a request.values['person']
    # .values contains .args and .form combined
    form = dict(request.values) # Convert all values into a dictionary
    person = form['person']
    return f"Hello, {person}, welcome to my website"

# Start the web server. These should be the last lines.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
```

Upload a file from webpage to flask

HTML extract

* Note that enctype="multipart/form-data" is mandatory for uploading binary files

```html
<!DOCTYPE html>
<html>
  <body>
    <form action=“http://localhost/upload" method="POST" enctype="multipart/form-data">
      <input type="text" name="person">
      <input type="file" name="my_upload">
      <input type="submit" name="submit" value="Answer">
    </form>
  </body>
</html>
```

Corresponding Python/Flask code

* `secure_filename()` protects from security risks with a user-supplied filename

```py
# from werkzeug.utils import secure_filename
# import os
# app.config['MAX_CONTENT_LENGTH'] = 1<<24 # 16MB

@app.route("/upload", methods=["POST"])
def upload_photo():
    f = request.files['my_upload']  # refer to the HTML <input> name attribute
    f.save(os.path.join(app.root_path, 'photos', secure_filename(f.filename)))
    return 'file uploaded successfully'
```

Send / receive JSON data

```py
@app.route("/api", methods=['GET','POST'])
def api():
    if request.is_json:
        data = request.json # list/dictionary of values
        print(data)
        result = {"status": "received"}
    else:
        result = {"status": "error"}
    return jsonify(result)
```
 
### Jinga2 templates

Jinga2 is a templating language you can use to generate HTML documents from your Python data.

An example of a Jinga2 HTML document, illustrating the most common constructs

```html
{% raw %}
<!DOCTYPE html>
<html>
    <body>
        <!-- Insert content of variable -->
        <h1>Welcome, {{ personName }}!</h1>

        <!-- if statement -->
        {% if personName != "" %}
            <!-- Insert content of variable -->
            <h1>Welcome, {{ personName }}!</h1>
        {% else %}
            <h1>Welcome visitor!</h1>
        {% endif %}

        <!-- for loop -->
        <ul>
        {% for name in people %}
            <li>{{ name }}</li>
        {% endfor %}
        </ul>

        <!-- if variable is defined -->
        {% if variable is defined %}
            <p>variable is defined with value {{ variable }}</p>
        {% endif %}

        <!-- if variable is empty -->
        {% if variable|length %}
            <p>variable is not empty</p>
        {% else %}
            <p>variable is empty</p>
        {% endif %}

        <!-- drop down list: default to the option based on value of `choice` -->
        <select name="day">
            <option {{ "selected" if choice=='Monday' else "" }}>Monday</option>
            <option {{ "selected" if choice=='Tuesday' else "" }}>Tuesday</option>
        </select>

    </body>
</html>
{% endraw %}
```

To render this from Flask

* Place the template HTML file into a templates/ folder for Flask to find it.
* Pass all the Python data you want Jinga2 to have access to via the `render_template()` function.

```py
return render_template("main.html", personName=p, people=names, variable=v)
```


### Minimalist example

Python file

```py
from flask import Flask, render_template, request, send_file
import random

app = Flask(__name__) # Create the server object variable
app.config['SECRET_KEY'] = str(random.randint(0,100000000))

@app.route("/")
def main_page():
    return send_file("main.html")

@app.route("/process", methods=['POST'])
def form_process():
    received = dict(request.values)
    text1 = received['text1'] # Dictionary key is the 'name' attribute in HTML
    # Do whatever processing you want with the data
    print("The user sent",text1)
    # Send a response
    return render_template("response.html", info=text1)

if __name__ == "__main__":
    # Start Flask webserver
    app.run(host="0.0.0.0", port=80, debug=True)
```

main.html

```html
<!DOCTYPE html>
<html>
    <head><title>Flask demo</title></head>
    <body>
        <h1>Welcome to my demo project</h1>
        <form method="POST" action="/process" enctype="multipart/form-data">
            <p>What do you want to send to the server?</p>
            <input type="text" name="text1" value="">
            <input type="submit" name="submit" value="Send">
        </form>
    </body>
</html>
```

templates/response.html

```html
{% raw %}
<!DOCTYPE html>
<html>
    <head><title>Flask demo</title></head>
    <body>
        <h1>Thank you for your submission</h1>
        <p>You sent: {{ info }}</p>
        <a href="/">Return to main</a>        
    </body>
</html>
{% endraw %}
```

