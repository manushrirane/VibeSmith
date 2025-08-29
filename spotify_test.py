from agent import track_search

# manual test of the track_search function

query = "gracie abrams"
tracks = track_search(query, limit=5)

print(f"Top {len(tracks)} tracks for: '{query}'\n")

for index, song in enumerate(tracks, start=1):
    print(f"{index}. {song['name']} by {song['artist']} (Album: {song['album']})")
    print(f"Listen here: {song['url']}\n")
