from pathlib import Path
import msvcrt as m
import lolstats


def wait():
	m.getch()


apisettingspath = Path("apisettings.py")

if apisettingspath.exists():
	print("API file present - note that the API key expires every 24 hours")
	lolstats.runmain()
else:
	print("No API file - press any key to create")
	createfile = open("apisettings.py", "w+")
	createfile.write("yourapikey = ")
	uapi = input("What is your API key? ")
	createfile = open("apisettings.py", "a+")
	createfile.write("'%s" % uapi)
	createfile.write("'")
	createfile.close()
	print("API file created")
	lolstats.runmain()
