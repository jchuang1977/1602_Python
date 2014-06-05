import lcddriver
import socket

from time import *
from datetime import datetime

lcd = lcddriver.lcd()

while True:
	sleep(1)
	lcd.lcd_clear
	lcd.lcd_display_string(datetime.now().strftime('  %I : %M : %S'),1)
	lcd.lcd_display_string(datetime.now().strftime('  %a %b %d %Y'),2)
