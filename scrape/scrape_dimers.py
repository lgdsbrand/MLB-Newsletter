def enrich_with_dimers(games):
    for game in games:
        # Match team names to Dimers format
        # Scrape weather, pick, O/U model, best bet
        game["weather"] = "Sunny"
        game["wind"] = 12
        game["pick"] = "Reds"
        game["ou_model"] = "No Bet"
        game["best_bet"] = "Hendricks U18.5 Outs"
        game["extra_prop"] = "Elly OPS 1.000 in July"
    return games

