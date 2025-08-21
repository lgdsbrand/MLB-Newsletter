def enrich_with_dimers(games):
    for game in games:
        # Stubbed enrichment — replace with real scraping logic
        game["weather"] = "Sunny"
        game["wind"] = 12
        game["pick"] = game["matchup"].split(" @ ")[0]  # Away team
        game["ou_model"] = "No Bet"
        game["best_bet"] = "Hendricks U18.5 Outs"
        game["extra_prop"] = "Elly OPS 1.000 in July"
    return games
