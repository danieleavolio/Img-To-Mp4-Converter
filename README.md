# Video Creator

Video Creator is a Python application that allows you to create a video from an image and an audio file. The application provides a simple GUI for selecting the image and audio files, and for starting the video creation process.

<p align="center">
    <img src="https://i.imgur.com/k8zcdF2.png" alt="Video Creator GUI">
</p>
<div style="display:flex; justify-content:space-between">
    <img src="https://i.imgur.com/BePm1U3.png" alt="Example" width="49%">
    <img src="https://i.imgur.com/JP1nOZU.png" alt="Example" width="49%">
</div>

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


<marquee direction="left" scrollamount="50">
I am not sure if this works on Linux and macOS. If you are a Linux or macOS user, please let me know if it works or not.
</marquee>