import pytest
from lib.album_repository import AlbumRepository
from lib.album import Album


@pytest.fixture
def albums_fix():
    return [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2)
    ]

"""
Test all() method which returns
a list of albums from seed data
"""
def test_all_method_should_return_list_of_albums(db_connection, albums_fix):
    db_connection.seed('seeds/record_store.sql')
    repository = AlbumRepository(db_connection)
    actual_albums = repository.all()
    assert actual_albums == albums_fix


"""
Test create() method which adds a new album
"""
def test_create_method_adds_new_album(db_connection, albums_fix):
    db_connection.seed('seeds/record_store.sql')
    repository = AlbumRepository(db_connection)
    new_album = Album(13, "Voyage", 2022, 2)
    repository.create(new_album)
    albums_fix.append(new_album)

    assert repository.all() == albums_fix

