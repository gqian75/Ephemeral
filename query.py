import psycopg2
import psycopg2.extras
DB_HOST = "queenie.db.elephantsql.com"
DB_NAME = "zuvviiky"
DB_USER = "zuvviiky"
DB_PASS = "gUj52EfnqxD2UeVkSPQ7kDeiAQOwMcu6"
DB_PORT = "5432"

db = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

query = db.cursor(cursor_factory=psycopg2.extras.DictCursor)

query.execute('SELECT * FROM song;')
song_list = query.fetchall()

# What we have
# query.execute('SELECT * FROM artist as a left join song as s on a.artist_name = s.artist;')
# New idea
# #query.execute('SELECT song_name FROM song as s WHERE rank in (SELECT song_rank FROM link WHERE artist_rank in (SELECT artist_rank FROM artist));')
# query.execute('select * from artist left join link on artist.artist_rank = link.artist_rank left join song on song.rank = link.song_rank;')
# artist_list = query.fetchall()


# query.execute("select album.album_name from album left join song on album.album_rank = song.album_rank;")
# album_list = query.fetchall()


print(song_list)
print(len(song_list))


query.close()
db.close()

# import os
# import urllib.parse as up
# import psycopg2
#
# up.uses_netloc.append("postgres")
# url = up.urlparse(os.environ["postgres://zuvviiky:gUj52EfnqxD2UeVkSPQ7kDeiAQOwMcu6@queenie.db.elephantsql.com:5432/zuvviiky"])
# conn = psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
#
# conn.close()
