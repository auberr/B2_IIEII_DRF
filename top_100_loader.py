import json

with open('top100.json', 'r', encoding='UTF-8') as f:
    top_100 = json.load(f)

print(top_100)

new_list = []
for song in top_100:
    songs = {"model": "musicplaylist.music"}
    songs["fields"] = {}
    songs["fields"] = song
    new_list.append(songs)

with open('top100_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)

