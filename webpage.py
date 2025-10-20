import streamlit as st
import pandas as pd
import numpy as np
import joblib

directory = "./data/imdb-top-rated-movies-user-rated.csv"
df = pd.read_csv(directory)

model_dir = "./models/pipeline.joblib"
model = joblib.load(model_dir)

df_tags = df.copy()
df_tags["Tags"] = df_tags["Tags"].astype(str).map(lambda x:x.split(", "))
df_writers = df.copy()
df_writers["Writers"] = df_writers["Writers"].astype(str).map(lambda x:x.split(", "))

directors = df['Director'].unique()
tags = df_tags.explode('Tags')['Tags'].map(lambda x:x.strip('"')).unique()
writers = df_writers.explode('Writers')['Writers'].map(lambda x:x.strip('"')).unique()

st.markdown("# IMDb Rating Predictor")

chosen_votes = st.select_slider('select no. of votes',np.arange(0,20001))
chosen_critics = st.select_slider('select critics',np.arange(0,101))
chosen_director = st.selectbox('choose director',options=directors)
chosen_genre = st.multiselect('choose genre',options=tags,max_selections=5)
chosen_writer = st.multiselect('choose writer',options=writers,max_selections=5)

sample = pd.DataFrame({
    'Votes':[chosen_votes],
    'Meta Score':[chosen_critics],
    'Director':[chosen_director],
    'Tags':[chosen_genre],
    'Writers':[chosen_writer],
})

if st.button("predict"):
    prediction = model.predict(sample)[0]
    st.write("Predicted IMDb rating")

    st.write(round(prediction,1))




