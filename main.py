import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
from glob import glob
from pathlib import Path
import plotly.express as px


# Set page config
st.set_page_config(layout="wide")
# Add header
st.header("Diary Tone")

# Initialize SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Get the diaries
filepaths = glob("diary/*.txt")
# Sort the diaries in order
filepaths = sorted(filepaths)

# Lists for dates, positivity and negativity scores
dates = []
pos = []
neg = []

# Iterate through each diary
for filepath in filepaths:
    # Get the date of each diary
    date_string = Path(filepath).stem
    # Read the diary
    with open(filepath, "r") as file:
        diary = file.read()

    # Get the sentiment scores
    scores = analyzer.polarity_scores(diary)

    # Store date, positivity and negativity scores
    dates.append(date_string)
    pos.append(scores["pos"])
    neg.append(scores["neg"])

# Add the positivity subheader
st.subheader("Positivity")
# Plot the chart
figure1 = px.line(x=dates, y=pos, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure1)

# Add the negativity subheader
st.subheader("Negativity")
# Plot the chart
figure2 = px.line(x=dates, y=neg, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure2)

