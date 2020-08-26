from riotwatcher import LolWatcher, ApiError
import requests
import sys
from pick import pick
from string import whitespace


# Launches menu, using pick to allow the player to select what they want to do
def runmain():
	global sumname

	title = "Menu - What do you want to do? Choose an options below."
	options = ['Run program', 'Load summoner']
	option, index = pick(options, title)
	print(option)
	if option == "Run program":
		sumname = input('Your summoner name: ')
		sumname = sumname.translate(dict.fromkeys(map(ord, whitespace)))
		launchstattree()
	elif option == "Load summoner":
		saveplayer()
	else:
		print("Error - did not pick a valid option")


# Launch stat tree - load server list, then load rank stats
def launchstattree():
	global element
	from lib import apisettings

	lol_watcher = LolWatcher(apisettings.yourapikey)

	serverselect()

	me = lol_watcher.summoner.by_name(my_region, sumname)

	my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])

	for element in my_ranked_stats:
		if element['queueType'] == 'RANKED_SOLO_5x5':
			statgatherer()
	else:
		print('Error - no data found - check server, and summoner name.')


# Wait for a key press
def waitforkey():
	input("\n\nPress Enter to continue...\n")


# Server select process - starts at listing servers
def serverselect():
	global my_region
	title = "What server do you want?"
	servers = ['Europe West', 'Brazil', 'Europe Nordic and East',
				'Japan', 'Korea', 'Latin America North',
				'Latin America South', 'North America',
				'Oceania', 'Turkey', 'Russia', 'Public Beta']
	serveroption, index = pick(servers, title)
	print(serveroption)
	if serveroption == 'Brazil':
		my_region = 'br1'
		print('\nServer set to Brazil.')
	elif serveroption == 'Europe Nordic and East':
		my_region = 'eun1'
		print('\nServer set to Europe Nordic and East.')
	elif serveroption == 'Europe West':
		my_region = 'euw1'
		print('\nServer set to Europe West.')
	elif serveroption == 'Japan':
		my_region = 'jp1'
		print('\nServer set to Japan.')
	elif serveroption == 'Korea':
		my_region = 'kr1'
		print('\nServer set to Korea.')
	elif serveroption == 'Latin America North':
		my_region = 'la1'
		print('\nServer set to Latin America North.')
	elif serveroption == 'Latin America South':
		my_region = 'la2'
		print('\nServer set to Latin America South.')
	elif serveroption == 'North America':
		my_region = 'na'
		print('\nServer set to North America.')
		my_region = 'na1'
	elif serveroption == 'Oceania':
		my_region = 'oc1'
		print('\nServer set to Oceania.')
	elif serveroption == 'Turkey':
		my_region = 'tr1'
		print('\nServer set to Turkey.')
	elif serveroption == 'Russia':
		my_region = 'ru'
		print('\nServer set to Russia.')
	elif serveroption == 'Public Beta':
		my_region = 'pbe1'
		print('\nServer set to Public Beta.')


# Gathers stats
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


# Allows user to save player, wipe list
def saveplayer():
	global saveloop
	saveloop = True
	while saveloop:
		userchoice = input(
			"Choose option?\n\n1. Add player\n\n2. Wipe list\n\n3. View list of saved players\n\n4. Leave\n")
		if userchoice == '1':
			playername = input("What is the players name?\n")
			if playername == "":
				print("You must input a name.")
			else:
				players = open("lib/players.txt", "a+")
				players.write(playername)
				players.write(",")
				players.close()
		elif userchoice == '2':
			players = open("lib/players.txt", "w+")
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


# Returns list of saved players
def getsavedplayer():
	global sumname
	global saveloop
	try:
		playerfile = open("lib/players.txt", "r")
		lines = playerfile.read().split(',')
		playerfile.close()
		del lines[-1]
		title = 'Please choose the summoner to load in: '
		sumname, index = pick(lines, title)
		print("You have picked", sumname, "will now search for stats.")
		launchstattree()
	except FileNotFoundError:
		print("\n\nYou need to create a list of saved players.\n\n")
		return
