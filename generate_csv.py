import pandas as pd
from datetime import datetime
from scrape.scrape_odds import get_odds_data
from scrape.scrape_pitchers import get_pitcher_stats
from scrape.scrape_dimers import enrich_with_dimers
# You can add scrape_teams and scrape_props later

def build_daily_csv():
    date_str = datetime.today().strftime("%Y%m%d")
    matchups = get_odds_data()
    enriched = enrich_with_dimers(matchups)

    rows = []
    for game in enriched:
        pitchers = get_pitcher_stats(game)

        row = {
            "date": date_str,
            "game": game["matchup"],
            "time": game["time"],
            "weather": game["weather"],
            "wind_mph": game["wind"],
            "ml_home": game["ml_home"],
            "ml_away": game["ml_away"],
            "over_under": game["ou"],
            "pitcher_home": pitchers["home_name"],
            "pitcher_away": pitchers["away_name"],
            "stats_home": pitchers["home_stats"],
            "stats_away": pitchers["away_stats"],
            "team_home_stats": "Stubbed team stats",  # Add scrape_teams later
            "team_away_stats": "Stubbed team stats",
            "player_trend": game["extra_prop"],       # Can swap with scrape_props later
            "best_bet": game["best_bet"],
            "pick_to_win": game["pick"],
            "ou_model": game["ou_model"],
            "extra_prop": game["extra_prop"]
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv(f"data/insights_{date_str}.csv", index=False)
    print(f"✅ CSV saved: insights_{date_str}.csv")

if __name__ == "__main__":
    build_daily_csv()

