import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
from glob import glob
from pathlib import Path


st.set_page_config(layout="wide")
st.header("Diary Tone")
st.subheader("Positivity")

analyzer = SentimentIntensityAnalyzer()
filepaths = glob("diary/*.txt")
mood = {}

for filepath in filepaths:
    date_string = Path(filepath).stem
    with open(filepath, "r") as file:
        diary = file.read()

    scores = analyzer.polarity_scores(diary)
    mood[date_string] = (scores["pos"], scores["neg"])

print(mood)

