
#Plain Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Album route
POST /album

# Submit message route
POST /submit
  name: string
  message: string
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
This is my album page!
"""

# POST /albums
#  Expected response (200 OK):
"""
POST data to album
"""

# POST /albums
#  Parameters:
#    name: title
#    release_year: year/int
#  Expected response (200 OK):
"""
POST data to album
"""

# GET /artists
#  Expected response (200 OK):
"""
Returns: Pixies, ABBA, Taylor Swift, Nina Simone
"""

# POST /artists
# Expected response (200 OK):

# POST /artists
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Provides the artist names
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /albums
  Expected response (200 OK):
  "This is the albums page!"
"""
def test_post_albums(web_client):
    response = web_client.get('/albums', data={'title': 'voyage', 'release_year': 2022, 'artist_id': 2})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Book(1, Invisible Cities, Italo Calvino)",
        "Book(2, The Man Who Was Thursday, GK Chesterton)",
        "Book(3, Bluets, Maggie Nelson)",
        "Book(4, No Place on Earth, Christa Wolf)",
        "Book(5, Nevada, Imogen Binnie)"
    ])

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

