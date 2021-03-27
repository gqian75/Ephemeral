import requests
import json
import base64
from urllib.parse import urlencode

class SpotifyAPI(object):
    access_token = None
    client_id = None
    client_secret = None

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token_data(self):
        client_id = self.client_id
        client_secret = self.client_secret
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())

        token_url = "https://accounts.spotify.com/api/token"
        method = "POST"
        token_data = {
            "grant_type": "client_credentials"
        }
        token_headers = {
            "Authorization" : f"Basic {client_creds_b64.decode()}"
        }
        r = requests.post(token_url, data=token_data, headers=token_headers)
        token_response_data = r.json()
        self.access_token = token_response_data['access_token']
        expires = token_response_data['expires_in'] #seconds
        type = token_response_data["token_type"]

    def search(self, q, search_type, search_limit): # valid search types: "album", "artist", "playlist", "show", "episode"
        access_token = self.access_token
        headers = {
            "Authorization" : f"Bearer {access_token}"
        }
        endpoint = "https://api.spotify.com/v1/search"
        data = urlencode({"q": q, "type": search_type, "limit": search_limit})
        lookup_url = f"{endpoint}?{data}"
        r = requests.get(lookup_url, headers=headers)

        text_file = open("json.txt","w") # json information on json.txt
        text_file.write(str(r.json()))
        text_file.close()

        json = r.json()
        data = []
        if (search_type=="track"):

            items = json["tracks"]["items"]

            for i in items:
                name = i["name"]
                length = i["duration_ms"]
                album = i["album"]["name"]
                release_date = i["album"]["release_date"]
                artist = i["artists"][0]["name"]

                track = { name: {
                    "name": name,
                    "artist": artist,
                    "album": album,
                    "release": release_date,
                    "length": length
                    }
                }
                data.append(track)

        elif (search_type=="artist"):
            items = json["artists"]["items"]
            for i in items:
                name = i["name"]
                followers = i["followers"]["total"]
                genre = i["genres"] #array of str
                images = i["images"] #[{"url"}]
                popularity = i["popularity"]

                artist = { name: {
                    "name": name,
                    "Genre": genre,
                    }
                }
                data.append(artist)

        elif (search_type=="album"):
            items = json["albums"]["items"]
            for i in items:
                name = i["name"]
                release = i["release_date"]
                tracks = i["total_tracks"]
                artist = i["artists"][0]["name"]
                type = i["type"]
                # genre

                album = { name: {
                    "name":name,
                    "release":release,
                    "artist":artist,
                    "type":type,
                    "tracks":tracks
                    }
                }
                data.append(album)

        return data



client_id = "123d71c67be54fbeb90cc8dda4a451a6"
client_secret = "a8f77509182b4dae9ce0a9caa3ec674e"
spotify = SpotifyAPI(client_id,client_secret)
spotify.get_token_data()
access_token = spotify.access_token

#print(spotify.search("drivers license","track","1"))
#print(spotify.search("olivia rodrigo","artist","1"))
#print(spotify.search("bleeding","album","1"))
