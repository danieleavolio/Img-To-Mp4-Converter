# Video Creator

Video Creator is a Python application that allows you to create a video from an image and an audio file. The application provides a simple GUI for selecting the image and audio files, and for starting the video creation process.

## Requirements

- Python 3.6 or higher
- Pillow 8.3.2
- opencv-python 4.5.3.56
- ffmpeg

## Installation

1. Clone this repository.
2. Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

3. Install ffmpeg on your system. You can download it from the [official website](https://www.ffmpeg.org/download.html).

    If you are on `Linux` or `macOS`, you can install ffmpeg using the following commands:

    ```bash
    # Debian, Ubuntu, Linux Mint, Pop!_OS, etc.
    sudo apt install ffmpeg

    # Fedora, CentOS, RHEL, etc.
    sudo dnf install ffmpeg

    # macOS
    brew install ffmpeg
    ```

## Usage

Run the `converter_guy.py` script to start the application:

For Windows users:

```bat
run_converter.bat
```

For Linux and macOS users:

```bash
./run_converter.sh
```