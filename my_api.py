import requests, json
from datetime import date

querystring = {"date":date.today().strftime("%Y-%m-%d")}
headers = {
    'x-rapidapi-key': "cdec391e94msh59bba6e6cb20d6dp148a7bjsn7a9048b31414",
    'x-rapidapi-host': "billboard2.p.rapidapi.com"
    }
headers_audioDB = {
    'x-rapidapi-key': "cdec391e94msh59bba6e6cb20d6dp148a7bjsn7a9048b31414",
    'x-rapidapi-host': "theaudiodb.p.rapidapi.com"
    }

CLIENT_ID = "852c80dddc2242c690fd514762d73d86"
CLIENT_SECRET = "dcd5f80d6deb4215a996e1a0719c64a2"
AUTH_URL = 'https://accounts.spotify.com/api/token'
SEARCH_URL = "https://api.spotify.com/v1/search"
ART_URL = "https://api.spotify.com/v1/artists"
auth_response = requests.post(AUTH_URL, {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET,})
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headers_spotify = {'Authorization': 'Bearer {token}'.format(token=access_token)}

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
        json = r.json()
        albums=json["tracks"]["items"][0]["album"]["name"]
        return albums

def songAPI():
    url = "https://billboard2.p.rapidapi.com/hot_100"
    res = requests.request("GET", url, headers=headers, params=querystring)
    res = res.json()

    songs = []

    for song in res:
        if "&#039;" in song["title"]:
            temp = song["title"].split("&#039;")
            song["title"] = temp[0] + "'" + temp[1]
        name = song["credited_artists"][0]["artist_name"]
        if "&#039;" in name:
            temp = name.split("&#039;")
            name = temp[0] + "'" + temp[1]
        try:
            get_id = requests.get(SEARCH_URL, headers=headers_spotify, params={'q': song["title"], 'type': "track", 'market': 'US'})
            get_id = get_id.json()
            trackID = get_id["tracks"]["items"][0]["id"]
            get_spotify = requests.get("https://api.spotify.com/v1/tracks/"+ trackID, headers=headers_spotify, params={'market': 'US'})
            get_spotify = get_spotify.json()
            release = song["history"]["debut_date"]
            duration = get_spotify["duration_ms"]
            album = get_spotify["album"]["name"]
            songs.append({"song_name": song["title"], "rank": song["rank"], "release_date": release, "duration": int(duration), "artist": name, "album": album})
        except Exception:
            print(name)
            print(song["title"])

    songJSON = {'Songs': songs}

    with open('songs.json', 'w') as fp:
        json.dump(songJSON, fp, indent=4)


def artistAPI():
    url_artist = "https://billboard2.p.rapidapi.com/artist_100"
    art = requests.request("GET", url_artist, headers=headers, params=querystring)
    art = art.json()

    artists = []

    for artist in art:
        name = artist["artist"]
        if "&#039;" in name:
            temp = name.split("&#039;")
            name = temp[0] + "'" + temp[1]
        try:
            get_artist = requests.get(SEARCH_URL, headers=headers_spotify, params={'q': name, 'type': "artist", 'market': 'US'})
            get_artist = get_artist.json()
            artID = get_artist["artists"]["items"][0]["id"]
            get_spotify = requests.get(ART_URL, headers=headers_spotify, params={'ids': artID})
            get_spotify = get_spotify.json()
            followers = get_spotify["artists"][0]["followers"]["total"]
            genre = get_spotify["artists"][0]["genres"]
            artists.append({"artist_name": artist["artist"], "artist_rank": int(artist["rank"]), "artist_genre": genre, "followers": int(followers)})
        except:
            print(name)
            print(get_artist)

    artistJSON = {'Artists': artists}
    with open('artists2.json', 'w') as fp:
        json.dump(artistJSON, fp, indent=4)

def albumAPI():
    url_albums = "https://billboard2.p.rapidapi.com/billboard_200"
    al = requests.request("GET", url_albums, headers=headers, params=querystring)
    al = al.json()

    albums = []
    for album in al[:100]:
        name = album["title"]
        if "&#039;" in name:
            temp = name.split("&#039;")
            name = temp[0] + "'" + temp[1]
        rank = album["rank"]
        release = album["history"]["debut_date"]
        artist = album["artist_name"]
        if "&#039;" in artist:
            temp = artist.split("&#039;")
            artist = temp[0] + "'" + temp[1]
        # genre =
        albums.append({"album_name": name, "album_rank": int(rank), "album_release_date": release, "artist": artist})

    albumJSON = {'Albums': albums}
    with open('albums.json', 'w') as fp:
        json.dump(albumJSON, fp, indent=4)

songAPI()

#if __name__ == "__main__":
    # songAPI()
    # artistAPI()
    # albumAPI()
