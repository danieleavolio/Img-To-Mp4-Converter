import subprocess

def create_video_with_audio(audio_file, image_file, output_file):
    ffmpeg_cmd = [
        'ffmpeg.exe',  # Aggiungi l'estensione .exe per la versione Windows di ffmpeg
        '-loop', '1',
        '-i', image_file,
        '-i', audio_file,
        '-c:v', 'libx264',
        '-tune', 'stillimage',
        '-vf', 'scale=1280:720',  # Modifica la risoluzione secondo le tue esigenze
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-b:a', '192k',
        '-shortest',
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Video creato con successo:", output_file)
    except subprocess.CalledProcessError as e:
        print("Errore durante la creazione del video:", e)

if __name__ == "__main__":
    audio_file = input("Inserisci il percorso del file audio: ")
    image_file = input("Inserisci il percorso dell'immagine: ")
    output_file = input("Inserisci il percorso del file di output (senza estensione): ")
    output_file += ".mp4"  # Aggiungi l'estensione .mp4 al percorso

    create_video_with_audio(audio_file, image_file, output_file)
