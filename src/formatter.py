import os
from enum import Enum
from typing import Dict
from typing import List

from src.uploader import upload_image


class Language(Enum):
    RU = 'RU'
    PL = 'PL'
    RU_PL = 'RU-PL'


def remove_new_lines(text: str) -> str:
    return text.replace('\n', '')


def get_html_tag_for_image(title: str, image_file_name: str) -> str:
    image_path = os.path.join('generated', title, 'images', image_file_name)
    image_url = upload_image(image_path)

    return image_url


def format_text(title: str, sentences: List[Dict[str, str]], language: Language):
    '''

    :param title:
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
            if 'ru' in sentence:
                formatted_text += f"{sentence['ru']} "  # TODO: сделать что-то с переносом пробела после символа переноа строки
            elif 'img' in sentence:
                image_url = get_html_tag_for_image(title, sentence['img'])
                formatted_text += f"\n{image_url}\n"
    elif language == Language.PL:
        for sentence in sentences:
            if 'pl' in sentence:
                formatted_text += f"{sentence['pl']} "
            elif 'img' in sentence:
                image_url = get_html_tag_for_image(title, sentence['img'])
                formatted_text += f"\n{image_url}\n"
    elif language == Language.RU_PL:
        for sentence in sentences:
            if 'ru' in sentence and 'pl' in sentence:
                sentence_ru = remove_new_lines(sentence['ru'])
                sentence_pl = remove_new_lines(sentence['pl'])

                formatted_text += (f"{sentence_ru}"
                                   f"\n"
                                   f"{sentence_pl}"
                                   f"\n\n")
            elif 'img' in sentence:
                image_url = get_html_tag_for_image(title, sentence['img'])
                formatted_text += f"{image_url}\n"

    # if language == Language.RU:
    #     formatted_text.replace('\n ', '\n')
    #     x=1

    print(f"Done.\n")

    return formatted_text
