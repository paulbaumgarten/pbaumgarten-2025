import machine
import uos
from ili9341 import Display, color565
from xglcd_font import XglcdFont
from xpt2046 import Touch

#########################################################
## Import checks
#########################################################

required_files = ["ili9341.mpy", "xglcd_font.mpy", "xpt2046.mpy", "Unispace12x24.c"]
for file in required_files:
    try:
        uos.stat(file)
    except OSError:
        raise AssertionError(f"Required file missing: {file}")

#########################################################
## Onboard LED
#########################################################

class LED:
    def __init__(self, r, g, b):
        self.red = machine.Pin(r, machine.Pin.OUT)
        self.green = machine.Pin(g, machine.Pin.OUT)
        self.blue = machine.Pin(b, machine.Pin.OUT)
        self.red.on() # off
        self.green.on() # off
        self.blue.on() # off
        self.blink_counter = 0
        self.blink_rate = 100

    def blink(self):
        self.blink_counter = (self.blink_counter + 1) % self.blink_rate
        self.green.off() if self.blink_counter < (self.blink_rate//2) else self.green.on()

    def off(self):
        self.red.on() # off
        self.green.on() # off
        self.blue.on() # off

    def green(self):
        self.red.on() # off
        self.green.off() # on
        self.blue.on() # off

    def red(self):
        self.red.off() # on
        self.green.on() # off
        self.blue.on() # off

    def blue(self):
        self.red.on() # off
        self.green.on() # off
        self.blue.off() # on


#########################################################
## Colours for the display
#########################################################

class Colors: # Colors for TFT. Color codes are BGR
    white = color565(255, 255, 255)
    grey = color565(64, 64, 64)
    black = color565(0, 0, 0)
    red = color565(0, 0, 255)
    green = color565(0, 255, 0)
    blue = color565(255, 0, 0)
    yellow = color565(0, 255, 255)
    magenta = color565(255, 0, 255)
    cyan = color565(255, 255, 0)
    pink = color565(255,105,180)
    orange = color565(0, 165, 255)
    purple = color565(128, 0, 128)
    brown = color565(42, 42, 165)
    light_blue = color565(230, 216, 173)
    lime = color565(0, 255, 128)
    olive = color565(0, 128, 128)
    gold = color565(0, 215, 255)
    navy = color565(128, 0, 0)
    teal = color565(128, 128, 0)
    maroon = color565(0, 0, 128)
    violet = color565(238, 130, 238)
    salmon = color565(250, 128, 114)
    turquoise = color565(208, 224, 64)

#########################################################
## TouchScreenHandler
#########################################################

class TouchScreenHandler:
    def __init__(self):
        self._pressed = False
        self._x = 0
        self._y = 0

    def press(self, x, y):
        """Interrupt handler to store the touch event."""
        self._pressed = True
        self._x = x
        self._y = y

    @property
    def pressed(self):
        """Returns whether the screen is currently pressed."""
        return self._pressed

    @property
    def x(self):
        """Returns the x-coordinate of the last press."""
        return self._x if self._pressed else None

    @property
    def y(self):
        """Returns the y-coordinate of the last press."""
        return self._y if self._pressed else None

    def getpress(self):
        """
        Returns the (x, y) tuple if a press event occurred, else None.
        Resets the pressed state after returning.
        """
        if self._pressed:
            press_coords = (self._x, self._y)
            self._pressed = False  # Reset the press state
            return press_coords
        return None


#########################################################
## Define objects for UX
#########################################################

# Display and touchscreen
spi_1 = machine.SPI(1, baudrate=10000000, sck=machine.Pin(14), mosi=machine.Pin(13), miso=machine.Pin(12))
display = Display(spi_1, dc=machine.Pin(2), cs=machine.Pin(15), rst=machine.Pin(15), width=320, height=240, rotation=0)
touchscreen = Touch(spi_1, cs=machine.Pin(33), int_pin=machine.Pin(36), width=320, height=240)

# Font
font = XglcdFont('Unispace12x24.c', 12, 24)

# Backlight
backlight = machine.Pin(27, machine.Pin.OUT)
backlight.on()

# Onboard LED
led = LED(r=4,g=16,b=17)

# Instantiate the touch screen object
screen = TouchScreenHandler()

# Set the event handler
touchscreen.int_handler = screen.press

