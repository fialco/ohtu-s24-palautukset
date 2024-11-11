import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
    
    def __str__(self):
        return f"{self.name:20} {self.team}  {self.goals} + {self.assists} = {self.goals + self.assists}"
        

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.players = []

        for player_dict in self.response:
            player = Player(player_dict)
            self.players.append(player)

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players

    def top_scorers_by_nationality(self, nationality):

        nat_list = []

        for player in self.players:
            if player.nationality == nationality:
                nat_list.append(player)

        nat_list.sort(key=lambda player:player.assists+player.goals, reverse=True)
        return nat_list