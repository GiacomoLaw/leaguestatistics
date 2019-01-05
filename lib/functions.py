import requests
import sys

# main program


def runmain():
	global element
	from riotwatcher import RiotWatcher
	from lib import apisettings

	sumname = input('Your summoner name: ')

	watcher = RiotWatcher(apisettings.yourapikey)

	serverselect()

	me = watcher.summoner.by_name(my_region, sumname)

	my_ranked_stats = watcher.league.positions_by_summoner(my_region, me['id'])
	# print(my_ranked_stats)
	# ^ only enabled for debugging and bui

	for element in my_ranked_stats:
		if element['queueType'] == 'RANKED_SOLO_5x5':
			statgatherer()
	else:
		print('Error - no data found - check server, and summoner name.')


# wait for a key press

def waitforkey():
	input("\n\nPress Enter to continue...")


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
	sys.exit()


# allows user to save player, wipe list

def saveplayer():
	userchoice = input("What do you want to do?\n\n1. Add player\n\n2. Wipe list\n\n3. Leave\n")
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
		return


# returns list of saved players

def getsavedplayer():
	text_file = open("players.txt", "r")
	lines = text_file.read().split(',')
	print(lines)
	print(len(lines))
	text_file.close()
