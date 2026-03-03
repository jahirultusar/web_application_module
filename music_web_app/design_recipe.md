_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

```
Your test should assert that the new album is present in the list of records returned by GET /albums (you will also need to test drive this route!).

```
Nouns:

album, title, release_year, artist, id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| album                 | title, release year, artist_id, id |

Name of the table (always plural): `albums`

Column names: `id`, `title`, `release_year, artist_id`, 

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, column names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```
############################################################################

#Plain Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Album route
POST /albums
title: string
release_year: number(str)
artist_id: number(str)
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# POST /albums
#    title: Hyperspace Sunrise
#    release_year: 2038
#    artist_id: 1
#  Expected response (200 OK):
"""
No Content Returns
"""

# GET /albums
#  Expected response (200 OK):
"""
Returns:
Albums(1, 'Hyperspace Sunset', 2035, 1)
Albums(2, 'Hyperspace Sunrise', 2038, 1)
"""

# POST /albums
# Expected response (400 Bad Request):
"""
You need to Submit a title, realease year and title
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

