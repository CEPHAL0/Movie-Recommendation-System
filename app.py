import streamlit as st
import pickle
import pandas as pd

movies_list = pickle.load(open('assets/movie_dict.pkl', 'rb'))
movies_df = pd.DataFrame(movies_list)
movies_list = movies_df['title'].values
similarity = pickle.load(open('assets/similarity.pkl', 'rb'))
movpre = pickle.load(open('assets/movpre.pkl', 'rb'))

# Function to recommend movie


def recommend(movie: str):
    if movies_df[movies_df['title'] == movie].empty:
        print(f"{movie} not present in the database")
    else:
        movie_index = movies_df[movies_df['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)),
                             reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = []
        movie_id = []
        for i in movies_list:
            movie_id = i[0]
            recommended_movies.append(movpre.iloc[i[0]].title)

        print(movie_id)
        return recommended_movies


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie that you like or finished watching', movies_list)

button = st.button("Recommend")
if button:
    st.text("TOP PICKS FOR YOU:")
    recommendations = recommend(selected_movie_name)
    for recommendation in recommendations:
        st.write(recommendation)
else:
    st.write("")
recommend("Avatar")
