import msvcrt as m
import requests


def waitforkey():
	m.getch()


def serverselect():
	url = "https://raw.githubusercontent.com/GiacomoLaw/lolstats/master/lib/serverlist.json"
	data = requests.get(url).json()
	for index, element in enumerate(data, start=1):
		print("{}. {}".format(index, element['richname']))


print(serverselect())
