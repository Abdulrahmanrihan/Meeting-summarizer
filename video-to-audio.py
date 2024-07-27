import os
from audio_extract import extract_audio

# Get the user's home directory
home_directory = os.path.expanduser("~")

# Specify the path to the FFMPEG executable
ffmpeg_path = os.path.join(home_directory, "Downloads", "video-to-audio", "ffmpeg")

# Set the environment variable for FFMPEG executable
os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path

video_path = "./benaa_al_qowa_al_nafsya.mp4"
audio_path = "./benaa_al_qowa_al_nafsya.mp3"

def extract_audio_file(input_path, output_path):
    # Call the extract_audio function
    extract_audio(input_path=input_path, output_path=output_path)

if __name__ == "__main__":
    extract_audio_file(video_path, audio_path)
