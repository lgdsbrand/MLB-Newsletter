import requests

def get_pitcher_stats(game):
    url = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"
    r = requests.get(url)
    data = r.json()

    matchup = game["matchup"]
    away_team, home_team = matchup.split(" @ ")

    for event in data.get("events", []):
        try:
            comp = event["competitions"][0]
            competitors = comp["competitors"]
            home = next(t for t in competitors if t["homeAway"] == "home")
            away = next(t for t in competitors if t["homeAway"] == "away")

            home_name = home["team"]["shortDisplayName"]
            away_name = away["team"]["shortDisplayName"]

            if home_name == home_team and away_name == away_team:
                home_pitcher = comp.get("startingPitcher", {}).get("home", {})
                away_pitcher = comp.get("startingPitcher", {}).get("away", {})

                home_stats = home_pitcher.get("statistics", [])
                away_stats = away_pitcher.get("statistics", [])

                def format_stats(pitcher, stats):
                    name = pitcher.get("athlete", {}).get("displayName", "Unknown")
                    era = next((s["displayValue"] for s in stats if s["name"] == "ERA"), "N/A")
                    wl = next((s["displayValue"] for s in stats if s["name"] == "wins"), "N/A") + "-" + \
                         next((s["displayValue"] for s in stats if s["name"] == "losses"), "N/A")
                    k9 = next((s["displayValue"] for s in stats if s["name"] == "strikeouts"), "N/A")
                    return name, f"W-L: {wl}, ERA: {era}, K: {k9}"

                home_name, home_stat = format_stats(home_pitcher, home_stats)
                away_name, away_stat = format_stats(away_pitcher, away_stats)

                return {
                    "home_name": home_name,
                    "away_name": away_name,
                    "home_stats": home_stat,
                    "away_stats": away_stat
                }
        except Exception:
            continue

    # Fallback
    return {
        "home_name": "Unknown",
        "away_name": "Unknown",
        "home_stats": "No data",
        "away_stats": "No data"
    }
