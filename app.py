import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
   url = "https://api.themoviedb.org/3/movie/{}?api_key=3f69e24e0b4926173eb57d0a7480b9d8&language=en-US".format(movie_id)
   dataset = requests.get(url)
   dataset = dataset.json()
   poster_path = dataset['poster_path']
   full_path = "https://image.tmdb.org/t/p/w500" + poster_path
   
   return full_path


def recommend(movie):
  index = moviess[moviess['title'] == movie].index[0]
  distances = sorted(list(enumerate(similarity[index])), reverse=True, key = lambda x: x[1])
  recommended_movies_name = []
  recommended_movies_poster = []
  for i in distances[1:7]:
     movie_id = moviess.iloc[i[0]].movie_id
     recommended_movies_poster.append(fetch_poster(movie_id))
     recommended_movies_name.append(moviess.iloc[i[0]].title)
  return recommended_movies_name, recommended_movies_poster

st.header("Movie Recoomendation Syetem using Machine Learning")
moviess = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarit.pkl', 'rb'))

movie_list = moviess['title'].values
selected_movie = st.selectbox(
    'type or select a movies to get recommended',
    movie_list
)

if st.button('shows Recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
       st.text(recommended_movies_name[0])
       st.image(recommended_movies_poster[0])

    with col2:
       st.text(recommended_movies_name[1])
       st.image(recommended_movies_poster[1])

    with col3:
       st.text(recommended_movies_name[2])
       st.image(recommended_movies_poster[2])
    
    with col4:
       st.text(recommended_movies_name[3])
       st.image(recommended_movies_poster[3])

    with col5:
       st.text(recommended_movies_name[4])
       st.image(recommended_movies_poster[4])

    with col6:
       st.text(recommended_movies_name[5])
       st.image(recommended_movies_poster[5])

    