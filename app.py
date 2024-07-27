import streamlit as st
import pandas as pd
import pickle
import requests

st.title("Movie Recommendation System")
with open('final_movies.pkl','rb') as file:
    movies_df=pickle.load(file)
with open('movie_similarities.pkl','rb') as file:
    similarities=pickle.load(file)

movie_name = st.selectbox(
    "Search any movie to view recommendations.",
    movies_df['title'],
)
def fetch_poster(id):
    response=requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']



def recommend(movie_name):
    movie_index=movies_df[movies_df['title']==movie_name].index[0]
    movies_list=sorted(enumerate(similarities[movie_index]),reverse=True,key=lambda x:x[1])[1:6]
    movie_ids=[]
    movie_names=[]
    for i in movies_list:
        movie_ids.append(movies_df.iloc[i[0]].movie_id)
        movie_names.append(movies_df.iloc[i[0]].title)
    return movie_ids,movie_names

if st.button('Recommend'):
    movie_ids,movie_names=recommend(movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.write(movie_names[0])
        st.image(fetch_poster(movie_ids[0]))

    with col2:
        st.write(movie_names[1])
        st.image(fetch_poster(movie_ids[1]))

    with col3:
        st.write(movie_names[2])
        st.image(fetch_poster(movie_ids[2]))
    col1, col2, col3 = st.columns(3)

    with col4:
        st.write(movie_names[3])
        st.image(fetch_poster(movie_ids[3]))

    with col5:
        st.write(movie_names[4])
        st.image(fetch_poster(movie_ids[4]))
