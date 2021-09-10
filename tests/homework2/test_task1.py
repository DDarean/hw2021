import os

import homework2.task1 as hw


file_path = os.path.join(os.getcwd(), 'data2.txt')

print(hw.get_longest_diverse_words(os.path.normpath(file_path)))
print(hw.get_rarest_char(os.path.normpath(file_path)))
print(hw.count_punctuation_chars(os.path.normpath(file_path)))
print(hw.count_non_ascii_chars(os.path.normpath(file_path)))
print(hw.get_most_common_non_ascii_char(os.path.normpath(file_path)))