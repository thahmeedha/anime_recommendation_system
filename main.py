#----------------------------------------LIBRARY------------------------------------------------------------------------
import numpy as np
import pandas as pd
import difflib
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#----------------------------------------LOAD DATASET-------------------------------------------------------------------
df = pd.read_csv('anime_datas.csv')

#-----------------------------------------CLEAN DATASET-----------------------------------------------------------------
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df = df.replace(r'\s+', ' ', regex=True)
df.columns = df.columns.str.strip()

#----------------------------------------FILL MISSING VALUES------------------------------------------------------------
filter_data = ["Name", "English name", "Genres", "Synopsis", "Type", "Studios", "Source"]
for i in filter_data:
    df[i] = df[i].fillna('')

#----------------------------------------COMBINE TEXT-------------------------------------------------------------------
combined_data = (
    df["Name"] + " " +
    df["English name"] + " " +
    df["Genres"] + " " +
    df["Synopsis"] + " " +
    df["Type"] + " " +
    df["Studios"] + " " +
    df["Source"]
)

#----------------------------------------VECTORIZE----------------------------------------------------------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(combined_data)

#----------------------------------------RECOMMEND FUNCTION-------------------------------------------------------------
def recommend(index):
    sim_scores = cosine_similarity(tfidf_matrix[index], tfidf_matrix)
    return sim_scores.flatten()

#----------------------------------------STREAMLIT UI-------------------------------------------------------------------

anime_name = st.text_input("Enter your anime name:")

if anime_name:
    list_of_all_title = df['Name'].tolist()
    find_closest_match = difflib.get_close_matches(anime_name, list_of_all_title)

    if find_closest_match:
        close_match = find_closest_match[0]

        idx_list = df[df['Name'] == close_match].index
        if len(idx_list) == 0:
            st.write("Anime not found in dataset")
        else:
            idx = idx_list[0]

            sim_scores = recommend(idx)
            get_score = list(enumerate(sim_scores))
            sorted_anime = sorted(get_score, key=lambda x: x[1], reverse=True)

            st.title("Anime Recommendations")

            i = 1
            for a in sorted_anime:
                if i >= 11:
                    break

                index = a[0]
                anime_list = df.iloc[index]["Name"]
                image_url = df.iloc[index]["Image URL"]

                st.write(f"{i}) {anime_list}")
                st.image(image_url)

                i += 1
    else:
        st.write("No anime found")