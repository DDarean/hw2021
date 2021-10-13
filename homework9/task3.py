"""
Write a function that takes directory path, a file extension and
an optional tokenizer.

It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
universal_file_counter(test_dir, "txt")
6
universal_file_counter(test_dir, "txt", str.split)
6

"""
from os import path, walk


def return_files_list(directory, extension=''):
    files_list = []
    for address, _, files in list(walk(directory, topdown=True)):
        for file in files:
            if file.endswith(extension):
                files_list.append(path.join(address, file))
    return files_list


def universal_file_counter(dir_path, file_extension='', tokenizer=None):
    row_counter = 0
    files_list = return_files_list(dir_path, file_extension)
    for file in files_list:
        with open(file, 'r') as f:
            if tokenizer:
                row_counter += sum(len(tokenizer(line)) for line in f)
            else:
                row_counter += sum(1 for _ in f)
    return int(row_counter)
