import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Kindergarten Cop", "year": 1990},
# ]
# data = json.dumps(movies)
# print(data)
# path = Path("movies.json")
# path.write_text(data)
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])
