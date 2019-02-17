from pathlib import Path
from lib import functions

# set path of api settings file
apisettingspath = Path("lib/apisettings.py")

# check if the api file exists - if it does, run the main program - if it doesn't, create it
if apisettingspath.exists():
	print("API file present - note that the API key expires every 24 hours")
	functions.runmain()
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
	functions.runmain()
