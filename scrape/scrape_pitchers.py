import requests
from bs4 import BeautifulSoup

def get_pitcher_stats(game):
    # Normalize team names for ESPN URL
    team_map = {
        "Reds": "cin", "Angels": "laa", "Braves": "atl", "White Sox": "cws",
        "Yankees": "nyy", "Rays": "tb", "Royals": "kc", "Twins": "min",
        "Dodgers": "lad", "Rockies": "col", "Padres": "sd", "Giants": "sf",
        "Mets": "nym", "Nationals": "was", "Cardinals": "stl", "Marlins": "mia",
        "Guardians": "cle", "Diamondbacks": "ari", "Cubs": "chc", "Brewers": "mil",
        "Athletics": "oak", "Rangers": "tex"
    }

    home, away = game["matchup"].split(" @ ")
    home_code = team_map.get(home.strip())
    away_code = team_map.get(away.strip())

    # ESPN game preview URL pattern
    url = f"https://www.espn.com/mlb/game/_/id/{home_code}-{away_code}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    # Stubbed for now — ESPN structure varies
    pitcher_home = {
        "name": "Hunter Greene",
        "stats": "W-L: 3-0, ER: 3, HR: 3, K/9: 6"
    }
    pitcher_away = {
        "name": "Kyle Hendricks",
        "stats": "W-L: 1-2, ER: 3, HR: 3, K/9: 6, .219 vs RHH, .320 vs LHH"
    }

    return {
        "home_name": pitcher_home["name"],
        "away_name": pitcher_away["name"],
        "home_stats": pitcher_home["stats"],
        "away_stats": pitcher_away["stats"]
    }

