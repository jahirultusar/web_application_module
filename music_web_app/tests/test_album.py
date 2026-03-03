from lib.album import Album

"""
Test checks Album object constructors
"""
def test_album_constructs():
    album = Album(1, "Test Title", 1000, 1)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 1000
    assert album.artist_id == 1

"""
Test makes Album objects equal with __e1
q__
"""
def test_makes_album_object_equal():
    album = Album(1, "Test Title", 1000, 1)
    album2 = Album(1, "Test Title", 1000, 1)
    assert album == album2

"""
Test presents the object stringyfied with __repr__
"""
def test_presents_stringify():
    album = Album(1, "Test Title", 1000, 1)
    assert str(album) == "Album(1, Test Title, 1000, 1)"