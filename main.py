"""
Currently using venv on Python 3.8, these are the required packages :

"""

from classes import Team, Game, Tournament, Round, Match
import sys

a = Team('LPA')
print(a)

NUMBER_OF_ROUNDS = 8
NUMBER_OF_ROUNDS = 3
NUMBER_OF_MATCHES = 8
NUMBER_OF_MATCHES = 3


tournament = Tournament('Tournoi test')

# Create all teams
#for id in range(1, 17):
for id in range(1, 5):
    team = Team('Team'+str(id))
    tournament.list_teams.append(team)
    tournament.list_teams_name.append(team.name)
for team in tournament.list_teams:
    print(team)
print(tournament.list_teams_name)

# Create all games
#for id in range(1, 9):
for id in range(1, 7):
    game = Game('Game' + str(id))
    tournament.list_games.append(game)
    tournament.list_games_name.append(game.name)
for game in tournament.list_games:
    print(game)
print(tournament.list_games_name)

print(tournament)

def print_results():
    for round in tournament.list_rounds:
        print('#################')
        for match in round.list_matches:
            str_round = round.name
            str_match = match.name
            str_home = match.home_team
            str_visiting = match.visiting_team
            str_game = match.game

            print(str_round)
            print('[{}] match {} : {} VS {} on {}'.format(str_round, str_match, str_home, str_visiting, str_game))
            print(match)
            print(str_game)

def find_game(home_team, visiting_team, current_match):
    for game in tournament.list_games:
        print(game.name)
        print(game.list_players)
        print(game.available)
        if not game.available:
            print('game not available, next loop')
            continue
        if home_team not in game.list_players and visiting_team not in game.list_players:
            print("thats a match")
            game.available = False
            game.list_players.append(home_team)
            game.list_players.append(visiting_team)

            current_match.game = game.name
            break
        else:
            print("already played that game")

def find_opponent(current_match):
    for home_team in tournament.list_teams:
        flag_break = False
        print(home_team.name)
        print(home_team.list_opponents)
        print(home_team.list_games)
        print(home_team.available)
        if not home_team.available:
            print('team not available, next loop')
            continue

        for visiting_team in tournament.list_teams:
            print(visiting_team.name)
            print(visiting_team.list_opponents)
            print(visiting_team.list_games)
            print(visiting_team.available)
            if not visiting_team.available:
                print('team not available, next loop')
                continue

            if (home_team.name != visiting_team.name) and (visiting_team.name not in home_team.list_opponents):
                print("that's a match between {} and {}".format(home_team.name, visiting_team.name))
                home_team.list_opponents.append(visiting_team.name)
                home_team.available = False
                visiting_team.list_opponents.append(home_team.name)
                visiting_team.available = False
                find_game(home_team.name, visiting_team.name, current_match)

                current_match.home_team = home_team.name
                current_match.visiting_team = visiting_team.name
                flag_break = True
                break
            else:
                print('this match is not possible')
        if flag_break:
            break


def create_match(current_round, number_matches):
    for i in range(number_matches):
        print('### NEW MATCH ###')
        current_round.list_matches.append(Match(i))
        find_opponent(current_round.list_matches[i])


def create_round(number_rounds, number_matches):
    for i in range(number_rounds):
        print('######### NEW ROUND ###########')
        tournament.list_rounds.append(Round(i))
        create_match(tournament.list_rounds[i], number_matches)
        tournament.reset_available()

        # After 1 round, try to print result to see
    print_results()
    print(tournament.list_rounds)
    print(tournament.list_rounds[0])
    print(tournament.list_rounds[0].list_matches)
    print(tournament.list_rounds[0].list_matches[0])



# Ici on a 8 rounds de 8 matchs chacun
create_round(NUMBER_OF_ROUNDS, NUMBER_OF_MATCHES)

