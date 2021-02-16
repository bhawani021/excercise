import os
import csv
from os import walk
import hashlib
from datetime import datetime


def clone_repo(repo):
    """
    Read repo name and close rpository
    :param repo: str
    :return: None
    """
    cmd = "git clone {}".format(repo)
    print("running command -> {}".format(cmd))
    print("please wait ....")
    os.popen(cmd).read()
    print("Done repo clone")


def read_files(dir_path):
    """
    Read dir path and return all files in directory
    :param dir_path: str
    :return: list
    """
    _, _, filenames = next(walk(dir_path))
    return filenames


def get_hexa(file_path):
    """
    Return Sha256 hexdigest of the file
    :param file_path: str
    :return: str
    """
    with open(file_path, "rb") as f:
        byt = f.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(byt).hexdigest()
        return readable_hash


def get_words_from_file(file_path):
    """
    Returns number of words in a file
    :param file_path: str
    :return: list
    """
    file = open(file_path)
    data = file.read()
    words = data.split()
    return words


if __name__ == '__main__':
    # clone repo to get files
    repo_name = 'https://github.com/jimmyislive/sample-files.git'
    clone_repo(repo_name)

    # Get all files
    files = read_files('./sample-files')

    output = []
    for file_name in files:
        if file_name.startswith('README'):
            continue

        # file path
        file_path = './sample-files/{}'.format(file_name)

        # Sha256 hexdigest of the file
        hexa = get_hexa(file_path)

        # File size in bytes
        file_size = os.stat(file_path).st_size

        # word count
        words = get_words_from_file(file_path)
        total_words = len(words)

        # Number of unique words in this file
        unique_word_count = len(set(words))

        # Today's date
        dt = datetime.today().strftime('%Y-%m-%d')

        row = [file_name, hexa, file_size, total_words, unique_word_count, dt]

        output.append(row)

    # write to csv file
    output_file = 'interview.csv'
    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(output)
