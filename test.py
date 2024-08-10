# import numpy as np


def reverse(str):
    if (str == None or len(str) == 0):
        return str

    print("all-but-first chars:", str[1:])
    return reverse(str[1:]) + list(str[0])

names = ["Nancy", "Dave", "Dominic"]

for name in names:
    str_list = list(name)
    # print(str_list)
    result = reverse(name)
    print("=> word: ", name, "reverse: ", result)
    print()
