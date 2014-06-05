import lcddriver
import socket

from time import *
from datetime import datetime
from subprocess import *


lcd = lcddriver.lcd()
cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def run_cmd(cmd):
       p = Popen(cmd, shell=True, stdout=PIPE)
       output = p.communicate()[0]
       return output


ipaddr = run_cmd(cmd)
ipaddrstr = 'IP:' + ipaddr 	

while True:
	sleep(1)
	lcd.lcd_clear
	lcd.lcd_display_string(datetime.now().strftime('%m%d/%y %X'),1)
	lcd.lcd_display_string(ipaddrstr,2)
