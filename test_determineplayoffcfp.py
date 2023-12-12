import unittest
import cfp
from cfp import determine_playoff, Team

def test_determine_playoff():
    # Test sorting by strength of schedule
    team1 = Team("Team 1", 1.5)
    team2 = Team("Team 2", 2.0)
    team3 = Team("Team 3", 1.0)
    team4 = Team("Team 4", 0.5)
    teams = [team1, team2, team3, team4]
    expected_playoff_teams = [team4, team3, team2, team1]
    actual_playoff_teams = determine_playoff(teams)
    assert actual_playoff_teams == expected_playoff_teams

    # Test head-to-head results
    team1.add_head_to_head_result(team2, "W")
    team2.add_head_to_head_result(team1, "L")
    team3.add_head_to_head_result(team4, "W")
    team4.add_head_to_head_result(team3, "L")
    expected_playoff_teams = [team4, team3]
    actual_playoff_teams = determine_playoff(teams)
    assert actual_playoff_teams == expected_playoff_teams

    # Test ties based on overall record
    team1.add_head_to_head_result(team3, "W")
    team2.add_head_to_head_result(team4, "W")
    expected_playoff_teams = [team4, team3, team2, team1]
    actual_playoff_teams = determine_playoff(teams)
    assert actual_playoff_teams == expected_playoff_teams

    # Test ties based on head-to-head record
    team1.add_head_to_head_result(team2, "W")
    team3.add_head_to_head_result(team4, "W")
    expected_playoff_teams = [team4, team3, team2, team1]
    actual_playoff_teams = determine_playoff(teams)
    assert actual_playoff_teams == expected_playoff_teams

    # Test ties based on strength of schedule
    team1.strength_of_schedule = 2.5
    team2.strength_of_schedule = 2.5
    expected_playoff_teams = [team4, team3, team2, team1]
    actual_playoff_teams = determine_playoff(teams)
    assert actual_playoff_teams == expected_playoff_teams

if __name__ == "__main__":
    unittest.main()