"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'

- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.

- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""


def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
    # Replace the line below with your code
    qualified_games = []
    qualified_players = 0
    current_game_id = -9000

    # if no game data, returns empty list
    if not game_data:
        return qualified_games

    # sorts the list based on date, sorting from most recent to least
    game_data.sort(reverse=True, key=findDate)

    # loop through game data
    for game_info in game_data:
        # keeps track of what the current game is
        if current_game_id != game_info["gameID"]:
            qualified_players = 0
            current_game_id = game_info["gameID"]

        # calculates the average
        attempted = game_info["fieldGoal2Attempted"] + game_info["fieldGoal3Attempted"] + game_info["freeThrowAttempted"]
        made = game_info["fieldGoal2Made"] + game_info["fieldGoal3Made"] + game_info["freeThrowMade"]
        average = (made/attempted) * 100

        # if the average meets the true shooting cutoff, continues logic
        if average >= true_shooting_cutoff:
            # adds a count of 1 to the qualified players
            qualified_players += 1
            # if enough players qualify and the game hasn't qualified already
            if qualified_players >= player_count and game_info['gameID'] not in qualified_games:
                qualified_games.append(game_info["gameID"])

    # returns all qualified games
    return qualified_games


# finds the date for sorting
def findDate(in_game_data):
    return in_game_data['gameDate']
