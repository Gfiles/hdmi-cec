#sudo apt-get install libcec-dev build-essential python-dev
import sys
import subprocess
from time import sleep

try:
	import cec # pip install cec
except:
	subprocess.run(["sudo", "apt", "install", "libcec-dev"])

if len(sys.argv) > 1:
	command = sys.argv[1]
	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	tvStatus = tv.is_on()
	#print(f"Status {tv.is_on()}")
	if (command.lower() == "on"):
		while not tvStatus:
			tv.power_on()
			print("Power on")
			sleep(2)
			tvStatus = tv.is_on()
	elif command.lower() == "off":
		while tvStatus:
			tv.standby()
			print("Power off")
			sleep(2)
			tvStatus = tv.is_on()
	else:
		print("use 'on' or 'off'")
else:
	print("run 'hmdi on' or 'hdmi off'")
