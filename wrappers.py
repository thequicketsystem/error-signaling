import board
import neopixel

# our strip has 60 LEDs
NUM_PIXELS = 60

# delay of 125ms between pulses
FLASH_DELAY = 125000000

GREEN = (0, 255, 0)
RED = (255, 0, 0)
OFF = (0, 0, 0)

# the dataline is on GPIO 18
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS)

# pulse a given color for the set flash delay
def pulse(color):
	pixels.fill(color)
	delay_ns(FLASH_DELAY)
	pixels.fill(OFF)
	delay_ns(FLASH_DELAY)

# set solid green
def setStatusOkay():
	pixels.fill(GREEN)

# pulse red twice before going solid red
def setStatusError():
	pulse(RED)
	pulse(RED)
	pixels.fill(RED)

# startup
for i in range(NUM_PIXELS):
	pixels[i] = GREEN
	delay_ns(FLASH_DELAY // 100)

pixels.fill(OFF)
