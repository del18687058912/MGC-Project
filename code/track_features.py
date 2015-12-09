import os
from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav
import numpy as np

def _get_covariance_matrix(mfcc_feat):
    num_segments = len(mfcc_feat)
    num_features = len(mfcc_feat[0])

    cov_mat = []
    for i in range(num_features):
        tmp_mat = []           
        for j in range(num_features):
            value = 0
            mean_1 = 0
            mean_2 = 0
            for k in range(num_segments):
                mean_1 += mfcc_feat[k][i]
                mean_2 += mfcc_feat[k][j]
                value += mfcc_feat[k][i] * mfcc_feat[k][j]
            mean_1 /= num_segments
            mean_2 /= num_segments
            value /= num_segments
            tmp_mat.append(value - mean_1 * mean_2)
        cov_mat.append(tmp_mat)
    return cov_mat

def _get_features_mean(mfcc_feat):
    num_segments = len(mfcc_feat)
    num_features = len(mfcc_feat[0])

    mean = [0 for i in range(num_features)]
    for i in range(num_segments):
        mean += mfcc_feat[i]
    for i in range(num_features):
        mean[i] /= num_segments

    return mean

def get_track_features(track_name):
    (rate,sig) = wav.read(track_name)
    mfcc_feat = mfcc(sig,rate)
    fbank_feat = logfbank(sig,rate)

    num_segments = len(mfcc_feat)
    num_features = len(mfcc_feat[0])

    features_mean = _get_features_mean(mfcc_feat)
    cov_mat = _get_covariance_matrix(mfcc_feat)

    return (features_mean, cov_mat)

def get_features(dir_path, max_track_number, *genre_names): 
    features = []   
    for genre_name in genre_names:
        genre_dir_path = dir_path + "/" + genre_name +"/"
        track_list = os.listdir(genre_dir_path)
        track_list = track_list[:int(max_track_number)]

        for index in range(len(track_list)):
            track_list[index] = genre_dir_path + track_list[index]

        for track in track_list:
            print "Reading ", track
            (mean, cov_mat) = get_track_features(track)
            features.append((mean, cov_mat, genre_name))

    return features

def get_genre_ID(genre_name):
    track_ID = ""
    for ch in genre_name:
        char_ID = str(ord(ch))
        if int(char_ID) < int(100):
            char_ID = "0"+char_ID
        track_ID += char_ID

    return int(track_ID)

def get_genre_name(genre_ID):
    genre_ID_list = list(str(genre_ID))
    if len(genre_ID_list) % 3 != 0:
        genre_ID_list = ["0"] + genre_ID_list
    genre_name = ""
    i = 0
    while (i < len(genre_ID_list)):
        genre_name_ch = genre_ID_list[i] + genre_ID_list[i + 1] + genre_ID_list[i + 2]
        genre_name += chr(int(genre_name_ch))
        i += 3
        
    return genre_name

def list_to_cortege(features, n_features):
    mean = features[0:n_features]
    covariance = features[n_features:].reshape(n_features, n_features)
    return (mean, covariance)

def cortege_to_list(features):
    return np.concatenate([features[0], np.array(features[1]).ravel()]).tolist()

def read_features_from_files(dir_path, genre_names):
    features_cortege_list = []
    for genre_name in genre_names: 
        features_file = open(dir_path + "/" + genre_name + ".txt", "r")

        n_features = int(features_file.readline())

        for line in features_file:
            features_list = map(float, line[1:len(line) - 2].split(", "))
            (mean, cov_mat) = list_to_cortege(np.array(features_list), n_features)
            features_cortege_list.append((mean, cov_mat, genre_name))

        features_file.close()

    return features_cortege_list

def write_features_to_file(dir_path, genre_name, features_cortege_list):
    features_file = open(dir_path + "/" + genre_name + ".txt", "w")
    features_file.write(str(len(features_cortege_list[0][0])) + "\n")
    for features_cortege in features_cortege_list:
        features_file.write(str(cortege_to_list(features_cortege)) + "\n")

    features_file.close()
