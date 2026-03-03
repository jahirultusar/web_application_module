from lib.artist import Artist

"""
Test constructs artist
"""
def test_initialises_artist_modal():
    artist = Artist(1, 'Test Name', 'Test Genre')
    assert artist.id == 1
    assert artist.name == 'Test Name'
    assert artist.genre == 'Test Genre'

"""
Test checks equal objects with __eq__()
"""
def test_checks_equal_objects():
    artist_1 = Artist(1, 'Test Name', 'Test Genre')
    artist_2 = Artist(1, 'Test Name', 'Test Genre')

    assert artist_1 == artist_2

"""
Test returns stringify object with __repr__()
"""
def test_stringify_object():
    artist = Artist(1, 'Test Name', 'Test Genre')

    assert str(artist) == "Artist(1, Test Name, Test Genre)"