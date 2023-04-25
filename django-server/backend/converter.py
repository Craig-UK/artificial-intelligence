from pydub import AudioSegment
import os
# Might need to put path in here for local machine 
# AudioSegment.converter = "C:\\FFMPEG_Files\\ffmpeg.exe"
# AudioSegment.ffmpeg = "C:\\FFMPEG_Files\\ffmpeg.exe"
# AudioSegment.ffprobe = "C:\\FFMPEG_Files\\ffprobe.exe"

def Convert(filename):

    script_dir = os.path.dirname(__file__)
    rel_path = "media/" + filename
    rel_path2 = "media/" + "shortvideo.wav"
    abs_file_path = os.path.join(script_dir, rel_path)
    abs_file_path2 = os.path.join(script_dir, rel_path2)

    clip = AudioSegment.from_file(abs_file_path, format="mp4")

    clip.export(abs_file_path2, format="wav")