# Music genre classification

## Description
TBD

## Installing python
TBD
```
sudo apt-get install python-dev python-tk
```
## Installing the dependencies
We provide detailed instructions only for Linux users, but Windows users can also easilly install all of that dependencies.

### FFmpeg
[FFmpeg][ffmpeg-official] is used to decode audio files and to convert samples to .wav format. To install __FFmpeg__ type in command line the following:

```
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install ffmpeg
```
Full information about installing __FFmpeg__ can be found on it's [ppa][ffmpeg-ppa] page.

### Pip
[Pip][pip-wiki] is a package management system used to install and manage software packages written in Python. You can install it as shown below:

```
sudo apt-get -y install python-pip
```
### Pydub library
The [pydub library][pydub-library] is a usefull module for working with audio files. We use it to get 30 seconds sample from each song that could be considered as training or testing data. To install this use terminal:

```
pip install pydub
```

### Python speech features
[Python speech features][python-speech-features-git] is a library that provides common speech features for ASR including MFCCs and filterbank energies. We use this library to calculate Mel Frequency Cepstral Coefficients for each song. To install it you should download zip from git page and unpack it or or clone git repository (if you have git intalled):
```
git clone https://github.com/jameslyons/python_speech_features.git
```
Then you should setup environment to use the library in your project:
```
cd ./python_speech_features
sudo python setup.py install
```
### Scikit-learn
[Scikit-learn][scikit-learn-official]
TBD
```
pip install -U scikit-learn
```

## Mel Frequency Cepstral Coefficients (MFCC)
TBD

## k-Nearest Neighbors algorithm (k-NN)
k-NN is a non-parametric method used for classification. Input consists of the l closest training examples in the feature space. An object is classified by a majority vote of its neghbots, with the object begin assigned to the class most common among its k nearest neighbors. It can be useful to assign weight to the contributions of the neighbors, so that the nearer neighbors contribute more to the average than the more distant ones. More infomation about this algorithm can be found on [Wikipedia][knn-algorithm-wiki].

To figure out the distance between two songs we use Kullback-Leibler divergence. So we have two multivatiate Gaussian distribution with mean and covariance derived from the MFCC matrix for each song. To compute the distance we use the following formula: 

![KL-divergence-for-multivariate-Normal-distribution][KL-divergence-for-multivariate-Normal-distribution-image]

where ![mu][mu-image] are means, ![covariance-matricies][covariance-matricies-image] are covariance matricies. 

![trace-formula](https://upload.wikimedia.org/math/5/f/5/5f5e87515ab75d6ac2da5e936af81d1f.png) is a [trace][trace-wiki] of square matrix.

More information about Kullback-Leibler divergence can be found on [Wikipedia][KL-divergence-wiki].


<!-- LINKS -->
  
[ffmpeg-official]:
https://www.ffmpeg.org/
[pip-wiki]:
https://en.wikipedia.org/wiki/Pip_(package_manager)
[pydub-library]:
https://github.com/jiaaro/pydub
[ffmpeg-ppa]:
https://launchpad.net/~mc3man/+archive/ubuntu/trusty-media
[python-speech-features-git]:
https://github.com/jameslyons/python_speech_features
[scikit-learn-official]:
http://scikit-learn.org/stable/index.html
[knn-algorithm-wiki]:
https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
[KL-divergence-wiki]:
https://en.wikipedia.org/wiki/Kullback–Leibler_divergence
[KL-divergence-for-multivariate-Normal-distribution-image]:
https://upload.wikimedia.org/math/7/4/d/74d5ae529f03bde48a2b92c4f29aa58c.png
[mu-image]:
https://upload.wikimedia.org/math/f/6/2/f627798b2478f55112483851e60c5cf7.png
[covariance-matricies-image]:
https://upload.wikimedia.org/math/e/2/0/e206ca0dd0e69c8b3e4c408904defa4a.png
[trace-wiki]:
https://en.wikipedia.org/wiki/Trace_(linear_algebra)