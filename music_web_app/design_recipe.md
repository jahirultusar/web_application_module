
#Plain Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE
# List all albums
GET /albums

# Create a new album
POST /albums
  title: string
  release_year: int
  artist_id: int

# List all artists
GET /artists

# Create a new artist
POST /artists
  name: string
  genre: string
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /albums
#  Expected response (200 OK):
"""
Returns all seeded albums <== need to create some!!
"""

# POST /albums
#  Parameters:
#    title: Voyage
#    release_year: 2022
#    artist_id: 2
#  Expected response (200 OK):
"""
Album created successfully
"""

# GET /artists
#  Expected response (200 OK):
"""
Pixies, ABBA, Taylor Swift, Nina Simone
"""

# POST /artists
#  Parameters:
#    name: Wild nothing
#    genre: Indie
#  Expected response (200 OK):
"" # (No content)

# GET /artists (after POST)
#  Expected response (200 OK):
"""
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
POST /albums
Test calls POST /albums route
and adds a new album to the list
and returns all albums
response 200
"""
def test_post_albums(web_client):
    response = web_client.post('/albums', data={
        'title': 'Voyage', 
        'release_year': 2022, 
        'artist_id': 2
    })
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album created successfully"

"""
GET /artists
  Expected response: 200 OK with initial artist list
"""
def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == [
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
    ]

"""
POST /artists
  Parameters: name=Wild nothing, genre=Indie
  Expected response: 200 OK (No content)
  Followed by GET /artists: updated list
"""
def test_post_artists_and_get_updated_list(web_client):
    post_response = web_client.post('/artists', data={
        'name': 'Wild nothing', 
        'genre': 'Indie'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]
```

