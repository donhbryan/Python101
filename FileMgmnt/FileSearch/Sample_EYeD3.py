import eyed3

audiofile = eyed3.load(
    "C:\\Users\\db\\Python-Source\\Data\\1-16 Comma & Comma.mp3")
print(dir(audiofile))
print(audiofile.tag.artist)
print(audiofile.info)
print(audiofile.type)
print(audiofile.tag.version)
