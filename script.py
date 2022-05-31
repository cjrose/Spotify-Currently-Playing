import requests
import time

URL = 'https://api.spotify.com/v1/me/player/currently-playing'
OAUTH_TOKEN = ''

def get_song():
    # build the header
    header = {"Content-Type":"application/json", "Authorization": f"Bearer {OAUTH_TOKEN}"}
    # GET method
    response = requests.get(URL, headers= header)

    if (response.status_code == 200):
        # Parse the response into JSON format
        responseJSON = response.json()
        song_name = responseJSON['item']['name']
        album_name = responseJSON['item']['album']['name']

        all_artists = responseJSON['item']['artists']
        artist_concat = ''
        for artist in all_artists:
            if len(artist_concat) > 0:
                artist_concat += ', ' + artist['name']
            else:
                artist_concat = artist['name']
        
        return f'{song_name} by {artist_concat} on {album_name}'

    else:
        print(f'ERROR: Response Status {response.status_code}')
        return None


def write_song(song_string):
    file = open('song.txt', 'w')
    if song_string is not None:
        file.write(song_string)
    file.close()

def main():
    while(True):
        # Loop infinitely until the program is closed
        song_string = get_song()
        write_song(song_string)
        time.sleep(5)


if __name__ == '__main__':
    main()