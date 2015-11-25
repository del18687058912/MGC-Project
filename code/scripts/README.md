# Music genre classification


## Installing the dependencies
First you need to install __libav__ or __ffmpeg__.
Full information about installing __ffmpeg__ can be found [here][ffmpeg-ppa].

For Linux users:
```
#libav
sudo apt-get install libav-tools

#ffmpeg
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install ffmpeg
```
Then you need to install __pip__.

For Linux users:
```
sudo apt-get -y install python-pip
```
After that install [pydub library][pydub-library].

For Linux users:
```
pip install pydub
```
## Scripts

### Track_cut script 
This script lets you to cut part from soundtrack in .mp3 format.

### Convert audio file from .au to .wav format
In our project we use [GTZAN Genre Collection][GTZAN].
There are 10 genres represented, each containing 100 tracks. All the
tracks are 30 seconds long 22050Hz Mono 16-bit audio files in .au format. 
Audio format .au is not suitable for us due to data representation. That's why it is necessary to convert audio files to .wav.

To convert all .au files in current folder to .wav format Linux users can execute following command in terminal:
```
for i in $(ls *au); do ffmpeg -i $i ${i%.*}.wav; rm -f $i; done;
```

### Mel Frequency Cepstral Coefficients (MFCC)
TBD



### Examples

#### Track_cut script
Move to folder with script and type in terminal:
```
python track_cut.py song_path segment_from serment_to
```
Arguments __segment_from__ and __segment_to__ uses to determine time interval in seconds to cut.

#### MFCC usage

TBD

<!-- LINKS -->

[pydub-library]:
https://github.com/jiaaro/pydub
[ffmpeg-ppa]:
https://launchpad.net/~mc3man/+archive/ubuntu/trusty-media
[GTZAN]:
http://marsyas.info/downloads/datasets.html