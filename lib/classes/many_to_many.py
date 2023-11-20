class Game:

    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if (not hasattr(self, 'title') and isinstance(title, str) and len(title) > 0):
            self._title = title
        
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set(result.player for result in Result.all if result.game == self))

    def average_score(self, player):
        player_scores = [result.score for result in player.results() if result.game == self]
        if len(player_scores) > 0:
            return sum(player_scores) / len(player_scores)
        else:
            return 0

class Player:
    
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if (isinstance(username, str) and (2 <= len(username) <= 16)):
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set(result.game for result in Result.all if result.player == self))

    def played_game(self, game):
        return True if game in self.games_played() else False

    def num_times_played(self, game):
        filtered_games = list(filter(lambda x: x.game == game, self.results()))
        return len(filtered_games)
    
    @classmethod
    def highest_scored(cls, game):
        player_scores = {}
        for player in cls.all:
            player_scores[player] = game.average_score(player)
        highest_score = max(player_scores.values())
        top_players = [player for player, score, in player_scores.items() if score == highest_score]
        return top_players[0] if top_players else None

class Result:
    
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if (not hasattr(self, 'score') and isinstance(score, int) and (1 <= score <= 5000)):
            self._score = score