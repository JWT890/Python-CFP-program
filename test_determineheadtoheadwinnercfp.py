import unittest
from cfp import determine_head_to_head_winner, Team

def test_determine_head_to_head_winner():
    team1 = Team("Team 1", 1.0)
    team2 = Team("Team 2", 1.0)
    assert determine_head_to_head_winner(team1, team2) == team1

    team1 = Team("Team 1", 1.0)
    team2 = Team("Team 2", 2.0)
    assert determine_head_to_head_winner(team1, team2) == team2

    team1 = Team("Team 1", 2.0)
    team2 = Team("Team 2", 1.0)
    assert determine_head_to_head_winner(team1, team2) == None

    team1 = Team("Team 1", 2.0)
    team2 = Team("Team 2", 2.0)
    assert determine_head_to_head_winner(team1, team2) == None

if __name__ == "__main__":
    unittest.main()