import pytest
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

@pytest.fixture
def artist_fix():
    return [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]

"""
Test all() method 
so test returns all artists
"""

def test_get_all_artist(db_connection, artist_fix):
    db_connection.seed('seeds/record_store.sql')
    repository = ArtistRepository(db_connection)
    actual_list = repository.all()
    assert actual_list == artist_fix

"""
Test checks if create() can add 
new artist
"""
def test_adds_artist(db_connection, artist_fix):
    db_connection.seed('seeds/record_store.sql')
    repository = ArtistRepository(db_connection)

    new_artist = Artist(5, "Wild Nothing", "Indie")
    repository.create(new_artist)
    artist_fix.append(new_artist)

    assert repository.all() == artist_fix
