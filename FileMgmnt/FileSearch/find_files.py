"""
find files that match a generic pattern defined in the constants
then hash the files and return a list of the fully qualified files
and hash values
"""
from  find_file_dialog_ui import Ui_WizardPage
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import codecs
import hashlib
import csv
import os

PICTURES = [".jpg", ".jpeg", ".bmp", ".mp4", ".3pg", ".png", ".heic"]
BATCH = [".bat", ".cmd", ".ps1"]
MOVIES = ["m4v", ".mp4", ".mpeg", ".vob", "qt", "avchd", "swf", ".mpg", ".mp2", ".mpe", ".mpv",
          ".flv", ".mov", ".3gp", ".avi", ".ifo", ".wmv", "m4p"]
AUDIO = [".mp3", ".au", ".cda", ".m4a", ".ogg", ".wma", ".wav"]
CSV_FILE = 'd:\\temp\\checksums_archive Photos.csv'
CSV_FILE = 'd:\\temp\\checksums_archive AllMusic3.csv'
SEARCH_PATH = 'K:\\Google photos\\takeout-20190412T201553Z-001\\Takeout\\Google Photos'
SEARCH_PATH = 'H:\\Source\\Python\\Data'


class file_selection_ui(QtWidgets.QMainWindow, Ui_WizardPage):
    """ provide a dialog to select files"""
    def __init__(self, parent = None):
        super(file_selection_ui, self).__init__(parent)
        self.setupUi(self)

        print(dir(self))
        self.quitBtn.clicked.connect(self.on_quitBtn_clicked)
        self.browseBtn.clicked.connect(self.browse_folder)
        QtCore.QMetaObject.connectSlotsByName(self)


    @QtCore.pyqtSlot()
    def on_quitBtn_clicked(self):
        sys.exit()

    def browse_folder(self):
        self.listWidget.clear()  # In case there are any existing elements in the list
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                               "Pick a folder")
        print(directory)
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

        if directory:  # if user didn't pick a directory don't continue
            # for all files, if any, in the directory
            for file_name in os.listdir(directory):
                # add file to the listWidget
                self.textBrowser.addItem(file_name)

def file_hash_hex(file_path, hash_func):
    """
    hash the fully qualified 'file_path'
    using the specified 'hash_func' (which is resolved at runtime)
    """
    digest = hash_func()
    with open(file_path, 'rb') as file_obj:
        while True:
            buf = file_obj.read(4096 * 4096)
            if not buf:
                break
            digest.update(buf)
    return digest.hexdigest()

    # return hash_func(f.read()).hexdigest()


def find_files(search_dir, file_pattern):
    """
    search from the specified search directory to
    find files that match the pattern list
    and return a list of fully qualified file names
    """
    file_count = 0
    matching_files = []
    for dir_path, _, files in os.walk(search_dir, topdown=False):
        for file in files:
            full_filename = os.path.join(dir_path, file)
            if os.path.isfile(full_filename):
                for pattern in file_pattern:
                    if full_filename.lower().endswith(pattern):
                        matching_files.append(full_filename)
                        file_count += 1
                        break
    print(f"File pattern {file_pattern} Files found = {file_count}")
    return matching_files

def Build_ui():
    app = QtWidgets.QApplication(sys.argv)
    WizardPage = QtWidgets.QWizardPage()
    ui = file_selection_ui()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())


def main():
    """ Main """
    start_time = datetime.now()
    Build_ui()
    files_found = []
    # files_found is a list of all files that match the search pattern
    files_found = find_files(SEARCH_PATH, AUDIO)
    # print(files_found.__len__(), sep='\n')
    with open(CSV_FILE, 'w') as file_obj:
        writer = csv.writer(file_obj, delimiter='\t', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        for file in files_found:
            file = codecs.encode(file, encoding='utf-8')
            writer.writerow((file, file_hash_hex(file, hashlib.md5)))
            # print(files_found.__len__(), file,
            #       file_hash_hex(file, hashlib.md5))
        etime = 'Time elpased (hh:mm:ss.ms) ' + str(datetime.now() -
                start_time) + ' for ' + str(files_found.__len__()) + ' files'
        writer.writerow(etime)
    print(
        f'Time elpased (hh:mm:ss.ms) {datetime.now()-start_time} for {files_found.__len__()} files')


if __name__ == "__main__":
    import sys
    main()

   


# strx = 'XyZ'
# stra = strx.lower()
# print(f"{stra}")

# import os
# for dir_path, _, files in os.walk("L:\\Optimus", topdown=False):
#     print([os.path.join(dir_path, file)
#            for path in dir_path for file in files if file.lower().endswith("exe")])

# files_found = ["0"]

# print(files_found.__len__(), sep='\n')
