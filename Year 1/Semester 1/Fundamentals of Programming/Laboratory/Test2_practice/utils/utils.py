from copy import deepcopy


def gnome_sort(list_, key=None, reverse=False):
    def default_key(obj):
        return obj

    def compare(obj1, obj2):
        return obj1 < obj2

    new_list = deepcopy(list_)
    if key is None:
        key = default_key
    pos = 1
    while pos < len(new_list):
        if pos == 0 or not compare(key(new_list[pos]), key(new_list[pos - 1])):
            pos += 1
        else:
            new_list[pos - 1], new_list[pos] = new_list[pos], new_list[pos - 1]
            pos -= 1
    if reverse:
        i = 0
        j = len(new_list) - 1
        while i < j:
            new_list[i], new_list[j] = new_list[j], new_list[i]
            i += 1
            j -= 1
    return new_list
