from enum import Enum
from typing import Dict
from typing import List


class Language(Enum):
    RU = 'RU'
    PL = 'PL'
    RU_PL = 'RU-PL'


def format_text(sentences: List[Dict[str, str]], language: Language):
    '''

    :param sentences: массив словарей, где ключ - язык, значение - предложение.
    В каждом словаре содержится перевод исходного предложения на русский и оригинальное польское предложени
    Пример: [{'ru': 'привет', 'pl': 'cześć'}, {'ru': 'как дела?', 'pl': 'jak się masz?'}]
    :return: Текст, в котором каждое предложение на русском и польском языке разделено переносом строки,
    и каждая пара предложений разделена пустой строкой
    '''
    print(f"Formatting text...")

    formatted_text = ''

    if language == Language.RU:
        for sentence in sentences:
            formatted_text += f"{sentence['ru']} "
    elif language == Language.PL:
        for sentence in sentences:
            formatted_text += f"{sentence['pl']} "
    elif language == Language.RU_PL:
        for sentence in sentences:
            formatted_text += f"{sentence['ru']}\n{sentence['pl']}\n\n"

    print(f"Done.\n")

    return formatted_text
