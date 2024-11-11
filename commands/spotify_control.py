from dotenv import load_dotenv
import os
import spotipy
import base64
import json
import requests
from spotipy.oauth2 import SpotifyOAuth
from urllib.error import HTTPError

load_dotenv()

scope = "user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"), client_secret = os.getenv("SPOTIFY_CLIENT_SECRET"), scope=scope, redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')))

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

def search(query, type = 'track'):
    try:
        res = sp.search(query, type=type)
        one_res = res['tracks']['items'][0]
        return [one_res['uri']]
    except HTTPError as err:
        if err.code == 404:
            print(err)
        else: pass
def skip(): sp.next_track()
def pause(): sp.pause_playback()
def previous(): sp.previous_track()
def start(): sp.start_playback()
def set_volume(volume): 
    try:
        volume = int(volume)
        sp.volume(volume)
    except:
        print('Inavlid volume')
def play_song(song_name): 
    uri = search(song_name)
    sp.start_playback(uris = uri)
def transfer_to_device(device_id): sp.transfer_playback(device_id)
def add_to_queue(song_name):
    print(song_name)
    uri = search(song_name)
    sp.add_to_queue(uri[0])
