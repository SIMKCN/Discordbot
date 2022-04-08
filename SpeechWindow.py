from tkinter import *
from tkinter.filedialog import askopenfilename
import logging

logging.basicConfig(filename='Speechwindow.log', level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info("App started")
def datei():
    try:
        filename = askopenfilename()
        get_large_audio_transcription(filename)

    except NameError:
        logging.info("NO FILE CHOOSED")
def anleitung():
    root2 = Tk()
    root2.geometry("600x200")
    root2.title("Anleitung")
    frame = Frame(root2)
    frame.pack()
    logging.info("Anleitung geöffnet")
    sb = Scrollbar(frame, orient=HORIZONTAL)
    sb.pack(fill=X)
    lb = Listbox(frame, width=580, height=180, xscrollcommand=sb.set)
    lb.pack()

    lb.configure(xscrollcommand=sb.set)
    sb.config(command=lb.xview)

    lb.insert(0, "Anleitung")
    lb.insert(1, "Vorinformationen")
    lb.insert(2, "Achtung! Das Programm funktioniert nur mit .wav Datein!!!")
    lb.insert(3, "Sollten sie andere Audio Formate nutzen könnte es zu Problemen kommen.")
    lb.insert(4, "Das Programm benötigt eine Internetverbindung da es auf eine Datenbank zugreift.")
    lb.insert(5, "Der Transcripter arbeitet nicht 100% perfekt und hat Probleme mit Dialekten.")
    lb.insert(6, "Er kann nicht zwischen Stimmen unterscheiden.")
    lb.insert(7, "Nach Nutzung sollte der Text nochmal korrigiert werden.")
    lb.insert(8, "Dazu werden während des transkribieren Audio Chunks erstellt, jeweils versähen mit dem Namen des Chunks.")
    lb.insert(9, "Diese Chunks werden im selben Ordner in der sich auch das Programm befindet gespeichert.")
    lb.insert(10, "Zusätzlich wird der Text in der Datei ""Transscript.txt"" gespeichert welche auch im Ordner des Programms gespeichert wird.")
    lb.insert(11, "Dieses Script muss im Terminal ausgeführt werden")
    lb.insert(12, "Begriffserklärung:")
    lb.insert(13, "Error:Eine Stelle wo keine Sprache erkannt worden ist. (Kann bei langem Atmen o.ä auftreten)")

    root2.mainloop()

def close():
    logging.info("App closed")
    root.quit()
    
root = Tk()
root.title("PYTranscriptor")
root.geometry("180x180")
anleitungb = Button(root, text="Anleitung", command=anleitung)
close = Button(root, text="Close", command=close)
l1 = Label(root, text="Audio Datei:")
b1 = Button(root, text="Öffnen", command=datei)
b1.grid(row=1, column=2)
l1.grid(row=1, column=1)
close.grid(row=2, column=2)
anleitungb.grid(row=2, column=1)
root.mainloop()

