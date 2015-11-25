# Music genre classification

## Description
TBD

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

## Mel Frequency Cepstral Coefficients (MFCC)
TBD

<!-- LINKS -->
  
[pydub-library]:
https://github.com/jiaaro/pydub
[ffmpeg-ppa]:
https://launchpad.net/~mc3man/+archive/ubuntu/trusty-media
