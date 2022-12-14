import re
from random import randint
def structure_string_is_valid(struct_str):
    if not re.match(r"^([dpw][1-9]\d*)+$",struct_str):
        return False
    return True
def structure_elements_list(struct_str):
    pairList=[]
    for match in re.findall(r"[dpw][1-9]\d*",struct_str):
        pairList.append((match[0],int(match[1:])))
    return pairList
def randstring(alphabet,n):
    return "".join([alphabet[randint(0,len(alphabet)-1)] for _ in range(n)])
def word_dict_get():
    word_dict=dict()
    with open("wordlist.txt") as stream:
        for line in stream.readlines():
            line=line[:-1]
            if len(line) in word_dict:
                word_dict[len(line)].append(line)
            else:
                word_dict[len(line)]=[line]
    return word_dict
print(word_dict_get())