# I am using requirements.py instead of a requirements.txt due to the Windows dependant modules
from pip._internal import main

# All required modules
_all_ = [
	"pick == 0.6.4",
	"requests == 2.21.0",
	"riotwatcher == 3.0.0",
]

# Modules required on Windows
windows = ["windows-curses", ]


def install(packages):
	for package in packages:
		main(['install', package])


# Install modules
if __name__ == '__main__':
	from sys import platform
	install(_all_)
	if platform == 'windows':
		install(windows)
