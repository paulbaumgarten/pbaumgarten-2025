---
title: Hardware Reference
layout: default
nav_order: 9
parent: MicroPython
has_children: true
---

# Hardware Reference
{: .no_toc }

Quick-reference wiring and code for every component used in this course.

- TOC
{:toc}

---

{: .important }
**Safety first:** Always double-check your wiring before powering on. The ESP32-S3 runs at **3.3V logic** — do not connect 5V signals directly to GPIO pins without a voltage divider. Never short-circuit power and ground pins.

---

## ESP32-S3 Safe Pin Guide

Not all GPIO pins are equal. Some have special functions or restrictions:

| Pins | Notes |
|------|-------|
| GPIO 0 | Good for buttons (has pull-up support). Hold LOW at boot = bootloader mode |
| GPIO 1, 3 | UART TX/RX — avoid using for other things |
| GPIO 6–20 | Generally safe for external components |
| GPIO 45, 46 | Strapping pins — avoid using |
| GPIO 48 | Built-in NeoPixel — already wired on the board |

**Recommended pins for components:**
- Buttons: GPIO 0, GPIO 14
- IR sensor: GPIO 12
- HC-SR04: TRIG = GPIO 5, ECHO = GPIO 4
- Servo: GPIO 13
- Relay: GPIO 15
- 8×8 NeoPixel grid: GPIO 6

---

## 1. Built-in NeoPixel (ESP32-S3)

No external wiring needed — the NeoPixel is soldered onto the board at GPIO 48.

**Code:**
```python
import machine
import neopixel

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)   # 1 LED

np[0] = (255, 0, 0)   # Red (R, G, B) — values 0–255
np.write()            # Send to LED

np[0] = (0, 0, 0)     # Off
np.write()
```

**Colour examples:**

| Colour | RGB tuple |
|--------|-----------|
| Red | (255, 0, 0) |
| Green | (0, 255, 0) |
| Blue | (0, 0, 255) |
| Yellow | (255, 255, 0) |
| Cyan | (0, 255, 255) |
| Magenta | (255, 0, 255) |
| White | (255, 255, 255) |
| Off | (0, 0, 0) |

---

## 2. Push Button (Active-Low)

**Wiring:**

| Button Leg | Connect To |
|-----------|-----------|
| Leg 1 | GPIO pin (e.g., GPIO 0) |
| Leg 2 | GND |

Use `Pin.PULL_UP` to enable the internal pull-up resistor. Without it, the pin "floats" and gives unreliable readings.

**Logic:**
- Button NOT pressed: pin reads `1` (HIGH, pulled up to 3.3V)
- Button pressed: pin reads `0` (LOW, connected to GND)

This is called **active-low**.

**Code:**
```python
from machine import Pin
import time

btn = Pin(0, Pin.IN, Pin.PULL_UP)

while True:
    if btn.value() == 0:   # Button pressed
        print("Pressed!")
    time.sleep(0.05)
```

**Two buttons:**
```python
btn_a = Pin(0, Pin.IN, Pin.PULL_UP)
btn_b = Pin(14, Pin.IN, Pin.PULL_UP)
```

---

## 3. IR Proximity Sensor

**Wiring:**

| IR Sensor Pin | Connect To |
|--------------|-----------|
| VCC | 3.3V |
| GND | GND |
| OUT | GPIO 12 (or any GPIO) |

**Logic:** Active-low — output goes `0` (LOW) when an object is detected.

Some modules have a sensitivity potentiometer (small screw). Turn it to adjust detection range.

**Code:**
```python
from machine import Pin
import time

ir = Pin(12, Pin.IN)

while True:
    if ir.value() == 0:   # Object detected
        print("Object detected!")
    else:
        print("Clear")
    time.sleep(0.1)
```

{: .highlight }
**Did you know?** IR sensors work by emitting infrared light and detecting its reflection. They're used in automatic hand sanitiser dispensers, TV remote controls, and robot obstacle detection.

---

## 4. HC-SR04 Ultrasonic Distance Sensor

**Wiring:**

| HC-SR04 Pin | Connect To |
|------------|-----------|
| VCC | 5V (some modules work on 3.3V — check yours) |
| GND | GND |
| TRIG | GPIO 5 |
| ECHO | GPIO 4 (via voltage divider if module outputs 5V) |

{: .important }
**Voltage divider on ECHO:** Some HC-SR04 modules output 5V on the ECHO pin, which could damage the ESP32-S3's 3.3V GPIO. Add a voltage divider: ECHO → 1kΩ → junction → GPIO, and junction → 2kΩ → GND. HC-SR04**P** variants run natively at 3.3V and don't need this.

**How it works:** Send a 10µs pulse on TRIG. The sensor emits 8 ultrasonic pulses and raises ECHO HIGH until they return. Measure ECHO duration → calculate distance.

```
Distance (cm) = echo_duration_µs / 58.2
```

**Code:**
```python
from machine import Pin
import time

trig = Pin(5, Pin.OUT)
echo = Pin(4, Pin.IN)

def get_distance():
    """Measure distance in cm. Returns -1 if no reading."""
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    timeout = time.ticks_us() + 30000   # 30ms timeout
    while echo.value() == 0:
        if time.ticks_us() > timeout:
            return -1

    start = time.ticks_us()
    timeout = start + 30000
    while echo.value() == 1:
        if time.ticks_us() > timeout:
            return -1

    duration = time.ticks_diff(time.ticks_us(), start)
    return round(duration / 58.2, 1)

while True:
    dist = get_distance()
    if dist != -1:
        print(f"Distance: {dist} cm")
    time.sleep(0.5)
```

