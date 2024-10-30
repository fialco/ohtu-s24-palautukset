import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_right_amount_of_edm_players(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)

    def test_right_amount_of_players(self):
        amount = len(self.stats._players)
        self.assertEqual(amount, 5)


    def test_find_right_player(self):
        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

    def test_return_none_if_player_not_found(self):
        player = self.stats.search("Ruutu")
        self.assertEqual(player, None)


    def test_rank_one_is_right(self):
        top_scorers = self.stats.top(4)
        self.assertEqual(str(top_scorers[0]), "Gretzky EDM 35 + 89 = 124")

    def test_rank_five_is_right(self):
        top_scorers = self.stats.top(4, SortBy.POINTS)
        self.assertEqual(str(top_scorers[4]), "Semenko EDM 4 + 12 = 16")

    def test_rank_one_by_goals_is_right(self):
        top_scorers = self.stats.top(4, SortBy.GOALS)
        self.assertEqual(str(top_scorers[0]), "Lemieux PIT 45 + 54 = 99")

    def test_rank_one_by_assists_is_right(self):
        top_scorers = self.stats.top(4, SortBy.ASSISTS)
        self.assertEqual(str(top_scorers[0]), "Gretzky EDM 35 + 89 = 124")