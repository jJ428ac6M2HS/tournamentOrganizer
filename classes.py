class Tournament:
    def __init__(self, name):
        self.name = name
        self.list_teams = []
        self.list_teams_name = []
        self.list_games = []
        self.list_games_name = []
        self.list_rounds = []

    def __str__(self):
        str_teams = ''
        str_games = ''
        for team in self.list_teams:
            str_teams += (team.name + ', ')
        for game in self.list_games:
            str_games += (game.name + ', ')
        return "This is tournament {} with teams : {} and games : {}".format(self.name, str_teams, str_games)

    def reset_available(self):
        for team in self.list_teams:
            team.available = True
        for game in self.list_games:
            game.available = True

class Team:
    def __init__(self, name):
        self.name = name
        self.list_opponents = []
        self.list_games = []
        self.available = True

    def __str__(self):
        return "This is team {}".format(self.name)

class Game:
    def __init__(self, name):
        self.name = name
        self.list_players = []
        self.available = True

    def __str__(self):
        return "This is game {}".format(self.name)

class Round:
    def __init__(self, number):
        self.name = 'Round' + str(number)
        self.list_matches = []

    def __str__(self):
        return "This is Round {}".format(self.name)

class Match:
    def __init__(self, name):
        self.name = name
        self.home_team = ''
        self.visiting_team = ''
        self.game = ''

    def __str__(self):
        return "This is Match {} opposing {} to {} on {}".format(self.name, self.home_team, self.visiting_team,
                                                                 self.game)

