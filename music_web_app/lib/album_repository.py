from lib.album import Album

class AlbumRepository:
    """Initialises the database connection"""
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        """Returns all albums"""
        rows = self._connection.execute('SELECT * FROM albums')
        album_list = []
        for row in rows:
            item = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            album_list.append(item)
        return album_list
    
    def create(self, album):
            rows = self._connection.execute(
                'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)',
                [album.title, album.release_year, album.artist_id]    
            )
            return None
        