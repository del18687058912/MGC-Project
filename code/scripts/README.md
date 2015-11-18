# Track_cut script 
This script lets you to cut part from soundtrack in .mp3 format.
# Installing the dependencies
First you need want to install __libav__ or __ffmpeg__.

For Linux user's:
```` 
#libav
apt-get install libav-tools libavcodec-extra-53

#ffmpeg
apt-get install ffmpeg libavcodec-extra-53 
````
After that install [pydub library][pydub-library].

For Linux user's:
````
pip install pydub
````
# Example
Move to folder with script and type in terminal:
````
python track_cut.py song_path segment_from serment_to
````
Arguments __segment_from__ and __segment_to__ uses to determine time interval in seconds to cut.

<!-- LINKS -->

[pydub-library]: 
https://github.com/jiaaro/pydub
