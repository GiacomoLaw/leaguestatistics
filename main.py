from pathlib import Path
from lib import functions

# Set path of api settings file
apisettingspath = Path("lib/apisettings.py")

# Check if the api file exists - if it does, run the main program - if it doesn't, create it
if apisettingspath.exists():
	print("API file present - note that the API key expires every 24 hours")
	functions.runmain()
# If no API found, create a apisettings file, and then ask the user for their key
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
