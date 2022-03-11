from tkinter import *
from tkinterdnd2 import *
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pathlib import Path




r = sr.Recognizer()
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,

        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language="de-DE")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
                nonsens = " "
                datei = open("Transscript.txt", "a")
                datei.write("\r\n" + chunk_filename + nonsens + text)
                datei.close()
    # return the text for all chunks detected
    return whole_text

def show_text(event):
    print(event)
    fpath = Path(event).absolute()
    print(fpath)
    textarea.delete("1.0","end")
    if event.data.endswith(".wav"):
        get_large_audio_transcription(fpath)
        #with open(event.data, "r") as file:
         #   for line in file:
          #      line=line.strip()
           #     textarea.insert("end",f"{line}\n")

ws = TkinterDnD.Tk()
ws.title('PythonGuides')
ws.geometry('600x500')
ws.config(bg='#fcb103')

frame = Frame(ws)
frame.pack()

textarea = Text(frame, height=600, width=500)
textarea.pack(side=LEFT)
textarea.drop_target_register(DND_FILES)
textarea.dnd_bind('<<Drop>>', show_text)

sbv = Scrollbar(frame, orient=VERTICAL)
sbv.pack(side=RIGHT, fill=Y)

textarea.configure(yscrollcommand=sbv.set)
sbv.config(command=textarea.yview)



ws.mainloop()
