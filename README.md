# Spotify Currently Playing
A quick and simple script that writes your currently played song to a text file. The script executes the GET request every 5 seconds and writes the result to the text file 'song.txt' in the same directory. You can use a text element in OBS to read from this file to show the currently playing song.

## ** Getting your own OAUTH Token**

Before you can run the script, you will need to get your own OAUTH token and add it to the script. You can get your token from [here](https://developer.spotify.com/console/get-users-currently-playing-track). Click "Get Token" and make sure you add `user-read-currently-playing` to the scope of the OAUTH, then press request. Copy and paste the OAUTH token into the script.py `OAUTH_TOKEN` variable.

## **Requires `requests` to be installed**

Run `pip install requests` or `pip3 install requests` for Python3 to install the package


## **Response Status 204?**

You aren't listening to anything...
