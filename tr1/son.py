# Ce script crée un fichier audio WAV contenant une onde sinusoïdale à 440 Hz (note La)

import wave  # Module pour manipuler des fichiers audio WAV
import math  # Module pour les fonctions mathématiques comme sin()
import struct  # Module pour convertir des nombres en format binaire

# Définition des paramètres du fichier audio
nom_fichier = (
    "C:/xampp/htdocs/prg/isamm/python/tr1/exemple.wav"  # Nom du fichier à créer
)
framerate = 44100  # Nombre d'échantillons par seconde (qualité audio)
nchannels = 1  # Nombre de canaux audio (1 = mono)
sampwith = 2  # Taille de chaque échantillon (2 octets = 16 bits)
nframes = 44100  # Nombre total d'échantillons (1 seconde de son)
comptype = "NONE"  # Type de compression (aucune)
compname = "not compressed"  # Description de la compression

# Création et configuration du fichier WAV
with wave.open(nom_fichier, "w") as fichier_audio:
    fichier_audio.setparams(
        (nchannels, sampwith, framerate, nframes, comptype, compname)
    )

    # Génération de l'onde sinusoïdale et écriture dans le fichier
    for i in range(nframes):
        # Calcul de la valeur de l'échantillon à partir d'une onde sinusoïdale à 440 Hz
        valeur = int(32767.0 * math.sin(2.0 * math.pi * 440.0 * i / float(framerate)))

        # Conversion de la valeur en format binaire et écriture dans le fichier
        fichier_audio.writeframes(struct.pack("<h", valeur))
