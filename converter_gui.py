import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import threading
from PIL import Image
import os
import cv2


class VideoCreatorApp:
    """
    A class representing a video creator application.

    This class provides a graphical user interface for creating videos by combining
    an audio file and an image file using FFmpeg. It allows the user to select the
    audio and image files, specify the output file name, and create the video.

    Attributes:
        root (tk.Tk): The root window of the application.
        audio_file (str): The path of the selected audio file.
        image_file (str): The path of the selected image file.

    Methods:
        __init__(self, root): Initializes the VideoCreatorApp instance.
        choose_audio_file(self): Opens a file dialog to choose an audio file.
        choose_image_file(self): Opens a file dialog to choose an image file.
        create_video(self): Creates a video by combining the audio and image files.
    """

    def __init__(self, root):
        """
        Initializes the VideoCreatorApp instance.

        Args:
            root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("Video Creator")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate position of window to center it
        position_top = int(screen_height / 2 - 500 / 2)
        position_right = int(screen_width / 2 - 500 / 2)

        # Set the geometry of the window
        root.geometry(f"500x500+{position_right}+{position_top}")

        self.audio_file_label = tk.Label(root, text="Seleziona file audio:")
        self.audio_file_label.pack(pady=10)

        self.audio_file_button = tk.Button(
            root, text="Sfoglia...", command=self.choose_audio_file
        )
        self.audio_file_button.pack()

        self.audio_file_selected_label = tk.Label(root, text="File selezionato:")
        self.audio_file_selected_label.pack()

        self.image_file_label = tk.Label(root, text="Seleziona immagine:")
        self.image_file_label.pack(pady=10)

        self.image_file_button = tk.Button(
            root, text="Sfoglia...", command=self.choose_image_file
        )
        self.image_file_button.pack()

        self.image_file_selected_label = tk.Label(root, text="File selezionato:")
        self.image_file_selected_label.pack()

        self.output_file_label = tk.Label(root, text="Nome del file di output:")
        self.output_file_label.pack(pady=10)

        self.output_file_entry = tk.Entry(root)
        self.output_file_entry.pack()

        self.create_button = tk.Button(
            root, text="Crea video", command=self.create_video
        )
        self.create_button.pack(pady=20)

        self.log_text = ScrolledText(root, height=10, width=60)
        self.log_text.insert(tk.END, "Welcome to Video Creation! \n")
        self.log_text.pack(pady=10)

    def choose_audio_file(self):
        """
        Opens a file dialog to choose an audio file.
        Updates the self.audio_file attribute with the selected file path.
        Updates the self.audio_file_selected_label with the selected file path.
        Inserts a log message indicating that an audio file has been selected.
        """
        self.audio_file = filedialog.askopenfilename(
            filetypes=[("Audio Files", "*.mp3 *.wav")]
        )
        self.audio_file_selected_label.config(
            text="File selezionato: " + self.audio_file
        )
        self.log_text.insert(tk.END, "Selected Audio.\n")

    def choose_image_file(self):
        """
        Opens a file dialog to choose an image file, rescales it to 1920x1080 pixels,
        and saves the rescaled image as "rescaled_img.png".
        """
        self.image_file = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )
        # Open the image file
        with Image.open(self.image_file) as img:
            # Read with CV2
            img = cv2.imread(self.image_file)
            # Resize the image 1920x1080 using INTERLANCZ0S4
            new_img = cv2.resize(img, (1920, 1080), interpolation=cv2.INTER_LANCZOS4)
            # Save img
            cv2.imwrite("rescaled_img.png", new_img)
        self.image_file = "rescaled_img.png"
        self.image_file_selected_label.config(
            text="File selezionato: " + self.image_file
        )
        self.log_text.insert(tk.END, "Rescaled Image.\n")

    def create_video(self):
        """
        Creates a video by combining an image file and an audio file using FFmpeg.
        The output video file is saved with the specified name or with a default name if not provided.
        """
        output_file = self.output_file_entry.get()
        if not output_file.endswith(".mp4"):
            output_file += ".mp4"

        ffmpeg_cmd = [
            "ffmpeg.exe",  # Add .exe extension for Windows version of ffmpeg
            "-hide_banner",  # Hides the FFmpeg header in the log
            "-loop",
            "1",
            "-pix_fmt",
            "yuv420p",  # Sets the pixel format to yuv420p
            "-i",
            self.image_file,
            "-i",
            self.audio_file,
            "-c:v",
            "mpeg4",  # Use the MPEG-4 video codec
            "-b:v",
            "2M",
            "-tune",
            "stillimage",
            "-c:a",
            "aac",
            "-strict",
            "experimental",
            "-b:a",
            "192k",
            "-shortest",
            "-y",  # Overwrites the output file if it already exists
            output_file,
        ]

        def run_ffmpeg_command():
            """
            Runs the FFmpeg command to create a video and convert it to MP4.

            This function executes the FFmpeg command specified by `ffmpeg_cmd` to create a video.
            It then checks if the output file was successfully created and displays appropriate messages.
            If the output file was created, it converts it to MP4 using the `converter_mp4.py` script.
            Finally, it deletes the rescaled image file and the original output file.

            Raises:
                Exception: If the output file was not created.

            Returns:
                None
            """
            try:
                process = subprocess.Popen(
                    ffmpeg_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                )
                self.log_text.insert(tk.END, "Creation in progress.\n")
                for line in process.stdout:
                    self.log_text.insert(tk.END, line)
                    
                process.wait()

                # Check if the output file was created
                if not os.path.isfile(output_file):
                    raise Exception("Output file was not created")

                self.log_text.insert(tk.END, "Creation completed.\n")
                self.log_text.insert(tk.END, "Converting to MP4.\n")
                # Convert the output file to MP4
                subprocess.call(["python", "converter_mp4.py", output_file])

                result_message = "Video creato con successo: " + output_file
                # Delete the rescaled image file
                if os.path.isfile(self.image_file):
                    os.remove(self.image_file)

                # Delete the output file (because it is already converted to MP4)
                if os.path.isfile(output_file):
                    os.remove(output_file)
            except Exception as e:
                result_message = "Errore durante la creazione del video: " + str(e)

            messagebox.showinfo("Risultato", result_message)

        thread = threading.Thread(target=run_ffmpeg_command)
        thread.setDaemon(True)
        thread.start()


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoCreatorApp(root)
    root.mainloop()
