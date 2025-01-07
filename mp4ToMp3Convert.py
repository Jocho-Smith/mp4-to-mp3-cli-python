import sys
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file):
    try:
        # Load the MP4 file
        video = VideoFileClip(input_file)
        
        # Extract the filename without extension
        output_file = input_file.rsplit(".", 1)[0] + ".mp3"
        
        # Extract and save audio as MP3
        video.audio.write_audiofile(output_file)
        print(f"Conversion successful! Audio saved as: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mp4ToMp3Convert.py <file.mp4>")
    else:
        input_file = sys.argv[1]
        convert_mp4_to_mp3(input_file)
