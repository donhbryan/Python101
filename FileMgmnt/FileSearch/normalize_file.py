"""
remove/modify any metadata that would contribute to the difference
between files. i.e. delete id3 tag so that audio content
can be compared
"""
import mutagen.id3


def revert_metadata(files):
    """
    Removes all tags from a mp3 file
    """
    for file_path in files:
        tags = EasyMP3(file_path)
        tags.delete()
        tags.save()


import io  # BytesIO
import os

from django.core.files import File

from mutagen import File as MutaFile
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4, MP4Cover, MP4Tags
from mutagen.aiff import _IFFID3

from mutagen.id3 import ID3NoHeaderError, ID3
from mutagen.id3._frames import (APIC, TIT2, TPE1, TDRC, TALB, TPE2, TRCK, TBPM,
                                 TOPE, TKEY, TCOM, TEXT, COMM, TPE4, TPUB, TCON, USLT)
