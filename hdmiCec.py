#sudo apt-get install libcec-dev build-essential python-dev
import sys
import subprocess
from time import sleep

def getStatus():
	noStatus = True
	while noStatus:
		try:
			tvStatus = tv.is_on()
			noStatus = False
		except:
			print("No Status")
			sleep(2)
	return tvStatus
	
try:
	import cec # pip install cec
except:
	subprocess.run(["sudo", "apt", "install", "libcec-dev"])

if len(sys.argv) > 1:
	command = sys.argv[1]
	cec.init()
	tv = cec.Device(cec.CECDEVICE_TV)
	tvStatus = getStatus()
	#print(f"Status {tv.is_on()}")
	if (command.lower() == "on"):
		while not tvStatus:
			tv.power_on()
			print("Power on")
			sleep(2)
			tvStatus = getStatus()
	elif command.lower() == "off":
		while tvStatus:
			tv.standby()
			print("Power off")
			sleep(2)
			tvStatus = getStatus()
	elif command.lower() == "status":
		tvStatus = getStatus()
		if tvStatus:
			print("Tv On")
		else:
			print("Tv Standby")
	else:
		print("use 'On', 'Off' or 'Status'")
else:
	print("run 'hmdiCec on', 'hdmiCec off' or 'hdmiCec Status")
