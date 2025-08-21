import requests
from bs4 import BeautifulSoup

def get_odds_data():
    url = "https://www.espn.com/mlb/scoreboard"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    games = []
    for card in soup.select(".Scoreboard"):
        try:
            teams = card.select(".team-name")
            home_team = teams[1].text.strip()
            away_team = teams[0].text.strip()
            matchup = f"{away_team} @ {home_team}"

            time = card.select_one(".game-time").text.strip()

            odds_block = card.select_one(".odds-details")
            ml_home = odds_block.select(".moneyline")[1].text.strip()
            ml_away = odds_block.select(".moneyline")[0].text.strip()
            ou = odds_block.select_one(".over-under").text.strip()

            games.append({
                "matchup": matchup,
                "time": time,
                "ml_home": ml_home,
                "ml_away": ml_away,
                "ou": ou,
                "weather": "TBD",      # To be filled by Dimers
                "wind": "TBD",
                "best_bet": "TBD",
                "pick": "TBD",
                "ou_model": "TBD",
                "extra_prop": "TBD"
            })
        except Exception as e:
            print(f"Error parsing game: {e}")
            continue

    return games
