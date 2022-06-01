### Run this script if you want the songs.txt file to be generated
### Add to OBS with a Text (GDI+). Click "Read from file" and find songs.txt
###

import requests
import time
from datetime import datetime

# Change to your liking
use_album_name = True
use_artist_name = True
use_nowplaying_prefix = False

ROOT_URL = 'http://ws.audioscrobbler.com/2.0/'
# PUT YOUR API KEY HERE
API_KEY = ''
# PUT YOUR LAST.FM USERNAME HERE
USERNAME = ''

### method for grabbing the most recently scrobbled track
def get_recently_played():
    # Format the url to grab the most recent track
    url = ROOT_URL + f'?method=user.getrecenttracks&user={USERNAME}&api_key={API_KEY}&format=json&limit=10'
    response = requests.get(url)
    responseJSON = response.json()

    if response.status_code == 200:
        most_recent_track = responseJSON['recenttracks']['track'][0]
        # print(most_recent_track)
        # Create a dictionary for the returned values
        track_dict = {
            'track_name': most_recent_track['name'],
            'album_name': most_recent_track['album']['#text'],
            'artist_name': most_recent_track['artist']['#text'],
            # number dictates image size. 0 - small, 1 - medium, 2 - large, 3 - extralarge 
            'album_art_url': most_recent_track['image'][2]['#text']
        }
        # @attr does not get returned if the track is not being played
        if '@attr' in most_recent_track:
            track_dict['is_playing'] = most_recent_track['@attr']['nowplaying']
        else:
            track_dict['is_playing'] = 'false'
        return track_dict
    else:
        return None

### Method for creating the 'song.txt' file
def write_song_txt(song_string):
    file = open('song.txt', 'w')
    file.write(song_string)
    file.close()


### Utility method for creating the string to be written in the text document
def format_song_string(track_dict):
    output = ''

    if use_nowplaying_prefix:
        output += 'Now Playing '

    output += track_dict['track_name']

    if use_album_name:
        output += f' on {track_dict["album_name"]}'
    
    if use_artist_name:
        output += f' by {track_dict["artist_name"]}'
    
    return output


### Main method of the script
def main():
    # Store the last listened to track for logging purposes
    most_recent_track = None
    while(True):
        # get the most recent track
        track_dict = get_recently_played()

        # if not playing a song and the stored track differs from the new one, print that no song is playing
        if track_dict['is_playing'] == 'false' and most_recent_track != track_dict:
            print(f'Time: {datetime.now()}\nNo song playing....\n\n')
            most_recent_track = track_dict

        # if the most recent track is not null and the stored track differs from the new one, post the updated track info
        elif track_dict is not None and most_recent_track != track_dict:
            print(f'Time: {datetime.now()}\nSong: {track_dict["track_name"]}\nAlbum: {track_dict["album_name"]}\nArtist: {track_dict["artist_name"]}\n\n')
            most_recent_track = track_dict

        # if the user is actively listening to a song, create the document
        if track_dict is not None and track_dict['is_playing'] == 'true':
            write_song_txt(format_song_string(track_dict))

        # if the user is not listening to a song, change to no song playing
        elif track_dict is not None and track_dict['is_playing'] == 'false':
            write_song_txt('No song playing...')

        # any other instance is an error
        else: 
            write_song_txt('Error getting recent track')
        


        # wait 5 seconds before each update
        time.sleep(5)


if __name__ == '__main__':
    main()