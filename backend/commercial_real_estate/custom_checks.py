# v.replace(" ", "") удаляет все пробелы (не удаляет символ пробела)
# re.sub(r'[^0-9.,]+', r'', string) удаляет всё кроме цифр, точки и запятой
# v = re.sub("\D", "", v) удаляет всё кроме цифр
# \s - Любой пробельный символ (пробел, табуляция, конец строки и т.п.)

import re


def is_int(v):
    v = re.sub("\s", "", v)
    try:
        v = int(v)
        return v
    except:
        return False


def is_float(v):
    v = re.sub(r'[^0-9.,]+', r'', v)
    try:
        v = float(v)
        return v
    except:
        return False


def is_list_int(v):
    # получает list со str (['3','4']),
    # проверяет что это list, преобразует значения в int,
    # если вместо int будет str, то не добавляет в конечный list
    new_list = []
    if type(v) == list:
        for item in v:
            try:
                i = int(item)
                new_list.append(i)

            except:
                continue
    else:
        return False
    return new_list


def is_str(v):
    if type(v) == str:
        return True
    else:
        return False


def is_list(v):
    if type(v) == list:
        return True
    else:
        return False


def is_bool(v):
    if type(v) == bool:
        return True
    else:
        return False
