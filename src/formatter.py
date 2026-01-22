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
    """
    Format translated sentences into the desired output format.

    :param title: Article title (used for image path resolution)
    :param sentences: Array of dictionaries where key is language code, value is the sentence.
                      Each dictionary contains the Russian translation and the original Polish sentence.
                      Example: [{'ru': 'hello', 'pl': 'cześć'}, {'ru': 'how are you?', 'pl': 'jak się masz?'}]
    :return: Formatted text where each Russian and Polish sentence pair is separated by a newline,
             and each pair is separated by an empty line.
    """
    print(f"Formatting text...")

    formatted_text = ''

    for sentence in sentences:
        if 'header' in sentence:
            formatted_text += f"{sentence['header']}\n"
        if 'footer' in sentence:
            formatted_text += f"\n{sentence['footer']}"
        if 'img' in sentence:
            image_url = get_html_tag_for_image(title, sentence['img'])
            formatted_text += f"\n{image_url}\n"
        if language == Language.RU:
            if 'ru' in sentence:
                formatted_text += f"{sentence['ru']} "  # TODO: handle space after newline character
        # elif language == Language.PL:
        #     if 'pl' in sentence:
        #         formatted_text += f"{sentence['pl']} "
        elif language == Language.RU_PL:
            if 'ru' in sentence and 'pl' in sentence:
                sentence_ru = remove_new_lines(sentence['ru'])
                sentence_pl = remove_new_lines(sentence['pl'])

                formatted_text += (f"{sentence_ru}"
                                   f"\n"
                                   f"{sentence_pl}"
                                   f"\n\n")

    print(f"Done.\n")

    return formatted_text
