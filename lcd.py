import lcddriver
import socket

from time import *

lcd = lcddriver.lcd()

lcd.lcd_display_string("  Hello world  ", 1)
lcd.lcd_display_string("1234567890ABCDEF", 2)
