import streamlit as st
from datetime import datetime
from utils.load_data import load_daily_csv
from utils.format_card import render_game_card

# Set page config
st.set_page_config(page_title="Daily MLB Insights", layout="wide")

# Inject chalkboard CSS
with open("styles/chalkboard.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page title
st.title("📰 Daily MLB Betting Insights")
st.markdown("Curated by Tyler | Updated Daily")

# Load today's CSV
today = datetime.today().strftime("%Y%m%d")
try:
    df = load_daily_csv(today)
except FileNotFoundError:
    st.error(f"No data found for {today}. Please run generate_csv.py.")
    st.stop()

# Render each game card
for _, row in df.iterrows():
    render_game_card(row)
    st.markdown("---")

