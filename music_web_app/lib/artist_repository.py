from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        """Initialises db connection"""
        self._connection = connection

    def all(self):
        """Returns all artist from table"""
        rows = self._connection.execute('SELECT * FROM artists')
        artist_list = []
        for row in rows:
            item = Artist(row['id'], row['name'], row['genre'])
            artist_list.append(item)
        return artist_list

    def create(self, artist):
        """Creates a new artist"""
        rows = self._connection.execute(
            'INSERT INTO artists (name, genre) VALUES (%s, %s)',
            [artist.name, artist.genre]
        )
        return None
