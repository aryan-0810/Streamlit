import streamlit as st

st.title("Instagram Like Counter")

if "likes" not in st.session_state:
    st.session_state.likes = 0

if st.button("Like"):
    st.session_state.likes += 1

st.write(f"Likes: {st.session_state.likes}")

import streamlit as st

st.title("Playlist Creator")

playlist_name = st.sidebar.text_input("Playlist Name")
number_of_songs = st.sidebar.number_input("Number of Songs", min_value=1, max_value=100, value=10)
genre = st.sidebar.selectbox("Music Genre", ["Pop", "Rock", "Hip-Hop", "Classical"])

if st.sidebar.button("Create Playlist"):
    st.subheader("Your Playlist")
    st.write("Playlist Name:", playlist_name)
    st.write("Number of Songs:", number_of_songs)
    st.write("Music Genre:", genre)

    