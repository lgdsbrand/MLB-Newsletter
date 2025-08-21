import requests

def get_odds_data():
    url = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"
    r = requests.get(url)
    data = r.json()

    games = []
    for event in data.get("events", []):
        try:
            competitions = event["competitions"][0]
            competitors = competitions["competitors"]
            home = next(team for team in competitors if team["homeAway"] == "home")
            away = next(team for team in competitors if team["homeAway"] == "away")

            home_team = home["team"]["shortDisplayName"]
            away_team = away["team"]["shortDisplayName"]
            matchup = f"{away_team} @ {home_team}"

            time = event["date"][11:16]  # Extract HH:MM from ISO timestamp

            odds = competitions.get("odds", [{}])[0]
            ml_home = odds.get("homeTeamOdds", {}).get("moneyLine", "N/A")
            ml_away = odds.get("awayTeamOdds", {}).get("moneyLine", "N/A")
            ou = odds.get("overUnder", "N/A")

            games.append({
                "matchup": matchup,
                "time": time,
                "ml_home": f"{home_team} {ml_home}",
                "ml_away": f"{away_team} {ml_away}",
                "ou": ou,
                "weather": "TBD",
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
