import requests, json
from datetime import date

querystring = {"date":date.today().strftime("%Y-%m-%d")}
headers = {
    'x-rapidapi-key': "9fecb91ce1mshb6c4094e7a3d2a6p1d58cejsn3f7fdfb7846e",
    'x-rapidapi-host': "billboard2.p.rapidapi.com"
    }
headers_audioDB = {
    'x-rapidapi-key': "e0ce79f895msh1b9afd3a9d55c1dp1b6355jsn312a3daff134",
    'x-rapidapi-host': "theaudiodb.p.rapidapi.com"
    }

def songAPI():
    url = "https://billboard2.p.rapidapi.com/hot_100"
    url_audioDB = "https://theaudiodb.p.rapidapi.com/searchtrack.php"
    res = requests.request("GET", url, headers=headers, params=querystring)
    res = res.json()

    songs = []

    for song in res:
        if "&#039;" in song["title"]:
            temp = song["title"].split("&#039;")
            song["title"] = temp[0] + "'" + temp[1]

        if "&#039;" in song["artist_name"]:
            temp = song["artist_name"].split("&#039;")
            song["artist_name"] = temp[0] + "'" + temp[1]

        querystring_audioDB = {"s":song["artist_name"],"t":song["title"]}
        track = requests.request("GET", url_audioDB, headers=headers_audioDB, params=querystring_audioDB)
        track = track.json()
        # songs.append({"song_name": song["title"], "rank": song["rank"], "release_date": song["history"]["debut_date"], "artist": song["artist_name"]})
        print(song["title"])
        songs.append({"song_name": song["title"], "rank": song["rank"], "release_date": song["history"]["debut_date"], "duration": int(track["track"][0]["intDuration"]), "artist": song["artist_name"]})

    # print(songs)

    songJSON = {'Songs': songs}

    with open('songs.json', 'w') as fp:
        json.dump(songJSON, fp, indent=4)

CLIENT_ID = "852c80dddc2242c690fd514762d73d86"
CLIENT_SECRET = "dcd5f80d6deb4215a996e1a0719c64a2"
AUTH_URL = 'https://accounts.spotify.com/api/token'
SEARCH_URL = "https://api.spotify.com/v1/search"
ART_URL = "https://api.spotify.com/v1/artists"
auth_response = requests.post(AUTH_URL, {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET,})
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headers_spotify = {'Authorization': 'Bearer {token}'.format(token=access_token)}

def artistAPI():
    url_artist = "https://billboard2.p.rapidapi.com/artist_100"
    art = requests.request("GET", url_artist, headers=headers, params=querystring)
    art = art.json()

    artists = []

    for artist in art:
        get_artist = requests.get(SEARCH_URL, headers=headers_spotify, params={'q': artist["artist"], 'type': "artist", 'market': 'US'})
        get_artist = get_artist.json()
        artID = get_artist["artists"]["items"][0]["id"]
        get_spotify = requests.get(ART_URL, headers=headers_spotify, params={'ids': artID})
        get_spotify = get_spotify.json()
        print(get_spotify["artists"][0]["genres"])
        artists.append({"artist_name": artist["artist"], "artist_rank": artist["rank"], "artist_genre": get_spotify["artists"][0]["genres"], "followers": get_spotify["artists"][0]["followers"]["total"]})

    print(artists)
    
    # artistJSON = {'Artists': artists}
    # with open('artists.json', 'w') as fp:
        # json.dump(artistJSON, fp, indent=4)

def albumAPI():
    pass

if __name__ == "__main__":
    # songAPI()
    # artistAPI()
    # albumAPI()