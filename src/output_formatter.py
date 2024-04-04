from typing import Dict
from typing import List


def format_text(sentences: List[Dict[str, str]]):
    '''

    :param sentences: массив словарей, где ключ - язык, значение - предложение.
    В каждом словаре содержится перевод исходного предложения на русский и оригинальное польское предложени
    Пример: [{'ru': 'привет', 'pl': 'cześć'}, {'ru': 'как дела?', 'pl': 'jak się masz?'}]
    :return: Текст, в котором каждое предложение на русском и польском языке разделено переносом строки,
    и каждая пара предложений разделена пустой строкой
    '''
    print(f"Formatting text...")

    formatted_text = ''
    for sentence in sentences:
        formatted_text += f"{sentence['ru']}\n{sentence['pl']}\n\n"

    print(f"Done.\n")

    return formatted_text
