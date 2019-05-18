from datetime import datetime
import hashlib
import csv
import os

PICTURES = [".jpg", ".bmp"]
BATCH = [".bat", ".cmd", ".ps1"]
MOVIES = ["m4v", ".mp4", ".mpeg", ".vob", "qt", "avchd", "swf", ".mpg", ".mp2", ".mpe", ".mpv",
          ".flv", ".mov", ".3gp", ".avi", ".ifo", ".wmv", "m4p"]
AUDIO = [".mp3", ".au", ".cda", ".m4a", ".ogg", ".wma", ".wav"]
CSV_FILE = 'd:\\temp\\checksums_archive.csv'


def file_hash_hex(file_path, hash_func):
    startTime = datetime.now()

    digest = hash_func()
    with open(file_path, 'rb') as file_obj:
        while True:
            buf = file_obj .read(4096 * 4096)
            if not buf:
                break
            digest.update(buf)
    print(
        f'Time elpased (hh:mm:ss.ms) {datetime.now()-startTime}  for  {file_path}')
    return digest.hexdigest()

    # return hash_func(f.read()).hexdigest()


def FindFiles(search_dir, file_pattern):
    """
    search from the specified search directory to
    find files that match the pattern list
    and return a list of fully qualified file names
    """

    matching_files = []
    for dir_path, _, files in os.walk(search_dir, topdown=False):
        for file in files:
            full_filename = os.path.join(dir_path, file)
            if os.path.isfile(full_filename):
                for pattern in file_pattern:
                    if full_filename.lower().endswith(pattern):
                        matching_files.append(full_filename)
                        break
    return matching_files


def main():
    """ Main """

    files_found = []
    files_found = FindFiles("L:\\HandBrake Movies", MOVIES)
    #print(*files_found, sep='\n')
    with open(CSV_FILE, 'w') as file_obj:
        writer = csv.writer(file_obj, delimiter='\t', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        for file in files_found:
            writer.writerow((file, file_hash_hex(file, hashlib.md5)))


if __name__ == "__main__":
    main()

"""
strx = 'XyZ'
stra = strx.lower()
print(f"{stra}")
"""

"""
import os
for dir_path, _, files in os.walk("L:\\Optimus", topdown=False):
    print([os.path.join(dir_path, file)
           for path in dir_path for file in files if file.lower().endswith("exe")])
"""
