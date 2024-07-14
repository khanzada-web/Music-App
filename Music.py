from pydub import AudioSegment
from pydub.playback import play

file_path = r"D:\Cubex_interShip_projects\Music App\music\8.mp3"

song = AudioSegment.from_mp3(file_path)
play(song)
