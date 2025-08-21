import streamlit as st
from utils.team_map import get_logo_path

def render_game_card(row):
    home_team, away_team = row["game"].split(" @ ")

    with st.container():
        st.markdown(f"### {row['game']} — {row['time']}")
        st.markdown(f"🌤️ **Weather**: {row['weather']}, Wind: {row['wind_mph']} mph")

        # Logos and team names
        col_logo, col_info = st.columns([1, 5])
        with col_logo:
            st.image(get_logo_path(home_team.strip()), width=60)
            st.image(get_logo_path(away_team.strip()), width=60)
        with col_info:
            st.markdown(f"**Home ML**: {row['ml_home']}  |  **Away ML**: {row['ml_away']}")
            st.markdown(f"**O/U**: {row['over_under']}")

        # Pitching Matchup
        st.markdown("#### 🧱 Pitching Matchup")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**{row['pitcher_home']}**")
            st.write(row['stats_home'])
        with col2:
            st.markdown(f"**{row['pitcher_away']}**")
            st.write(row['stats_away'])

        # Team Trends
        st.markdown("#### 📊 Team Trends")
        col3, col4 = st.columns(2)
        with col3:
            st.markdown(f"**{home_team}**")
            st.write(row['team_home_stats'])
        with col4:
            st.markdown(f"**{away_team}**")
            st.write(row['team_away_stats'])

        # Player Spotlight
        st.markdown("#### 🔥 Player Spotlight")
        st.write(row['player_trend'])

        # Betting Insights
        st.markdown("#### 💰 Betting Insights")
        st.write(f"**Pick to Win**: {row['pick_to_win']}")
        st.write(f"**O/U Model**: {row['ou_model']}")
        st.write(f"**Best Bet**: {row['best_bet']}")
        st.write(f"**Extra Prop**: {row['extra_prop']}")

