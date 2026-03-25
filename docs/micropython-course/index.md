---
title: MicroPython Course
layout: default
nav_order: 11
has_children: true
has_toc: false
---

# MicroPython Course
{: .no_toc }

Welcome! This is a complete, self-paced programming course that teaches Python fundamentals through hands-on hardware projects using the ESP32-S3 microcontroller and MicroPython.

Every lesson involves real hardware — LEDs that light up, sensors that detect objects, motors that spin. The hardware makes abstract programming concepts concrete and keeps things interesting.

{: .highlight }
**Who is this course for?** Students who are new to programming and want to learn Python through building real things. No prior programming experience needed — just curiosity and enthusiasm.

---

## What You Will Learn

| Unit | Lessons | Programming Concept | New Hardware |
|------|---------|--------------------|-|
| Unit 1: Getting Started | 1–4 | print, variables, data types, strings, expressions | ESP32-S3 built-in NeoPixel |
| Unit 2: Making Decisions | 5–7 | if/elif/else, comparison operators, logical operators | Push buttons |
| Unit 3: Loops & Repetition | 8–10 | while loops, for loops, range(), break, continue | IR sensor |
| Unit 4: Collections of Data | 11–13 | 1D lists, list operations, iterating lists | HC-SR04 ultrasonic sensor |
| Unit 5: Functions & Modularity | 14–16 | def, parameters, return values, scope | 9G servo motor |
| Unit 6: Working with Files | 17–18 | File I/O, CSV, data logging | Relay + DC motor |
| Unit 7: The Grid | 19–21 | 2D lists, nested loops, grid rendering | WS2812B 8×8 NeoPixel grid |
| Unit 8: Capstone Project | 22–24 | All concepts integrated | All hardware |

---

## What You Need

### Hardware

- **ESP32-S3 development board** — the main microcontroller. It has a **built-in NeoPixel RGB LED on GPIO 48** that you'll use from the very first lesson.
- **Breadboard and jumper wires** — for connecting external components
- **Push buttons** — momentary switches for physical input
- **IR proximity sensor** — detects nearby objects using infrared light
- **HC-SR04 ultrasonic distance sensor** — measures distance using sound pulses
- **9G micro servo motor** — a motor that holds a precise angle
- **3.3V relay module** — an electrically-controlled switch for the motor
- **5V geared DC motor** — switched on/off by the relay
- **WS2812B 8×8 NeoPixel grid** — 64 individually addressable RGB LEDs

{: .note }
**Introduce hardware gradually.** Units 1–2 use only the built-in NeoPixel — no extra wiring needed. New components are added one at a time.

### Software

- **Thonny IDE** — a beginner-friendly Python editor with built-in MicroPython support. Free download from [thonny.org](https://thonny.org).
- **MicroPython firmware** for ESP32-S3 — installed via Thonny (see the Setup Guide).

---

## How to Use This Course

This course is designed to be worked through **independently at your own pace**. A reasonable pace is 2–3 lessons per week, giving you about 10–12 weeks to complete the full course.

**Each lesson includes:**
1. Clear concept explanations with code examples
2. A step-by-step guided project you build yourself
3. Challenges (⭐ Core / ⭐⭐ Extension / ⭐⭐⭐ Stretch) to test yourself
4. Common mistakes and debugging tips
5. Key vocabulary definitions

**Tips for success:**
- **Type the code yourself** rather than copy-pasting. It sounds tedious but typing helps you notice every detail and builds muscle memory.
- **Make mistakes on purpose.** Change a value, remove a bracket, misspell something — see what error appears. This is how experienced programmers learn to debug.
- **Read the error messages.** Python's error messages are actually quite helpful once you know how to read them.
- **If you get stuck**, check the Common Mistakes section, reread the concept explanation, then check the challenge solutions.

---

## Before You Start

Read the **[Setup Guide](SETUP-GUIDE.html)** first — it walks you through installing Thonny and getting MicroPython running on your ESP32-S3.

Once setup is done, jump straight into **[Unit 1: Getting Started](unit-1/)**.

The **[Hardware Reference](HARDWARE-REFERENCE.html)** is a quick-reference wiring guide for all components — useful whenever you're connecting new hardware.

---

{: .highlight }
**A note on making mistakes:** Every programmer — including professionals — makes mistakes constantly. Debugging (finding and fixing mistakes) is not a sign of failure; it's a fundamental programming skill. The only way to get better at debugging is to practise it. Be patient with yourself, and remember that a program that finally works after ten failed attempts feels just as good as one that works first time.
