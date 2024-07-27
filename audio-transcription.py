import torch
from transformers import pipeline
from pydub import AudioSegment

whisper  = pipeline("automatic-speech-recognition", "openai/whisper-small")

def extract_audio_segment(input_file, output_file, start_time_ms, end_time_ms):
    audio = AudioSegment.from_file(input_file)

    # Extract the segment using the start and end times
    extracted_segment = audio[start_time_ms:end_time_ms]

    # Export the extracted segment to a new file
    extracted_segment.export(output_file, format="mp3")


def transcribe(path_to_audio):
    transcription = whisper(path_to_audio, chunk_length_s=20, stride_length_s=5, batch_size=1)
    return transcription

if __name__ == "__main__":

    # Specify the input audio file, output file, and the start and end times in milliseconds
    input_file = "benaa_al_qowa_al_nafsya.mp4"
    output_file = "benaa.mp3"
    start_time_ms = 10000  # Start time in milliseconds
    end_time_ms = 20000  # End time in milliseconds

    extract_audio_segment(input_file, output_file, start_time_ms, end_time_ms)
    transcribe(output_file)
