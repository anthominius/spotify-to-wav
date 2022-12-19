import os
import spotipy as sp
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

scope = 'playlist-read-private'
redirect_uri = 'http://localhost:8888/callback'

playlist_uri = 'spotify:playlist:37i9dQZF1F0sijgNaJdgit'
spotify = sp.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                              client_secret=client_secret,
                                              redirect_uri=redirect_uri,
                                              scope=scope))


def search_artist():
    results = spotify.search(q='Kaytranada', limit=20)
    for idx,track in enumerate(results['tracks']['items']):

        print(idx,track['name'])

def playlist_tracks(str: playlist_uri=playlist_uri):
    tup = []
    tracks = spotify.playlist_items(playlist_uri,
                                    limit=100,
                                    fields='items.track.name,items.track.artists.name',
                                    additional_types=['track'])

    if len(tracks['items']) == 0:
        return

    for items in tracks['items']:
        track = items['track']
        output = {
            'name': track['name'],
            'artist': track['artists'][0]['name']
        }
        tup.append(output['name'] + " " + output['artist'])
    return tup

def check_current_user():
    user_playlist = spotify.current_user_playlists(limit=50)

    for i, item in enumerate(user_playlist['items']):
        print("%d %s %s" % (i, item['name'],item['uri']))


#if __name__ == "__main__":


