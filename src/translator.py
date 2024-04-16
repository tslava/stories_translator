from typing import Dict
from typing import List

import requests
import json

from deepl import Formality
from deepl import SplitSentences
from deepl import Translator

from src.splitter import split_into_sentences

DEEPL_AUTH_KEY = "ac85b0d0-8563-45c4-87fc-616641063eb8:fx"


def translate_sentences(text: List[str]) -> List[Dict[str, str]]:
    '''
    :param text: массив предложений
    :return: массив словарей, где ключ - язык, значение - предложение.
    В каждом словаре содержится перевод исходного предложения на русский и оригинальное польское предложени
    '''
    print("Translating sentences...")

    translator = Translator(DEEPL_AUTH_KEY)
    translated_text = translator.translate_text(
        text=text,
        source_lang="PL",
        target_lang="RU",
        formality=Formality.MORE,
        # split_sentences=SplitSentences.ALL
    )

    translated_text = [
        {
            'ru': translation.text,
            'pl': sentence.rstrip()
        } for sentence, translation in zip(text, translated_text)]

    print(f"Done.\n")

    return translated_text


if __name__ == "__main__":
    # read text from file extracted_text.txt
    with open('extracted_text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        sentences = split_into_sentences(text)

    # translated_text = translate_sentences(text)
    translated_text = translate_sentences(sentences)
    print(json.dumps(translated_text, indent=4, ensure_ascii=False))
