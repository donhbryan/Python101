import os

HOME = os.path.expanduser("~")
ROOT_DIR = os.path.join(HOME, "TEST\\TF\\tf")
CMAKE_PATH = os.path.join(ROOT_DIR, "CMakeLists.txt")
CSV_FILE = 'TF.CSV'
# make target list


def make_target_list():
    target_tag = "set(TARGET_NAME"
    target_list = []
    for dirpath, _, files in os.walk(ROOT_DIR):
        if "CMakeLists.txt" in files:
            for file in files:
                CMAKE_PATH = os.path.join(dirpath, file)
                with open(CMAKE_PATH, 'r') as lines:
                    for line in lines:
                        if target_tag in line:
                            target = line[line.find(
                                target_tag)+len(target_tag)+1:line.find(")")]
                            target_list.append(target.strip('"'))
    return target_list

# writing csv


def write_csv(csv_line):
    import csv
    with open(CSV_FILE, 'w') as file_obj:
        w = csv.writer(file_obj, delimiter=',')
        w.writerow(csv_line)


if __name__ == '__main__':
    target = make_target_list()
    print(target)
    write_csv(target)
