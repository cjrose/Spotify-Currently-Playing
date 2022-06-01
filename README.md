# Spotify Currently Playing
A simple python script that grabs the most recent last.fm scrobbled [Spotify](https://spotify.com/) song for the purpose of displaying the currently playing song in [OBS](https://obsproject.com/).

## Requirements
To run this script, you will need to following:
* Python (or Python3) - [Download](https://www.python.org/downloads/)
* Requests Python package. To install, run `py -m pip install requests` in your command line once Python is installed.
* OBS (Preferred) - [Download](https://obsproject.com/)
* Spotify account - [Link](https://spotify.com/)
* last.fm account - [Link](https://last.fm/)

## Usage
Before running the scripts, you will need to enable last.fm scrobbling. This can be enabled by going to your Settings -> Applications, then connecting your spotify to last.fm.

You will also need a last.fm API Key to run the script. You can create an API account [here](https://www.last.fm/api/account/create). Once you have your key, add it to the `API_KEY` variable in the python script. You will also need to specify your last.fm username in the `USERNAME` field.

There are two scripts to choose from to run, `currently_playing_html.py` will generate a `songs.html` file that looks like this:

![html preview](https://user-images.githubusercontent.com/16892697/171449829-d21aaf92-2055-447b-8503-84eb258a78ae.png)

This html document will self-refresh every 2 seconds to avoid OBS caching and not updating the preview. To add this preview in OBS, create a new Browser source, check the `Local File` option and browse to the `songs.html` file. Change the width and height to 450 and 165 respectively. Your settings should look something like this:

![settings preview](https://user-images.githubusercontent.com/16892697/171450044-b199d231-d5c3-440b-bd32-43d881bc21cb.png)


The second script, `currently_playing_txt.py` creates a text document. By default, the format of this text file is `(song name) on (album name) by (artist)`. This can be customized in the first few lines of the script.

![settings](https://user-images.githubusercontent.com/16892697/171450703-95b83ff4-5534-40a4-9ff4-16408c67fe8a.png)

* Change `use_album_name` to `False` if you do not want the `on (album name)` to be added
* Change `use_artist_name` to `False` if you do not want the `by (artist name)` to be added
* Change `use_nowplaying_prefix` to `True` if you want `Now playing` to be added to the beginning of the string.

To add the text file to OBS, create a new Text (GDI+) source, and click `Read from file.` Browse to the `songs.txt` file and change the font to your preferences.
