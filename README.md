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

## k-Nearest Neighbors algorithm (k-NN)
k-NN is a non-parametric method used for classification. Input consists of the l closest training examples in the feature space. An object is classified by a majority vote of its neghbots, with the object begin assigned to the class most common among its k nearest neighbors. It can be useful to assign weight to the contributions of the neighbors, so that the nearer neighbors contribute more to the average than the more distant ones. More infomation about this algorithm can be found on [Wikipedia][knn-algorithm-wiki].

To figure out the distance between two songs we use Kullback-Leibler divergence. So we have two multivatiate Gaussian distribution with mean and covariance derived from the MFCC matrix for each song. To compute the distance we use the following formula: 

![KL-divergence-for-multivariate-Normal-distribution][KL-divergence-for-multivariate-Normal-distribution-image]

where ![mu][mu-image] are means, ![covariance-matricies][covariance-matricies-image] are covariance matricies. 

![trace-formula](https://upload.wikimedia.org/math/5/f/5/5f5e87515ab75d6ac2da5e936af81d1f.png) is a [trace][trace-wiki] of square matrix.

More information about Kullback-Leibler divergence can be found on [Wikipedia][KL-divergence-wiki].


<!-- LINKS -->
  
[pydub-library]:
https://github.com/jiaaro/pydub
[ffmpeg-ppa]:
https://launchpad.net/~mc3man/+archive/ubuntu/trusty-media
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
