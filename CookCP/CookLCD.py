# A Python "module" that sets up an LCD screen for CookC Python game.
import time
import RPi.GPIO as GPIO # This module can only be run on a Raspberry Pi.
from RPLCD.gpio import CharLCD


# Raspberry Pi pin configuration:
lcd_rs        = 7
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = CharLCD(pin_rs=lcd_rs, pin_rw=6, pin_e=lcd_en, pins_data=[lcd_d4, lcd_d5, lcd_d6, lcd_d7], numbering_mode=GPIO.BOARD)

# Print a two line message
lcd.write_string('LCD\nInitialized')
time.sleep(1.0)
lcd.clear()
lcd.write_string('Welcome to\nCookCP!')

def write(message):
    lcd.write_string(message)
