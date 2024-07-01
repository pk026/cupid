class User:
    def __init__(self, name):
        self.name = name
        self.playlist = []
        self.friends = []

    def add_song_to_playlist(self, song):
        if song not in self.playlist:
            self.playlist.append(song)

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)