def runmain():
	from riotwatcher import RiotWatcher
	import apisettings

	sumname = input('Your summoner name: ')

	watcher = RiotWatcher(apisettings.yourapikey)

	# to do - region select
	my_region = 'euw1'

	me = watcher.summoner.by_name(my_region, sumname)

	my_ranked_stats = watcher.league.positions_by_summoner(my_region, me['id'])
	# print(my_ranked_stats)
	# ^ only enabled for debugging and bui

	for element in my_ranked_stats:
		if element['queueType'] == 'RANKED_SOLO_5x5':
			current_rank = (element['tier']) + '  ' + (element['rank'])
			points = (element['leaguePoints'])
			wins = (element['wins'])
			losses = (element['losses'])
			total_games = wins + losses
			rate = round(wins*100/total_games, 2)
			print('Current rank: ', current_rank, '| League Points: ', points)
			print('Wins: ', wins, '| Losses: ', losses, '| Total games: ', total_games)
			print('Win rate: ', rate, '%')
			break
	else:
		print('Error - no data found - check server, and summoner name.')
