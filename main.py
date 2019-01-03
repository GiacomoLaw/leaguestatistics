from pathlib import Path
import lolstats

apisettingspath = Path("lib/apisettings.py")

if apisettingspath.exists():
	print("API file present - note that the API key expires every 24 hours")
	lolstats.runmain()
else:
	print("No API file - creating one now")
	createfile = open("lib/apisettings.py", "w+")
	createfile.write("yourapikey = ")
	uapi = input("What is your API key? ")
	createfile = open("lib/apisettings.py", "a+")
	createfile.write("'%s" % uapi)
	createfile.write("'")
	createfile.close()
	print("API file created")
	lolstats.runmain()
