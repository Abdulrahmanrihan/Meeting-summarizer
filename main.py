from video_to_audio import extract_audio_file
from audio_transcription import transcribe
from gemini_text_summarizer import summarize_text

import audio_extract

def summarize_meeting(video_path, audio_path):
    print("Initializing video to audio transformation")
    extract_audio_file(video_path, audio_path)
    print("Starting the transcription process")
    transcription = transcribe(audio_path)
    print("We have the transcription, Now we summarize!")
    summarization = summarize_text(transcription)
    print("Here is your meeting's summary: \n")
    print(summarization)

if __name__ == "__main__":
    video_name = input("Enter the video's name: ")
    video_path_original = './videos/' + video_name + '.mp4'
    audio_path_original = './audios/' + video_name + '.mp3'
    summarize_meeting(video_path_original, audio_path_original)