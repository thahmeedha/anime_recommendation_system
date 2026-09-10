# Anime Recommendation System

This project is a machine learning-based application that recommends similar anime based on user input using natural language processing techniques.

---

## Project Overview

The goal of this project is to build a content-based anime recommendation system that suggests similar anime based on textual features such as name, genre, synopsis, type, studio, and source.

The system uses TF-IDF vectorization and cosine similarity to measure relationships between anime titles and recommend the most relevant results.

---

## Dataset Used

The dataset (`anime_datas.csv`) contains detailed anime information including:

* Name
* English Name
* Genres
* Synopsis
* Type
* Studios
* Source
* Image URL

This dataset allows the model to understand both textual and metadata-based similarities between anime.

---

## Data Preprocessing

* Removed leading and trailing spaces from text data
* Cleaned extra whitespace using regex
* Standardized column names
* Handled missing values by replacing them with empty strings

---

## Feature Engineering

* Combined multiple text features into a single string:
  * Name
  * English Name
  * Genres
  * Synopsis
  * Type
  * Studios
  * Source

* Converted text data into numerical vectors using TF-IDF Vectorization
* Represented each anime as a high-dimensional feature vector

---

## Similarity Method

* Cosine Similarity is used to measure similarity between anime vectors
* The model calculates how close each anime is to the selected title
* Higher similarity score indicates stronger recommendation relevance

---

## Recommendation System

The system works as follows:

* User enters an anime name
* The system finds the closest matching title using fuzzy matching
* TF-IDF vectors are used to compute similarity scores
* Top 10 most similar anime are displayed

---

## Web Application

The application is built using Streamlit.

Features:

* Accepts anime name as input
* Finds closest matching title automatically
* Displays recommended anime list
* Shows anime images along with titles

---

## Project Structure
```
anime-recommendation-system/
│
├── main.py
├── anime_datas.csv
├── requirements.txt
├── README.md
```

---

## How to Run
```
pip install -r requirements.txt
streamlit run main.py
```

---

## Key Learnings

* Understanding content-based recommendation systems
* Working with TF-IDF vectorization
* Using cosine similarity for similarity scoring
* Handling real-world messy datasets
* Building an end-to-end ML web application using Streamlit

---

## Future Improvements

* Improve recommendation accuracy using hybrid filtering methods
* Add genre-based filtering options
* Optimize performance for large datasets
* Deploy the application publicly using Streamlit Cloud or similar platforms

---

## Author

This project was developed to explore content-based recommendation systems and to build a complete machine learning pipeline from data preprocessing to deployment.

## PR Test
This change was made on the test-pr branch.
