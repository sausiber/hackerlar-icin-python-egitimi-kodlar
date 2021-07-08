
import sys
import hashlib

def start():
    # /Users/kaantekiner/Desktop/hashes.txt
    # /Users/kaantekiner/Desktop/VmShare/wordlists/web_common.txt

    hash_list_path = sys.argv[1]
    with open(hash_list_path) as f:
        content = f.readlines()
    hashes = [x.strip() for x in content]

    wordlist_path = sys.argv[2]
    with open(wordlist_path) as f:
        for line in f:
            line = line.replace("\n", "")
            for hash in hashes:
                if hash == hashlib.md5(line.encode('utf-8')).hexdigest():
                    print("passwd found: " + hash + " : " + line)
print("script started....")
start()

