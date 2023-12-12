class Team:
    def __init__(self, name, strength_of_schedule):
        self.name = name
        self.strength_of_schedule = strength_of_schedule
        self.head_to_head_results = []

    def add_head_to_head_result(self, opponent, result):
        self.head_to_head_results.append((opponent, result))

def determine_playoff(teams):
    # Sort teams based on strength of schedule in descending order
    teams.sort(key=lambda x: x.strength_of_schedule, reverse=True)

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            if teams[i].strength_of_schedule == teams[j].strength_of_schedule:
                head_to_head_winner = determine_head_to_head_winner(teams[i], teams[j])
                if head_to_head_winner:
                    return [head_to_head_winner]
                
    return teams[:4]

def determine_head_to_head_winner(team1, team2):
    # If two teams have the same strength of schedule, it will then ask for a head to head matchup to determine rankings
    result = input(f"Enter head-to-head result between {team1.name} and {team2.name}: (W/L/D)").upper()
    # If the input is W, return team1 or team2 that won the matchup
    if result == "W":
    # If the input is L, return team2 or team1 that lost the matchup
        return team1
    elif result == "L":
        return team2
    # If the input is D, return neither team
    else:
        return None

def main():
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
    main()