from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.recipe_repository import RecipeRepository



# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

album_repository = AlbumRepository(connection)
albums = album_repository.all()

for album in albums:
    print(album)

print(album_repository.find('Ring Ring'))

recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()

for recipe in recipes:
    print(recipe)

print(recipe_repository.find('Dolma'))