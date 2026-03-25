---
title: "Unit 6: Working with Files"
layout: default
nav_order: 6
parent: MicroPython Course
has_children: true
has_toc: false
---

# Unit 6: Working with Files
{: .no_toc }

Variables disappear when your program stops. Files don't. This unit teaches you to save data permanently — so your programs can remember things between runs, log sensor data, and load settings.

## Lessons in This Unit

| Lesson | Title | Key Concepts |
|--------|-------|-------------|
| [Lesson 17](lesson-17-reading-files.md) | Reading Files | open(), read/readline/readlines, with statement, parsing CSV |
| [Lesson 18](lesson-18-writing-files.md) | Writing Files and Data Logging | write mode, append mode, CSV logging, relay + motor |

## New Hardware: Relay Module + DC Motor

A relay is an electrically-controlled switch — it uses a small 3.3V signal from the ESP32 to switch a separate 5V circuit for the motor. This lets you control high-current devices safely.

## About the MicroPython Filesystem

The ESP32-S3 stores files in its flash memory — think of it as a tiny USB drive built into the chip. Files persist between power cycles (unlike RAM). Thonny's file browser lets you create, view, and manage files on the device.

Limitations:
- Total storage is typically 4–16MB (plenty for our purposes)
- Writing to flash is slower than RAM
- Don't write files in tight loops — space is limited

## What You'll Be Able to Do by the End

- Read text and CSV files from the ESP32's filesystem
- Write and append to files
- Log sensor data automatically
- Control a DC motor via a relay
- Build a complete data-logging system with motor control

{: .highlight }
File I/O appears everywhere in real software — from game high scores to server logs to configuration files. After this unit you can build programs that remember things.
