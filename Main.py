import streamlit as st
import pandas as pd

# Load the preprocessed anime data
file_path = 'data/anime_1.csv'  # Adjust the file path if needed
anime_data = pd.read_csv(file_path)

# Clean up and select relevant columns (Name, Genres, Score)
anime_data = anime_data[['Name', 'Genres', 'Score']].dropna()

# Convert 'Genres' into a list of genres
anime_data['Genres'] = anime_data['Genres'].apply(lambda x: x.split(', '))

# Streamlit app title
st.title("Anime Recommendation System")

# Add a section for searching anime by name
st.subheader("Search for Anime")

# Create a search bar with dropdown
anime_list = anime_data['Name'].tolist()
selected_anime = st.selectbox("Select or search for an anime:", anime_list)

# Get the genres of the selected anime
selected_anime_genres = anime_data[anime_data['Name'] == selected_anime]['Genres'].values[0]

# Display the genres of the selected anime
st.write(f"Genres for {selected_anime}: {', '.join(selected_anime_genres)}")

# Add a slider to switch between the available genres of the selected anime
genre_index = st.slider(f"Select a genre to get recommendations for {selected_anime}:",
                        min_value=0, max_value=len(selected_anime_genres) - 1, value=0)

# Get the currently selected genre from the slider
selected_genre = selected_anime_genres[genre_index]

st.write(f"Recommendations based on the genre: {selected_genre}")

# Filter anime by the selected genre
similar_anime = anime_data[anime_data['Genres'].apply(lambda genres: selected_genre in genres)]

# Display recommendations based on the selected genre
st.dataframe(similar_anime[['Name', 'Score']].drop_duplicates())
