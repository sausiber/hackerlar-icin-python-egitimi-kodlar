import hashlib
import random


with open('/Users/kaantekiner/Desktop/hashes.txt', 'a') as the_file:

    my_string = "dashboard"
    the_file.write(hashlib.md5(my_string.encode('utf-8')).hexdigest())
    the_file.write("\n")

