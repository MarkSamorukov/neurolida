import os
import random
from index.index import search


def delete_duplicate(lst: list) -> list:
    res = []
    for item in lst:
        if item not in res:
            res.append(item)

    return res


def get_phrases() -> list[str]:
    phrases = []

    directory_path = 'texts'

    for filename in os.listdir(directory_path):
        if '.txt' in filename:
            with open(f"{directory_path}/{filename}", 'r', encoding='utf-8') as file:
                phrases += file.read().split('\n')

    return delete_duplicate(phrases)


def message_genarator(text, mode=0) -> str:
    if mode == 0:
        phrases = get_phrases()
        res = random.choice(phrases)
    elif mode == 1:
        res = search(text)

    return res
