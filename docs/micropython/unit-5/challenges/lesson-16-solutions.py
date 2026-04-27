# Lesson 16 Challenge Solutions
# Servos and Scope

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# Servo setup
servo_pin = machine.Pin(13, machine.Pin.OUT)
servo_pwm = machine.PWM(servo_pin, freq=50)

def set_angle(pwm, angle):
    """Set servo to angle (0–180 degrees)."""
    duty = int(40 + (angle / 180) * 75)
    duty = max(40, min(115, duty))
    pwm.duty(duty)

def servo_off():
    servo_pwm.deinit()

# ⭐ Core: Servo sweep
print("Servo sweep 0° → 180° → 0°:")
servo_pwm = machine.PWM(servo_pin, freq=50)

for angle in range(0, 181, 10):
    set_angle(servo_pwm, angle)
    print(f"  {angle}°")
    time.sleep(0.1)

for angle in range(180, -1, -10):
    set_angle(servo_pwm, angle)
    print(f"  {angle}°")
    time.sleep(0.1)

servo_pwm.deinit()

# ⭐⭐ Extension: Servo position tracker using scope
current_angle = 90   # Global position tracker

def move_servo_to(target_angle, speed=10):
    """Smoothly move servo from current_angle to target_angle."""
    global current_angle
    servo_pwm = machine.PWM(servo_pin, freq=50)

    step = 1 if target_angle > current_angle else -1
    for a in range(current_angle, target_angle + step, step):
        set_angle(servo_pwm, a)
        time.sleep(0.02)
    current_angle = target_angle
    servo_pwm.deinit()

print("\nSmooth servo movement:")
positions = [0, 90, 45, 135, 180, 90]
for pos in positions:
    print(f"  Moving to {pos}°")
    move_servo_to(pos)
    time.sleep(0.3)
    print(f"  Current angle: {current_angle}°")

# ⭐⭐⭐ Stretch: Button-controlled servo with position memory
btn_left  = machine.Pin(0,  machine.Pin.IN, machine.Pin.PULL_UP)
btn_right = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

servo_pwm = machine.PWM(servo_pin, freq=50)
servo_pos = 90   # Global position

print("\nButton-controlled servo:")
print("  Left button  → move left (-10°)")
print("  Right button → move right (+10°)")
print("  Both buttons → centre (90°)")
print("Run for 30 seconds...")

set_angle(servo_pwm, servo_pos)
end_time = time.ticks_ms() + 30000
was_l = was_r = False

while time.ticks_diff(time.ticks_ms(), end_time) < 0:
    l = btn_left.value()  == 0
    r = btn_right.value() == 0

    if l and r:
        servo_pos = 90
        np[0] = (0, 80, 0)
    elif l and not was_l:
        servo_pos = max(0, servo_pos - 10)
        np[0] = (80, 0, 0)
    elif r and not was_r:
        servo_pos = min(180, servo_pos + 10)
        np[0] = (0, 0, 80)
    else:
        np[0] = (0, 20, 0)

    set_angle(servo_pwm, servo_pos)
    np.write()
    was_l, was_r = l, r
    time.sleep(0.05)

servo_pwm.deinit()
np[0] = (0, 0, 0)
np.write()
print("Done.")
