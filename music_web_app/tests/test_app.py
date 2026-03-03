import pytest 

@pytest.fixture
def album_fix():
    return "\n".join([
        "Album(1, Doolittle, 1989, 1)",
        "Album(2, Surfer Rosa, 1988, 1)",
        "Album(3, Waterloo, 1974, 2)",
        "Album(4, Super Trouper, 1980, 2)",
        "Album(5, Bossanova, 1990, 1)",
        "Album(6, Lover, 2019, 3)",
        "Album(7, Folklore, 2020, 3)",
        "Album(8, I Put a Spell on You, 1965, 4)",
        "Album(9, Baltimore, 1978, 4)",
        "Album(10, Here Comes the Sun, 1971, 4)",
        "Album(11, Fodder on My Wings, 1982, 4)",
        "Album(12, Ring Ring, 1973, 2)"
    ]) + "\n"

@pytest.fixture
def artist_fix():
    return "\n".join([
        "Artist(1, Pixies, Rock)",
        "Artist(2, ABBA, Pop)",
        "Artist(3, Taylor Swift, Pop)",
        "Artist(4, Nina Simone, Jazz)"
    ]) + "\n"



"""
Test calls GET /albums route
and returns all albums
"""
def test_calls_get_all_albums_route(db_connection, web_client, album_fix):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == album_fix

"""
Test calls POST /albums route
and adds a new album to the list
and returns all albums
"""
def test_calls_post_albums_route(db_connection, web_client, album_fix):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.post('/albums', data={
        "title": "Voyage",
        "release_year": "2022",
        "artist_id": "2"
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "New Album added successfully!"

    response = web_client.get('/albums')
    assert response.status_code == 200
    expected_output = album_fix + "Album(13, Voyage, 2022, 2)\n"
    
    assert response.data.decode('utf-8') == expected_output


"""
GET /artists
  Expected response: 200 OK with initial artist list
"""
def test_get_artists(web_client, artist_fix):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == artist_fix

"""
POST /artists
  Parameters: name=Wild Nothing, genre=Indie
  Expected response: 200 OK (No content)
  Followed by GET /artists: updated list
# """
def test_post_artists_and_get_updated_list(web_client, artist_fix):
    post_response = web_client.post('/artists', data={
        'name': 'Wild Nothing', 
        'genre': 'Indie'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == "New Artist added successfully!"

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200

    expected_output = artist_fix + "Artist(5, Wild Nothing, Indie)\n"
    assert get_response.data.decode("utf-8") == expected_output
