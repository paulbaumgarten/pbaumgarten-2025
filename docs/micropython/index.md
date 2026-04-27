---
title: MicroPython
layout: default
nav_order: 11
has_children: true
has_toc: false
---

# MicroPython
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

## Hardware Reference

<div class="hw-card-grid">
  <a href="esp32-s3.html" class="hw-card">
    <div class="hw-card-icon">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 19.5V21M12 3v1.5m0 15V21m3.75-18v1.5m0 15V21m-9-1.5h10.5a2.25 2.25 0 0 0 2.25-2.25V6.75a2.25 2.25 0 0 0-2.25-2.25H6.75A2.25 2.25 0 0 0 4.5 6.75v10.5a2.25 2.25 0 0 0 2.25 2.25Zm.75-12h9v9h-9v-9Z" />
      </svg>
    </div>
    <div>
      <p class="hw-card-title">ESP32-S3</p>
      <p class="hw-card-desc">Pinout &amp; board reference</p>
    </div>
  </a>
  <a href="pico.html" class="hw-card">
    <div class="hw-card-icon">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 19.5V21M12 3v1.5m0 15V21m3.75-18v1.5m0 15V21m-9-1.5h10.5a2.25 2.25 0 0 0 2.25-2.25V6.75a2.25 2.25 0 0 0-2.25-2.25H6.75A2.25 2.25 0 0 0 4.5 6.75v10.5a2.25 2.25 0 0 0 2.25 2.25Zm.75-12h9v9h-9v-9Z" />
      </svg>
    </div>
    <div>
      <p class="hw-card-title">Pico W</p>
      <p class="hw-card-desc">Pinout &amp; board reference</p>
    </div>
  </a>
  <a href="cyd.html" class="hw-card">
    <div class="hw-card-icon">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M9 17.25v1.007a3 3 0 0 1-.879 2.122L7.5 21h9l-.621-.621A3 3 0 0 1 15 18.257V17.25m6-12V15a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 15V5.25A2.25 2.25 0 0 1 5.25 3h13.5A2.25 2.25 0 0 1 21 5.25Z" />
      </svg>
    </div>
    <div>
      <p class="hw-card-title">CYD</p>
      <p class="hw-card-desc">Cheap Yellow Display</p>
    </div>
  </a>
  <a href="HARDWARE-REFERENCE.html" class="hw-card">
    <div class="hw-card-icon">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6h9.75M10.5 6a1.5 1.5 0 1 1-3 0m3 0a1.5 1.5 0 1 0-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m-9.75 0h9.75" />
      </svg>
    </div>
    <div>
      <p class="hw-card-title">Sensors &amp; actuators</p>
      <p class="hw-card-desc">Wiring &amp; component guide</p>
    </div>
  </a>
</div>

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

{: .highlight }
**A note on making mistakes:** Every programmer — including professionals — makes mistakes constantly. Debugging (finding and fixing mistakes) is not a sign of failure; it's a fundamental programming skill. The only way to get better at debugging is to practise it. Be patient with yourself, and remember that a program that finally works after ten failed attempts feels just as good as one that works first time.
