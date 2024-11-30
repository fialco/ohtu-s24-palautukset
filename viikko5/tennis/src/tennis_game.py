class TennisGame:
    SCORES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty", 4: "Game"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def tie_game(self):
        if self.player1_score >= 3:
            return "Deuce"
        else:
            return f"{self.SCORES[self.player1_score]}-All"
        
    def late_game(self):
        score_diff = self.player1_score - self.player2_score

        if score_diff == 1:
            return f"Advantage {self.player1_name}"
        elif score_diff == -1:
            return f"Advantage {self.player2_name}"
        elif score_diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def mid_game(self):
        return f"{self.SCORES[self.player1_score]}-{self.SCORES[self.player2_score]}"

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.tie_game()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.late_game()
        else:
            return self.mid_game()
