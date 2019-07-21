"""
remove/modify any metadata that would contribute to the difference
between files. i.e. delete id3 tag so that audio content
can be compared
"""
# from mutagen.id3 import MutagenError
# import io  # BytesIO
# import os

# # from django.core.files import File

# from mutagen import File as MutaFile
# from mutagen.mp3 import MP3
# from mutagen.mp4 import MP4, MP4Cover, MP4Tags
# from mutagen.aiff import _IFFID3

# from mutagen.id3 import ID3NoHeaderError, ID3
# from mutagen.id3._frames import (APIC, TIT2, TPE1, TDRC, TALB, TPE2, TRCK, TBPM,

from __future__ import print_function
import eyed3
from eyed3.plugins import LoaderPlugin
#                                  TOPE, TKEY, TCOM, TEXT, COMM, TPE4, TPUB, TCON, USLT)

# eyed3.require((0, 7))


class Echo2Plugin(LoaderPlugin):
    SUMMARY = u"Displays details about audio files"
    NAMES = ["echo2"]

    def handleFile(self, f):
        super(Echo2Plugin, self).handleFile(f)

        if not self.audio_file:
            print("%s: Unsupported type" % f)
        else:
            print("Audio info: %s Metadata tag: %s " %
                  ("yes" if self.audio_file.info else "no",
                   "yes" if self.audio_file.tag else "no"))

files = {"D:\\Temp\\ANIMETAL\\Animetal Marathon\\29 ダンバインとぶ.mp3"}
x = Echo2Plugin(LoaderPlugin)
print (x.handleFile(files))
# def revert_metadata(files):
#     """
#     Removes all tags from a mp3 file
#     """
#     for file_path in files:
#         tags = EasyMP3(file_path)
#         # tags.delete()
#         # tags.save()
#         print([tag for tag in tags])


# revert_metadata(files)
