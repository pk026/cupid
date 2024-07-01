from .song import Song
from .user import User


class MusicLibrary:
    def __init__(self):
        self.songs = {}
        self.users = {}

    def add_song(self, song):
        if song.name not in self.songs:
            self.songs[song.name] = song

    def add_user(self, user):
        if user.name not in self.users:
            self.users[user.name] = user

    def add_friend(self, user_name, friend_name):
        user = self.users.get(user_name)
        friend = self.users.get(friend_name)
        if user and friend:
            user.add_friend(friend)
            friend.add_friend(user)

    def get_song_by_name(self, song_name):
        return self.songs.get(song_name)

    def get_user_by_name(self, user_name):
        return self.users.get(user_name)

    def recommend_songs(self, user_name):
        user = self.get_user_by_name(user_name)
        if not user:
            return []

        recommendations = []
        user_playlist = set(user.playlist)
        
        for song_name, song in self.songs.items():
            if song not in user_playlist:
                max_similarity_index = 0
                if user.playlist:
                    max_similarity_index = max(calculate_similarity_index(song, playlist_song) for playlist_song in user.playlist)
                friend_similarity_index = calculate_friend_similarity_index(song, user)
                recommendations.append((song, max_similarity_index, friend_similarity_index))

        recommendations.sort(key=lambda x: (-x[1], -x[2]))
        return [song.name for song, _, _ in recommendations]


def calculate_similarity_index(song1, song2):
    if not song1 or not song2:
        return 0
    attributes1 = song1.attributes()
    attributes2 = song2.attributes()
    same_attributes = sum(1 for a, b in zip(attributes1, attributes2) if a == b)
    total_attributes = len(attributes1)
    return same_attributes / total_attributes

def calculate_friend_similarity_index(song, user):
    if not user.friends:
        return 0
    friends_with_song = sum(1 for friend in user.friends if song in friend.playlist)
    total_friends = len(user.friends)
    return friends_with_song / total_friends
