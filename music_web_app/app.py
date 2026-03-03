import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.artist import Artist


# Create a new Flask app
app = Flask(__name__)

# List of Albums route 
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    response = ''
    for album in albums:
        response += f"{album}\n"
    return response

# Can add New Album in database
@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    new_album = Album(None, title, release_year, artist_id) 

    repository.create(new_album)
    return f"New Album added successfully!"

# List of Artists route 
@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    response = ''
    for artist in artists:
        response += f"{artist}\n"
    return response

# Can add New Artist in database 
@app.route('/artists', methods=['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    name = request.form['name']
    genre = request.form['genre']

    new_artist = Artist(None, name, genre) 

    repository.create(new_artist)
    return f"New Artist added successfully!"

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

