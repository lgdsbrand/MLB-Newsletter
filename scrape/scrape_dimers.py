import requests
from bs4 import BeautifulSoup

def enrich_with_dimers(games):
    base_url = "https://www.dimers.com/mlb"

    for game in games:
        try:
            away, home = game["matchup"].split(" @ ")
            matchup_url = f"{base_url}/{away.lower().replace(' ', '-')}-vs-{home.lower().replace(' ', '-')}"
            r = requests.get(matchup_url)
            soup = BeautifulSoup(r.text, "html.parser")

            # Weather
            weather_block = soup.find("div", class_="weather")
            game["weather"] = weather_block.text.strip() if weather_block else "Clear"
            game["wind"] = 10  # Stubbed until wind parsing added

            # Pick to win
            pick_block = soup.find("div", class_="pick-to-win")
            game["pick"] = pick_block.text.strip() if pick_block else away

            # O/U model
            ou_block = soup.find("div", class_="over-under-model")
            game["ou_model"] = ou_block.text.strip() if ou_block else "No Bet"

            # Best bet
            best_bet_block = soup.find("div", class_="best-bet")
            game["best_bet"] = best_bet_block.text.strip() if best_bet_block else "No edge"

            # Extra prop
            prop_block = soup.find("div", class_="player-prop")
            game["extra_prop"] = prop_block.text.strip() if prop_block else "No prop"

        except Exception:
            game["weather"] = "Clear"
            game["wind"] = 10
            game["pick"] = away
            game["ou_model"] = "No Bet"
            game["best_bet"] = "No edge"
            game["extra_prop"] = "No prop"

    return games
