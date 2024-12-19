from lib.recipe import Recipe
class RecipeRepository():

    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute("SELECT * FROM recipes")
        return [Recipe(
            row["id"], 
            row["name"], 
            row["cooking_time"], 
            row["rating"]) 
            for row in rows
            ]
    
    def find(self, name):
        rows = self.connection.execute("SELECT * FROM recipes WHERE name = %s", [name])
        row = rows[0]
        return Recipe(row["id"], row["name"], row["cooking_time"], row["rating"])
        