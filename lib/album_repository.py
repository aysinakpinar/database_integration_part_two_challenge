from lib.album import Album

class AlbumRepository:

    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        return [
            Album(row["id"], row["title"], row["release_year"], row["artist_id"]) 
            for row in rows
            ]
    
    def find(self, title):
        rows = self._connection.execute("SELECT * FROM albums WHERE title = %s", [title])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])