team_logo_map = {
    "Reds": "cin", "Angels": "laa", "Braves": "atl", "White Sox": "cws",
    "Yankees": "nyy", "Rays": "tb", "Royals": "kc", "Twins": "min",
    "Dodgers": "lad", "Rockies": "col", "Padres": "sd", "Giants": "sf",
    "Mets": "nym", "Nationals": "was", "Cardinals": "stl", "Marlins": "mia",
    "Guardians": "cle", "Diamondbacks": "ari", "Cubs": "chc", "Brewers": "mil",
    "Athletics": "oak", "Rangers": "tex"
}

def get_logo_path(team_name):
    code = team_logo_map.get(team_name)
    return f"assets/team_logos/{code}.png"

