import wave
import math
import struct

nom_fichier = "exemple.wav"
framerate = 44100
nchannels = 1
sampwith = 2
nframes = 44100
comptype = "NONE"
compname = "not compressed"
with wave.open(nom_fichier, "w") as fichier_audio:
    fichier_audio.setparams(
        (nchannels, sampwith, framerate, nframes, comptype, compname)
    )
    for i in range(nframes):
        valeur = int(32767.0 * math.sin(2.0 * math.pi * 440.0 * i / float(framerate)))
        fichier_audio.writeframes(struct.pack("<h", valeur))
