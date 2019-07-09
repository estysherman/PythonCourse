"""
Check password validation
"""
import re

#--------------- part 1 ---------------
def is_passphrase(text):
     m = re.search(r'\b(\w+)\b\s+.*\b\1\b', text)
     if m is None:
         return True
     else:
         return False


with open('I:\Ester Test Projects\exer1.txt') as fp:
    line = fp.readline()
    count = 0
    while line:
        if is_passphrase(line):
            count += 1
        line = fp.readline()

    print(f"Part 1: {count} passphrases are valid!!")
    #count = 383


#--------------- part 2 ---------------

def checkExistWord(list, m):
    sort = ''.join(sorted(m))
    if sort in list:
        return "###"
    else:
        list.append(sort)
        return m


with open('I:\Ester Test Projects\exer1.txt') as fp:
    line = fp.readline()
    count = 0
    while line:
        list = []
        line = re.sub(r"\b(\w+)\b", lambda m: checkExistWord(list, m.group(1)), line)

        isValid = re.search("###", line)
        if isValid is None:
            count += 1

        line = fp.readline()

    print(f"Part 2: {count} passphrases are valid!!")
    # count = 265



