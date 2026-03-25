---
title: Setup Guide
layout: default
nav_order: 100
parent: MicroPython Course
---

# Setup Guide
{: .no_toc }

- TOC
{:toc}

---

## What is MicroPython?

Python is a programming language that normally runs on computers — laptops, desktops, servers. When you run a Python script on your laptop, the laptop's operating system (Windows, macOS, Linux) handles loading the program, managing memory, and talking to the hardware.

A **microcontroller** like the ESP32-S3 is a different kind of computer. It has no operating system, no keyboard, no screen, and a tiny amount of memory (kilobytes, not gigabytes). It's designed to run *one program* repeatedly and efficiently — perfect for controlling hardware.

**MicroPython** is a stripped-down version of Python that fits on a microcontroller. It speaks almost exactly the same language as regular Python, but with some differences:
- No `tkinter` or other desktop GUI libraries
- No access to your computer's filesystem — instead, it uses a small filesystem in the chip's flash memory
- Some modules are different (e.g., `machine` instead of system-level hardware access)
- `input()` works when connected to Thonny, but not when the board is running standalone

{: .highlight }
**Flashing firmware** means installing MicroPython onto the ESP32-S3's flash memory. Think of it like installing an operating system. You only need to do this once (or when you want to update MicroPython).

---

## Installing Thonny IDE

**Thonny** is a beginner-friendly Python IDE (Integrated Development Environment — a program for writing and running code). It has built-in support for MicroPython on microcontrollers.

### Windows

1. Go to [https://thonny.org](https://thonny.org)
2. Click the download button for Windows
3. Run the installer — accept all defaults
4. Launch Thonny from your Start menu

### macOS

1. Go to [https://thonny.org](https://thonny.org)
2. Click the download button for macOS
3. Open the `.pkg` or `.dmg` file and follow the prompts
4. Launch Thonny from Applications

### Understanding the Thonny Interface

When you open Thonny, you'll see three main areas:

```
┌──────────────────────────────────────────────┐
│  Menu bar: File, Edit, View, Run, Tools...   │
├──────────────────────────────────────────────┤
│                                              │
│  Script Editor (top panel)                  │
│  — This is where you write your programs    │
│  — Save files here (.py)                    │
│                                              │
├──────────────────────────────────────────────┤
│  Shell / REPL (bottom panel)                │
│  — Type Python commands and run them        │
│    immediately (REPL mode)                  │
│  — See output and error messages            │
│  — Shows >>> when ready for input           │
└──────────────────────────────────────────────┘
```

There's also a **Files panel** (View > Files) that shows files on your computer AND files on the ESP32.

---

## Installing MicroPython on the ESP32-S3

### Step 1: Connect the ESP32-S3

Plug the ESP32-S3 into your computer using a **data USB cable** (not a charge-only cable — some cables only carry power, not data).

{: .important }
**Cable tip:** If your computer doesn't detect the board, try a different USB cable. Many phone charger cables are charge-only and won't work for programming.

### Step 2: Open Thonny's Interpreter Settings

1. In Thonny, go to **Tools > Options**
2. Click the **Interpreter** tab
3. From the dropdown, select **MicroPython (ESP32)**
4. For the port, select your ESP32-S3 (it usually appears as `COM3`, `COM4`, or similar on Windows; `/dev/tty.usbserial-...` on macOS/Linux)

### Step 3: Flash MicroPython Firmware

1. In the Interpreter tab, click **"Install or update MicroPython (esptool)"**
2. Thonny will download the firmware and flash it automatically
3. If prompted to put the board in bootloader mode: hold the **BOOT** button on the ESP32-S3 while plugging it in, then release

{: .note }
The firmware download may take a minute. Wait until Thonny says "Done". The ESP32-S3 will restart automatically.

### Step 4: Verify the Connection

After flashing, you should see `>>>` in the Shell panel at the bottom of Thonny. This is the **REPL** (Read-Eval-Print Loop) — the interactive Python console running on your ESP32-S3.

Type this and press Enter:
```python
print("Hello, MicroPython!")
```

You should see:
```
Hello, MicroPython!
```

If you see this, MicroPython is installed and working!

---

## Troubleshooting Setup Problems

| Problem | Likely Cause | Solution |
|---------|-------------|---------|
| Board not detected (no port in list) | Charge-only USB cable | Try a different cable; look for one labelled "data" |
| Board not detected (correct cable) | Missing driver | Install CP210x or CH340 USB driver from the chip manufacturer |
| `Permission denied` on macOS/Linux | User not in dialout group | Run: `sudo usermod -a -G dialout $USER` then log out and back in |
| `esptool not found` | esptool not installed | In Thonny: Tools > Manage packages > install `esptool` |
| Firmware flash fails | Board not in bootloader mode | Hold BOOT button while plugging in, try again |
| Shell shows garbled text | Wrong baud rate | Check interpreter settings; baud rate should be 115200 |
| REPL not responding | Previous script is running | Press Ctrl+C to interrupt the running script |

---

## Your First Test

Once MicroPython is installed and you can see `>>>` in the Shell, try this test. Type each line and press Enter:

```python
>>> import machine
>>> import neopixel
>>> np = neopixel.NeoPixel(machine.Pin(48), 1)
>>> np[0] = (255, 0, 0)
>>> np.write()
```

The built-in NeoPixel on your ESP32-S3 should turn **red**. Turn it off:

```python
>>> np[0] = (0, 0, 0)
>>> np.write()
```

{: .highlight }
If the LED lit up red, everything is working! You're ready to start the course.

---

## Saving Files

In Thonny, you can save files to two places:

- **Your computer** — for backup and editing later. Files saved here don't run on the ESP32 unless you explicitly send them.
- **The ESP32-S3 (MicroPython device)** — for running on the board.

When you click **File > Save As**, Thonny asks where to save. Choose **"MicroPython device"** to save to the ESP32.

{: .important }
**Special filename: `main.py`**
If you save a file called `main.py` to the ESP32, it will run automatically every time the board powers on — even without a computer connected. This is how you make standalone programs.

For most lessons, you'll save your work to your computer (for safekeeping) and also run it directly via Thonny.

---

## Using the REPL for Quick Tests

The REPL (`>>>` prompt) is perfect for trying out one-liners and experimenting:

```python
>>> 2 + 2
4
>>> print("Hello!")
Hello!
>>> type(42)
<class 'int'>
```

Press **Ctrl+C** at any time to stop a running program and return to the REPL.

Press **Up Arrow** to recall the previous command — saves retyping!

---

You're all set. Head to **[Unit 1: Getting Started](unit-1/)** to write your first programs!
