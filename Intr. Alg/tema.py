import speech_recognition as sr
from pydub import AudioSegment

# Cargar el archivo MP3
audio_file_path = '/Users/Luciowo/Documents/Marsellaise.flp.mp3'
audio = AudioSegment.from_mp3(audio_file_path)

# Exportar a WAV
wav_file_path = '/Users/Luciowo/Documents/temp.wav'
audio.export(wav_file_path, format='wav')

# Inicializar el reconocedor
recognizer = sr.Recognizer()

# Cargar el archivo de audio para reconocimiento
with sr.AudioFile(wav_file_path) as source:
    audio_data = recognizer.record(source)

# Reconocer el discurso en el archivo de audio
try:
    text = recognizer.recognize_google(audio_data, language="es-ES")
    print("Texto reconocido:", text)
except sr.UnknownValueError:
    print("Lo siento, no pude entender el audio.")
except sr.RequestError as e:
    print(f"No se pudieron solicitar los resultados del servicio de reconocimiento de voz de Google; {e}")
