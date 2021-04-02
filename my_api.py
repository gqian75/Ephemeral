import requests, json, base64
from urllib.parse import urlencode
from datetime import date

querystring = {"date":date.today().strftime("%Y-%m-%d")}
headers = {
    'x-rapidapi-key': "cdec391e94msh59bba6e6cb20d6dp148a7bjsn7a9048b31414",
    'x-rapidapi-host': "billboard2.p.rapidapi.com"
    }
headers_audioDB = {
    'x-rapidapi-key': "9fecb91ce1mshb6c4094e7a3d2a6p1d58cejsn3f7fdfb7846e",
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

def songAPI():
    url = "https://billboard2.p.rapidapi.com/hot_100"
    url_audioDB = "https://theaudiodb.p.rapidapi.com/searchtrack.php"
    res = requests.request("GET", url, headers=headers, params=querystring)
    res = res.json()

    songs = []
    song_list = []

    text_file = open("json.txt","w") # json information on json.txt
    text_file.write(str(res))
    text_file.close()

    for song in res:
        if "&#039;" in song["title"]:
            temp = song["title"].split("&#039;")
            song["title"] = temp[0] + "'" + temp[1]
        name = song["credited_artists"][0]["artist_name"]
        
        if "&#039;" in name:
            temp = name.split("&#039;")
            name = temp[0] + "'" + temp[1]
        try:
            r = requests.get(SEARCH_URL, headers=headers_spotify, params={'q': song['title'], 'type': 'track','market':'US'})
            r = r.json()

            if (r['tracks']['items'][0]['album']['album_type']=='single'):
                album = 'single'
            else:
                album=r["tracks"]["items"][0]["album"]["name"]
            duration = r['tracks']['items'][0]['duration_ms']
            songs.append({"song_name": song["title"], "rank": song["rank"], "release_date": song["history"]["debut_date"],
            "artist": name, "album":album, "duration":duration})

        except:

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
            popularity = get_spotify["artists"][0]["popularity"]
            genre = get_spotify["artists"][0]["genres"]
            artists.append({"artist_name": artist["artist"], "artist_rank": int(artist["rank"]), "artist_genre": genre, "followers": int(followers), "popularity": int(popularity)})
            if(genre==[]):
                genre=["N/A"]
        except:
            print(name)
            print(get_artist)

    artistJSON = {'Artists': artists}
    with open('artists.json', 'w') as fp:
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

        try:
            get_artist = requests.get(SEARCH_URL, headers=headers_spotify, params={'q': artist, 'type': "artist", 'market': 'US'})
            get_artist = get_artist.json()
            artID = get_artist["artists"]["items"][0]["id"]
            get_spotify = requests.get(ART_URL, headers=headers_spotify, params={'ids': artID})
            get_spotify = get_spotify.json()
            genre = get_spotify["artists"][0]["genres"]
            if genre==[]:
                genre = ['N/A']
        except:
            genre = ['N/A']


        albums.append({"album_name": name, "album_rank": int(rank), "album_release_date": release, "artist": artist, "genre": genre})

    albumJSON = {'Albums': albums}
    with open('albums.json', 'w') as fp:
        json.dump(albumJSON, fp, indent=4)

def imagesAPI():
    with open('songs.json') as f:
        j = json.load(f)

    imagesA = [] # artists
    imagesB = [] # songs
    for i in j["Songs"]:
        artist = i["artist"]
        r = requests.get(SEARCH_URL, headers=headers_spotify, params={'q': artist, 'type': 'artist','limit':'1'})
        r = r.json()
        r = r['artists']['items'][0]['images']
        imagesA.append({'artist_name': artist, "image": r})

        track = i['song_name']
        r = requests.get(SEARCH_URL, headers=headers_spotify, params={'q': track, 'type': 'track','limit':'1'})
        r = r.json()
        r = r['tracks']['items'][0]['album']['images']
        imagesB.append({'track_name': track, 'image': r})



    image1JSON = {'Images': imagesA}
    with open('images.json', 'w') as fp: # images of artists
        json.dump(image1JSON, fp, indent=4)

    image2JSON = {'Images': imagesB}
    with open('images2.json', 'w') as fp: # images of songs
        json.dump(image2JSON, fp, indent=4)

if __name__ == "__main__":
    songAPI()
    artistAPI()
    albumAPI()
    imagesAPI()
