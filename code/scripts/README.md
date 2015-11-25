# Scripts

## Track_cut script 
This script lets you to cut part from soundtrack in .mp3 format.

To use this script move to the folder with script and type in terminal:
```
python track_cut.py song_path segment_from serment_to
```
Arguments __segment_from__ and __segment_to__ uses to determine time interval in seconds to cut.

## Convert audio file from .au to .wav format
In our project we use [GTZAN Genre Collection][GTZAN].
There are 10 genres represented, each containing 100 tracks. All the
tracks are 30 seconds long 22050Hz Mono 16-bit audio files in .au format. 
Audio format .au is not suitable for us due to data representation. That's why it is necessary to convert audio files to .wav.

To convert all .au files in current folder to .wav format Linux users can execute following command in terminal:
```
for i in $(ls *au); do ffmpeg -i $i ${i%.*}.wav; rm -f $i; done;
```

<!-- LINKS -->

[GTZAN]:
http://marsyas.info/downloads/datasets.html
