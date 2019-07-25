# from mutagen.mp3 import MP3
import mutagen.mp3


audio = MP3(
    "L:\\AllMusic3\\Bob Marley and The Wailers\\The Complete Wailers 1967-1972, Part 3\\2-17 Guava.mp3")
print(audio.info.length)
print(audio.info.bitrate)


mutagen.File(
    'L:\\AllMusic3\\Bob Marley and The Wailers\\The Complete Wailers 1967-1972, Part 3\\2-17 Guava.mp3')
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
