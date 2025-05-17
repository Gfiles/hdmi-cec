#sudo apt-get install libcec-dev build-essential python-dev
import sys
import subprocess
from time import sleep

def getStatus():
	noStatus = True
	count = 0 
	while noStatus:
		try:
			status = tv.is_on()
			#print(f"getStatus: {status}")
			noStatus = False
			count += 1
			if count > 30:
				sys.exit()
		except:
			print("No Status")
			sleep(2)
	return status
	
try:
	import cec # pip install cec
except:
	subprocess.run(["sudo", "apt", "install", "libcec-dev"])

count = 0
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
			tvStatus = getStatus()
			#print(f"Status: {tvStatus}")
			count += 1
			if count > 10:
				sys.exit()
	elif command.lower() == "off":
		while tvStatus:
			tv.standby()
			print("Power off")
			tvStatus = getStatus()
			count += 1
			if count > 10:
				sys.exit()
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
