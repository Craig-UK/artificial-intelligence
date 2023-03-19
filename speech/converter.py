#pip install pydub
from pydub import AudioSegment
# Might need to put path in here for local machine 
# AudioSegment.converter = "C:\\FFMPEG_Files\\ffmpeg.exe"
# AudioSegment.ffmpeg = "C:\\FFMPEG_Files\\ffmpeg.exe"
# AudioSegment.ffprobe = "C:\\FFMPEG_Files\\ffprobe.exe"

clip = AudioSegment.from_mp3("PythonTest.mp3")

clip.export("PythonTesting.wav", format="wav")