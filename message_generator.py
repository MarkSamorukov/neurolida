import os
import random


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
        with open(f"{directory_path}/{filename}", 'r', encoding='utf-8') as file:
            phrases += file.read().split('\n')

    return delete_duplicate(phrases)

def message_genarator() -> str:
    phrases = get_phrases()
    return random.choice(phrases)
