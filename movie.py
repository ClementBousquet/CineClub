import os
import json

CURRENT_DIRECTORY = os.path.dirname(__file__)
DATA_FILE = os.path.join(CURRENT_DIRECTORY,"data","movies.json")

class Movie:
    
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title
  
    def _get_movies(self):
        with open(DATA_FILE,"r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE,"w") as f:
            json.dump(movies, f, indent=4)