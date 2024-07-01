# Cupid: Problem statement:
Music Recommendation

https://docs.google.com/document/d/1__2f3CkTv9IFDorpvQkGFaIGBqIXfPQF/edit


# Music Recommendation Application

## Project Structure
    cupid/
    ├── models/
    │ ├── __init__.py
    │ ├── song.py
    │ ├── user.py
    │ └── library.py
    └── main.py


## Models

### Song
- **Attributes:**
  - `name`
  - `genre`
  - `tempo`
  - `singer`
  - `popularity_score`
  - `release_year`
- **Method:**
  - `attributes()`: Returns a list of song attributes.

### User
- **Attributes:**
  - `name`
  - `playlist` (list of songs)
  - `friends` (list of friends)
- **Methods:**
  - `add_song_to_playlist(song)`: Adds a song to the user's playlist if not already present.
  - `add_friend(friend)`: Adds a friend to the user's friends list if not already present.

### MusicLibrary
- **Attributes:**
  - `songs` (dictionary of song names to Song objects)
  - `users` (dictionary of user names to User objects)
- **Methods:**
  - `add_song(song)`: Adds a song to the library if not already present.
  - `add_user(user)`: Adds a user to the library if not already present.
  - `add_friend(user_name, friend_name)`: Adds each user as a friend to the other if both users exist.
  - `get_song_by_name(song_name)`: Retrieves a song by its name.
  - `get_user_by_name(user_name)`: Retrieves a user by their name.
  - `recommend_songs(user_name)`: Recommends songs for a user based on the similarity index and friend similarity index, excluding songs already in the user's playlist.

## Similarity Calculation Functions

### calculate_similarity_index(song1, song2)
- Calculates the similarity index between two songs.
- Returns `0` if either song is `None`.

### calculate_friend_similarity_index(song, user)
- Calculates the friend similarity index for a song based on the user's friends' playlists.
- Returns `0` if the user has no friends.

## Running the Application

1. clone the project: `git clone git@github.com:pk026/cupid.git`
2. cd into project: `cd cupid`
3. run the main file with python: `python main.py`   (We do not need any extra setup here, if you have python installed on your machine it should work)

