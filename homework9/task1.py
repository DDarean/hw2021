"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6
"""


def gen(num, file):
    with open(file, 'r') as f:
        for line in f:
            try:
                yield num, int(line.strip())
            except ValueError:
                continue


def merge_sorted_files(file_list):
    generators_list = [gen(num, file) for num, file in enumerate(file_list)]
    buffer = [next(generator) for generator in generators_list]
    sorted_list = []
    while buffer:
        gen_num, min_value = sorted(buffer, key=lambda x: x[1])[0]
        buffer = buffer[1:]
        sorted_list.append(min_value)
        try:
            buffer.append(next(generators_list[gen_num]))
        except StopIteration:
            continue
    return sorted_list
