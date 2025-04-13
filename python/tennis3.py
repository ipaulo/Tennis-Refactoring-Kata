class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, n):
        if n == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def no_winner(self) -> bool:
        if self.player1_score < 4 and self.player2_score < 4:
            return True

    def is_simple_score(self) -> bool:
        if self.player1_score + self.player2_score == 6:
            return False
        return True

    def simple_score(self) -> str:
        score_list = ["Love", "Fifteen", "Thirty", "Forty"]
        score_name = score_list[self.player1_score]
        return (
            score_name + "-All"
            if (self.player1_score == self.player2_score)
            else score_name + "-" + score_list[self.player2_score]
        )

    def score(self):
        if self.no_winner() and self.is_simple_score():
            return self.simple_score()
        else:
            if self.player1_score == self.player2_score:
                return "Deuce"
            leader_name = (
                self.player1_name
                if self.player1_score > self.player2_score
                else self.player2_name
            )
            return (
                "Advantage " + leader_name
                if (
                    (self.player1_score - self.player2_score)
                    * (self.player1_score - self.player2_score)
                    == 1
                )
                else "Win for " + leader_name
            )
