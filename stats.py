import spotipy
from spotipy.oauth2 import SpotifyOAuth
from colorama import Fore, Style

def colorize(text, color):
    return f"{color}{text}{Style.RESET_ALL}"

def get_spotify_stats():
    CLIENT_ID = 'CLIENT_ID'
    CLIENT_SECRET = 'CLIENT_SECRET'
    REDIRECT_URI = 'http://localhost:5173/callback/'
    SCOPE = 'user-library-read user-top-read user-read-recently-played user-read-playback-state'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope=SCOPE))

    now_playing = sp.current_playback()
    if now_playing and now_playing['is_playing']:
        track_name = now_playing['item']['name']
        artists = ', '.join([artist['name'] for artist in now_playing['item']['artists']])
        print(colorize(f"\nNow Playing: {track_name} - {artists}", Fore.MAGENTA))

    top_artists = sp.current_user_top_artists(limit=5, time_range='medium_term')
    print(colorize("\nTop 5 Artists:", Fore.MAGENTA))
    for idx, artist in enumerate(top_artists['items'], 1):
        print(f"{idx}. {colorize(artist['name'], Fore.CYAN)}")

    top_tracks = sp.current_user_top_tracks(limit=5, time_range='medium_term')
    print(colorize("\nTop 5 Songs:", Fore.MAGENTA))
    for idx, song in enumerate(top_tracks['items'], 1):
        artists = ', '.join([artist['name'] for artist in song['artists']])
        print(f"{idx}. {colorize(song['name'], Fore.CYAN)} - {colorize(artists, Fore.GREEN)}")

    top_albums = sp.current_user_top_tracks(limit=5, time_range='medium_term')
    print(colorize("\nTop 5 Albums:", Fore.MAGENTA))
    for idx, album in enumerate(top_albums['items'], 1):
        artists = ', '.join([artist['name'] for artist in album['artists']])
        print(f"{idx}. {colorize(album['album']['name'], Fore.CYAN)} - {colorize(artists, Fore.GREEN)}")

    recently_played = sp.current_user_recently_played(limit=5)
    print(colorize("\nTop 5 Recently Played Songs:", Fore.MAGENTA))
    for idx, track in enumerate(recently_played['items'], 1):
        artists = ', '.join([artist['name'] for artist in track['track']['artists']])
        print(f"{idx}. {colorize(track['track']['name'], Fore.CYAN)} - {colorize(artists, Fore.GREEN)}")

if __name__ == "__main__":
    get_spotify_stats()
