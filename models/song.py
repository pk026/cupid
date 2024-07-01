class Song:
    def __init__(self, name, genre, tempo, singer, popularity_score, release_year):
        self.name = name
        self.genre = genre
        self.tempo = tempo
        self.singer = singer
        self.popularity_score = popularity_score
        self.release_year = release_year
    
    def attributes(self):
        return [self.genre, self.tempo, self.singer, self.popularity_score, self.release_year]

    def __str__(self):
        return f"{self.name}"
