import os
import subprocess

from enum import Enum
from pathlib import Path

AUDIO_DIR = Path(__file__).parent.parent.parent / 'audio'

# Walk the audio directory to get files and dirs
audio_dict = {}
for dirname, dirnames, filenames in os.walk(AUDIO_DIR):
    path = Path(dirname)
    for dir in dirnames:
        audio_dict[dir] = []
    if path.stem in audio_dict:
        audio_dict.update({path.stem:filenames})


# Create enum classes out of audio_dict
_audio_enums_dict = {}
for k, v in audio_dict.items():
    # k is the new enum class
    # v are the enum attributes
    enum_name = k.upper()
    enum_dict = {}
    for sound in v:
        sound_name = sound.upper().split('.')[0]
        sound_path = AUDIO_DIR / k / sound
        enum_dict[sound_name] = sound_path
    _audio_enums_dict[enum_name] = Enum(enum_name, enum_dict)
AUDIO = type('AUDIO', (object,), _audio_enums_dict)


def play(sound_file):
    subprocess.Popen(f'aplay {sound_file}', shell=True)

play(AUDIO.FIRING.FIRING.value)