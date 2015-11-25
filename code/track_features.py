from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav

def get_covariance_matrix(fbank_feat):
    num_segments = len(fbank_feat)
    num_features = len(fbank_feat[0])

    cov_mat = []
    for i in range(num_features):
        tmp_mat = []           
        for j in range(num_features):
            value = 0
            mean_1 = 0
            mean_2 = 0
            for k in range(num_segments):
            	mean_1 += fbank_feat[k][i]
            	mean_2 += fbank_feat[k][j]
                value += fbank_feat[k][i] * fbank_feat[k][j]
            mean_1 /= num_segments
            mean_2 /= num_segments
            value /= num_segments
            tmp_mat.append(value - mean_1 * mean_2)
        cov_mat.append(tmp_mat)
    return cov_mat

def get_features_mean(fbank_feat):
	num_segments = len(fbank_feat)
	num_features = len(fbank_feat[0])

	mean = [0 for i in range(num_features)]
	for i in range(num_segments):
		mean += fbank_feat[i]
	for i in range(num_features):
		mean[i] /= num_segments

	return mean

def get_track_features(track_name):
	(rate,sig) = wav.read(track_name)
	mfcc_feat = mfcc(sig,rate)
	fbank_feat = logfbank(sig,rate)

	num_segments = len(fbank_feat)
	num_features = len(fbank_feat[0])

	features_mean = get_features_mean(fbank_feat)
	cov_mat = get_covariance_matrix(fbank_feat)

	return (features_mean, cov_mat)
