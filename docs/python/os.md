---
title: Operating system
parent: Python notes
layout: default
nav_order: 6
---

# Operating system utilities
{: .no_toc }

- TOC
{:toc} 

There are a range of powerful functions Python provides for working with the operating system and file/folder system of your computer.

Import the os library for these code recipes.

```py
# Check if a file or folder exists of a given name
if os.path.exists("filename.txt"):
    print("The item exists")

# Check if a file exists
if os.path.isfile("filename.txt"):
    print("The item is a file")

# Check if a folder exists
if os.path.isdir("documents"):
    print("The item is a folder/directory")

# Delete a file - USE WITH CAUTION
os.remove("file.txt")

# Rename a file
os.rename("oldfile.txt", "newfile.txt")

# Create a folder - Will error if it already exists
os.mkdir("folder")

# Remove a folder - Will error if it is not empty
os.rmdir("folder")

# Get current logged in user
username = os.getlogin()

# Get the users home folder
home = os.path.expanduser("~")

# Get the users desktop folder (Note: For Windows requires minimum of Windows 7)
desktop = os.path.expanduser("~/Desktop")

# Get a list of all files and sub folders within a folder 
# (will not recursively give contents of subfolders)
files = os.listdir( "/folder/name" )
```
