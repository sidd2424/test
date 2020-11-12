import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# conf_path= 'C:\workspace\FileIO\'
# CONF_FILE= os.path.join(BASE_DIR, 'conf.json')
FILE_DIR = os.path.join(BASE_DIR, "FileIO")



TEXT_FILE_PATH = os.path.join(FILE_DIR, 'newFile.text')

if not os.path.exists(FILE_DIR):
    os.mkdir(FILE_DIR)
with open(TEXT_FILE_PATH, 'r') as _file:
    chunk_size = 10

    while True:
        data = _file.read(chunk_size)
        if len(data) <= 0:
            break

        print(data, end="")

# _TXT_FILE = os.path.join(FILE_DIR, 'new_copy_file.txt')

# with open(TXT_FILE_PATH, 'r') as read_file:
blank_file = os.path.join(FILE_DIR, 'blank_file.txt')

DATA = [
    ["This", "is", "my", "csv", "data"],
    ["This", "is", "my", "csv", "data"],
]

CSV_FILE_PATH = os.path.join(FILE_DIR, 'first_csv_file.csv')
with open(CSV_FILE_PATH, 'w') as _file:
    for data in DATA:
        _data ='.'.join(data)
        _file.write(_data)
        _file.write('\n')