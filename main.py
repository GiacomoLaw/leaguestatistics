from pathlib import Path
import lolstats

apisettingspath = Path("apisettings.py")

if apisettingspath.is_file():
    print("API file present")
    lolstats
else:
	print("No API file")