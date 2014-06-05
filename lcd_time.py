import lcddriver
import socket

from time import *
from datetime import datetime

lcd = lcddriver.lcd()

while True:
	sleep(1)
	lcd.lcd_clear
	lcd.lcd_display_string(datetime.now().strftime('%m%d/%y %X'),1)
	lcd.lcd_display_string(datetime.now().strftime('%a %b %d %Y'),2)
