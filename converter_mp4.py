import subprocess
import sys
import os

def convert_to_mp4(input_file):
    # Get the base name and extension of the input file
    base_name, _ = os.path.splitext(input_file)
    # Create the output file path
    output_file = base_name + "_conv.mp4"
    # Create the FFmpeg command
    ffmpeg_cmd = ["ffmpeg", "-i", input_file, "-c:v", "mpeg4", "-b:v", "2M", "-c:a", "aac", "-b:a", "192k", "-y", output_file]
    # Run the FFmpeg command
    subprocess.run(ffmpeg_cmd, check=True)

if __name__ == "__main__":
    # Check if an input file was provided
    if len(sys.argv) < 2:
        print("Usage: python converter_mp4.py <input_file>")
        sys.exit(1)
    # Convert the input file to MP4
    convert_to_mp4(sys.argv[1])