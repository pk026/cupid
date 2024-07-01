from models.song import Song
from models.user import User
from models.library import MusicLibrary


def main():
    # Create library
    library = MusicLibrary()

    # Add songs
    song1 = Song("Song1", "Pop", "Fast", "Singer1", 80, 2020)
    song2 = Song("Song2", "Rock", "Medium", "Singer2", 70, 2018)
    song3 = Song("Song3", "Jazz", "Slow", "Singer3", 60, 2019)
    song4 = Song("Song4", "Pop", "Fast", "Singer1", 90, 2021)
    song5 = Song("Song5", "Rock", "Medium", "Singer4", 50, 2017)

    library.add_song(song1)
    library.add_song(song2)
    library.add_song(song3)
    library.add_song(song4)
    library.add_song(song5)

    # Add users
    user1 = User("User1")
    user2 = User("User2")
    user3 = User("User3")

    library.add_user(user1)
    library.add_user(user2)
    library.add_user(user3)

    # Add songs to user playlists
    user1.add_song_to_playlist(song1)
    user1.add_song_to_playlist(song2)

    user2.add_song_to_playlist(song2)
    user2.add_song_to_playlist(song3)

    user3.add_song_to_playlist(song1)
    user3.add_song_to_playlist(song4)

    # Add friends
    library.add_friend("User1", "User2")
    library.add_friend("User1", "User3")

    # Show recommendations
    recommendations = library.recommend_songs("User1")
    print("Recommendations for User1:", recommendations)

if __name__ == "__main__":
    main()
