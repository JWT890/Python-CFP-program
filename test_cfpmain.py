import unittest
import cfp
from cfp import main, Team, determine_playoff, determine_head_to_head_winner


class TestMain(unittest.TestCase):
# from cfp write a unit test for the main() function
    def test_main(self):
        teams = []
        for _ in range(4):
            team_name = input("Enter team name: ")
            sos = float(input("Enter strength of schedule: "))
            teams.append(Team(team_name, sos))
    
        for i in range(len(teams)):
            for j in range(i + 1, len(teams)):
                teams[i].add_head_to_head_result(teams[j], None)
        
        playoff_teams = determine_playoff(teams)
        
        print("\nPlayoff Teams: ")
        for i, team in enumerate(playoff_teams):
            print(f"{i}. {team.name}")
        
    

if __name__ == "__main__":
    unittest.main()