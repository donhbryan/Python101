
from datetime import datetime
import glob
import logging
import sys
import os
from os.path import getsize


def print_movie_files(movie_directory, movie_extensions=['VOB', 'dat', 'mp4', 'mkv', 'vob']):
    ''' Print files in movie_directory with extensions in movie_extensions, recursively. '''

    # Get the absolute path of the movie_directory parameter
    movie_directory = os.path.abspath(movie_directory)

    # Get a list of files in movie_directory
    movie_directory_files = os.listdir(movie_directory)
    print_movie_files_counter = 0
    # Traverse through all files
    for filename in movie_directory_files:
        filepath = os.path.join(movie_directory, filename)

        # Check if it's a normal file or directory
        if os.path.isfile(filepath):

            # Check if the file has an extension of typical video files
            for movie_extension in movie_extensions:
                # Not a movie file, ignore
                if not filepath.endswith(movie_extension):
                    continue

                # We have got a video file! Increment the counter
                print_movie_files_counter += 1

                # Print it's name
                print('{0}'.format(filepath))
        elif os.path.isdir(filepath):
            # We got a directory, enter into it for further processing
            print_movie_files(filepath)
# def getsize(file_name):
#     return 1


def find_large_files(dir_list):
    # print_movie_files(search_path)
    logging.info(" start")
    for search_path in dir_list:
        for root, _, files in os.walk(search_path):
            file_size_sum = sum([getsize(os.path.join(root, name))
                                 for name in files if os.path.isfile(os.path.join(root, name))])
            if file_size_sum > 1000000000:
                print(format(file_size_sum, ','), end="\t")
                print(" bytes consumed by ", root, end="\t")
                print("in ", len(files), " non-directory files")
    logging.info(" done")


def whoami():
    logging.info("Now I'm there")


def foo():
    logging.info("I'm here")
    whoami()
    logging.info("I'm back here again")


def read_file(file_obj):
    try:
        with open(file_obj, "rb") as input_file:
            file_buff = input_file.read()
            return file_buff
    except OSError:
        print(f"OS Error: {sys.exc_info()[0]}")
        print("the file object is invalid: " + file_obj)
        logging.info(f" {file_obj} : {sys.exc_info()[0]}")
        return None
    else:
        print(input_file.name + " processed")


def write_file(file_obj, buff):
    try:
        with open(file_obj, "ab") as output_file:
            output_file.write(buff)
            return
    except OSError:
        print(f"OS Error: {sys.exc_info()[0]}")
        print("the file object is invalid: " + file_obj)
        logging.info(f" {file_obj} : {sys.exc_info()[0]}")
        return None
    else:
        print(output_file.name + " processed")


def append_files():
    buff = b''
    filenames = glob.glob("c:\\temp\\log*.txt")
    for each_file in filenames:
        buff += read_file(each_file)
    write_file(
        "c:\\temp\\"+datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", buff)
    print("done")


logging.basicConfig(
    filename='c:\\temp\\logger.txt', filemode='a',
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
    level=logging.INFO)
#
""" 
# foo()
# dir_list = ["m:\\"]  # "l:\\", "d:\\", "c:\\",
# find_large_files(dir_list)

# buff1 = (read_file("c:\\temp\\logger.txt"))
# buff2 = (read_file("c:\\temp\\logger2.txt"))
# buff3 = (read_file("c:\\temp\\logger3.txt"))
"""
