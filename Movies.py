import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Movie Page", page_icon="🎥")

page_bg_img = f"""
<style>
.stApp {{
    background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSW2YKonS1OsF2Akc6mskXxlJCKihUL7ihVPQ&s");
    background-attachment: fixed;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Block if not logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login to continue.")
    st.button("Login", on_click=lambda: st.session_state.clear())
    st.session_state.logged_in = False
    st.stop()

st.title("🎬 Welcome to Movie Recommender")
st.subheader(f"Hello, {st.session_state.user} 👋")

load_dotenv()

# Fetch poster image
def fetch_poster(movie_id):
    api_key = os.getenv("TMDB_API_KEY")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    try:
        data = requests.get(url)
        data.raise_for_status()
        data = data.json()

        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie {movie_id}: {e}")
        return None

# Recommend movies based on similarity
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)
        if poster:
            recommended_movie_posters.append(poster)
        else:
            recommended_movie_posters.append("https://via.placeholder.com/500x750.png?text=No+Poster+Available")
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Load pickled data
movies = pickle.load(open("L:\\project_ML\\movie_list.pkl", 'rb'))
similarity = pickle.load(open("L:\\project_ML\\similarity.pkl", 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            movie_name = recommended_movie_names[idx]
            st.text(movie_name)
            st.image(recommended_movie_posters[idx])

            search_links = {
                "FilmyWap": f"https://www.google.com/search?q={movie_name.replace(' ', '+')}+FilmyWap",
                "KatMovieHD": f"https://www.google.com/search?q={movie_name.replace(' ', '+')}+KatMovieHD",
                "Bolly4U": f"https://www.google.com/search?q={movie_name.replace(' ', '+')}+Bolly4U",
                "JioCinema": f"https://www.google.com/search?q={movie_name.replace(' ', '+')}+JioCinema"
            }

            for site, url in search_links.items():
                st.markdown(f"[🔗 {site}]({url})", unsafe_allow_html=True)

# Logout
if st.button("Logout"):
    st.session_state.clear()
    st.success("Logged out successfully.")
    st.switch_page("login.py")
