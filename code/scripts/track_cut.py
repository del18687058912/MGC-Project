import sys
from pydub import AudioSegment

song_path = sys.argv[1]
segment_from_sec = int(sys.argv[2])
segment_to_sec = int(sys.argv[3])

segment_from_milsec = segment_from_sec * 1000
segment_to_milsec = segment_to_sec * 1000

song = AudioSegment.from_mp3(song_path)

song_segment = song[segment_from_milsec:][:segment_to_milsec]

song_segment.export("track_" + str(segment_from_sec) + ":" + str(segment_to_sec) + ".mp3", format = "mp3")