def get_num_words(text):
    words = text.split()
    return len(words)


def get_uniq_char(text):
    uniq_list = {}
    for c in text:
        lowered = c.lower()
        if lowered in uniq_list:
            uniq_list[lowered] += 1
        else:
            uniq_list[lowered] = 1
    return uniq_list


def sort_on(items):
    return items["num"]


def get_sort_dict(my_dict):
    sorted_list = []
    for ch in my_dict:
        sorted_list.append({"char": ch, "num": my_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