{: .highlight }
**Did you know?** This sensor uses the same principle as bat echolocation — emit a sound, measure how long it takes to bounce back.

---

## 5. 9G Micro Servo Motor

**Wiring:**

| Servo Wire Colour | Connect To |
|------------------|-----------|
| Red | 5V |
| Brown or Black | GND |
| Orange or Yellow (signal) | GPIO 13 |

{: .note }
Servos can draw significant current when moving under load. If your ESP32 resets when the servo moves, power the servo from a separate 5V supply (keep GND connected to the ESP32's GND).

**How PWM works for servos:** Send a 50Hz signal. The pulse width (time the signal is HIGH) sets the angle:
- 0.5ms pulse ≈ 0°
- 1.5ms pulse ≈ 90° (centre)
- 2.5ms pulse ≈ 180°

**Code:**
```python
from machine import Pin, PWM
import time

servo = PWM(Pin(13), freq=50)

def set_angle(angle):
    """Move servo to angle (0–180 degrees)."""
    # Map 0–180° to duty cycle 40–115 (0–1023 range, 50Hz)
    # Adjust these values to calibrate your specific servo
    min_duty = 40
    max_duty = 115
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty(duty)

# Move through positions
for angle in [0, 45, 90, 135, 180]:
    set_angle(angle)
    print(f"Angle: {angle}°")
    time.sleep(1)

servo.deinit()   # Release PWM when done
```

**Calibrating your servo:**
If 0° and 180° aren't quite right, adjust `min_duty` and `max_duty`. Try values between 30–50 for min and 110–130 for max.

---

## 6. Relay Module (3.3V)

**Wiring — control side (ESP32 to relay):**

| Relay Pin | Connect To |
|----------|-----------|
| VCC | 3.3V |
| GND | GND |
| IN | GPIO 15 |

**Wiring — load side (motor circuit, separate power):**

| Relay Terminal | Connection |
|---------------|-----------|
| COM | One motor terminal |
| NO (Normally Open) | 5V positive supply |
| Motor other terminal | 5V GND (same GND as ESP32) |

{: .important }
**Separate power circuit:** The relay switches a separate 5V circuit for the motor. The motor should NOT be powered from the ESP32's 3.3V pin — motors draw too much current and will damage the board.

**Logic:**
- `relay.on()` → relay energised → COM connects to NO → motor runs
- `relay.off()` → relay de-energised → COM disconnects from NO → motor stops

**Code:**
```python
from machine import Pin
import time

relay = Pin(15, Pin.OUT)
relay.off()    # Start with motor off

relay.on()     # Motor ON
time.sleep(3)
relay.off()    # Motor OFF
```

---

## 7. WS2812B 8×8 NeoPixel Grid

**Wiring:**

| Grid Terminal | Connect To |
|--------------|-----------|
| 5V or VCC | 5V (external supply recommended for full brightness) |
| GND | GND (same GND as ESP32) |
| DIN (Data In) | GPIO 6 |

{: .important }
**Power note:** 64 LEDs at full white draw ~3.8A. For testing, keep brightness low (max ~50 per channel). For full brightness, use an external 5V power supply rated at 4A or more. Always connect GND of the external supply to the ESP32's GND.

**Pixel numbering:** Pixels are numbered 0–63, left-to-right, top-to-bottom:
```
 0  1  2  3  4  5  6  7   ← Row 0 (top)
 8  9 10 11 12 13 14 15   ← Row 1
16 17 18 19 20 21 22 23   ← Row 2
...
56 57 58 59 60 61 62 63   ← Row 7 (bottom)
```

Formula: `index = row * 8 + col`

**Code:**
```python
import machine
import neopixel

pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 64)

def clear():
    for i in range(64):
        np[i] = (0, 0, 0)
    np.write()

def set_pixel(row, col, r, g, b):
    np[row * 8 + col] = (r, g, b)

def render():
    np.write()

# Example: light up top-left corner
clear()
set_pixel(0, 0, 255, 0, 0)   # Red at row 0, col 0
render()
```

**Framebuffer approach (recommended for animations):**
```python
def make_framebuffer():
    return [[(0, 0, 0)] * 8 for _ in range(8)]

def render_fb(fb):
    for row in range(8):
        for col in range(8):
            np[row * 8 + col] = fb[row][col]
    np.write()

# Update framebuffer, then render once
fb = make_framebuffer()
fb[3][4] = (0, 255, 0)   # Green pixel at row 3, col 4
render_fb(fb)
```

{: .highlight }
**Did you know?** Each WS2812B LED in your grid contains its own tiny control chip. The data signal is passed from LED to LED in a chain — that's why you only need one data wire for all 64 LEDs.

---

## Quick-Reference: Pin Assignments

This course uses these default pin assignments. You can change them, but make sure to update your code:

| Component | Pin(s) |
|-----------|--------|
| Built-in NeoPixel | GPIO 48 (fixed) |
| Button A (left) | GPIO 0 |
| Button B (right) | GPIO 14 |
| IR sensor | GPIO 12 |
| HC-SR04 TRIG | GPIO 5 |
| HC-SR04 ECHO | GPIO 4 |
| Servo | GPIO 13 |
| Relay | GPIO 15 |
| 8×8 NeoPixel grid | GPIO 6 |
