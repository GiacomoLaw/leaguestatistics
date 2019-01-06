from riotwatcher import RiotWatcher
import requests
import sys
from pick import pick
import apisettings


# main program

def runmain():
	global sumname

	useroption = input("Do you want to save or load a summoner? ")
	if useroption == "yes" or useroption == "y":
		saveplayer()
	else:
		sumname = input('Your summoner name: ')
		launchstattree()


def launchstattree():
	global element
	watcher = RiotWatcher(apisettings.yourapikey)

	serverselect()

	me = watcher.summoner.by_name(my_region, sumname)

	my_ranked_stats = watcher.league.positions_by_summoner(my_region, me['id'])

	for element in my_ranked_stats:
		if element['queueType'] == 'RANKED_SOLO_5x5':
			statgatherer()
	else:
		print('Error - no data found - check server, and summoner name.')


# wait for a key press

def waitforkey():
	input("\n\nPress Enter to continue...\n")


# server select process - starts at listing servers

def serverselect():
	global my_region
	url = "https://raw.githubusercontent.com/GiacomoLaw/lolstats/master/lib/serverlist.json"
	data = requests.get(url).json()
	for index, regionelement in enumerate(data, start=1):
		print("\n{}. {}".format(index, regionelement['richname']))
	server_choice = input("\n\nWhat server do you want? Enter the number. ")
	if server_choice == '1':
		my_region = 'br1'
		print('\nServer set to Brazil.')
	elif server_choice == '2':
		my_region = 'eun1'
		print('\nServer set to Europe Nordic and East.')
	elif server_choice == '3':
		my_region = 'euw1'
		print('\nServer set to Europe West.')
	elif server_choice == '4':
		my_region = 'jp1'
		print('\nServer set to Japan.')
	elif server_choice == '5':
		my_region = 'kr1'
		print('\nServer set to Korea.')
	elif server_choice == '6':
		my_region = 'la1'
		print('\nServer set to Latin America North.')
	elif server_choice == '7':
		my_region = 'la2'
		print('\nServer set to Latin America South.')
	elif server_choice == '8':
		my_region = 'na'
		print('\nServer set to North America.')
	elif server_choice == '9':
		my_region = 'oc1'
		print('\nServer set to Oceania.')
	elif server_choice == '10':
		my_region = 'tr1'
		print('\nServer set to Turkey.')
	elif server_choice == '11':
		my_region = 'ru'
		print('\nServer set to Russia.')
	elif server_choice == '12':
		my_region = 'pbe1'
		print('\nServer set to Public Beta.')
	else:
		print('\nError. Select one of the numbers.')
		waitforkey()
		sys.exit("Valid number not selected.")


# gathers stats

def statgatherer():
	global element
	current_rank = (element['tier']) + '  ' + (element['rank'])
	points = (element['leaguePoints'])
	wins = (element['wins'])
	losses = (element['losses'])
	total_games = wins + losses
	rate = round(wins * 100 / total_games, 2)
	print('\n\nCurrent rank: ', current_rank, '| League Points: ', points)
	print('Wins: ', wins, '| Losses: ', losses, '| Total games: ', total_games)
	print('Win rate: ', rate, '%')
	waitforkey()
	sys.exit(0)


# allows user to save player, wipe list

def saveplayer():
	saveloop = True
	while saveloop:
		userchoice = input("Choose option?\n\n1. Add player\n\n2. Wipe list\n\n3. View list of saved players\n\n4. Leave\n")
		if userchoice == '1':
			playername = input("What is the players name?\n")
			players = open("players.txt", "a+")
			players.write(playername)
			players.write(",")
			players.close()
		elif userchoice == '2':
			players = open("players.txt", "w+")
			players.write("")
			players.close()
		elif userchoice == '3':
			getsavedplayer()
		elif userchoice == '4':
			return
		else:
			print("Please select a valid option.")
			waitforkey()
			sys.exit("Valid number not selected.")


# returns list of saved players

def getsavedplayer():
	global sumname
	playerfile = open("players.txt", "r")
	lines = playerfile.read().split(',')
	playerfile.close()
	del lines[-1]
	title = 'Please choose the summoner to load in: '
	sumname, index = pick(lines, title)
	print("You have picked", sumname, "will now search for stats.")
	launchstattree()
