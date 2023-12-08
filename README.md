# spotify-stats-python
A script written in Python to get your Spotify stats :)

## Features

- Display the currently playing song at the top with a distinctive color.
- Show your top 5 artists based on listening history.
- Present the top 5 songs you've listened to recently.
- Highlight your top 5 albums.
- Share the top 5 songs you've recently played.


## Requirements

- Python 3.x
- `spotipy` library (install it via `pip install spotipy`)
- `colorama` library (install it via `pip install colorama`)

## Setup Instructions
1. Clone this repository.
2. Install the dependencies `pip install -r requirements.txt`
3. Configure Spotify API credentials:

Create a Spotify App on the Spotify Developer Dashboard.
Obtain your `CLIENT_ID` and `CLIENT_SECRET.`
Set the `REDIRECT_URI` to http://localhost:5173/callback/ in your Spotify App settings.
4. Update stats.py: Replace the placeholders in the get_spotify_stats function with your `CLIENT_ID` and `CLIENT_SECRET`.
5. You can now run `python stats.py` to get the stats.
