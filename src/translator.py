from typing import Dict
from typing import List

from openai import OpenAI

DEEPL_AUTH_KEY = "ac85b0d0-8563-45c4-87fc-616641063eb8:fx"

openai_client = OpenAI(
    api_key="sk-REDACTED",
)


def add_author_and_date(author: str, date: str, url: str) -> str:
    return (f"{author}\n"
            f"{date}\n"
            f"Перевёл на русский tslava. Оригинальная статья: {url}\n")


def add_footer() -> str:
    return "Telegram канал: https://t.me/polish_stories\nПрисоединяйтесь!"


def translate_sentences(
        text: List[str],
        url: str,
        autor: str,
        date: str,
        source_lang: str,
        translator_type: str = "chatgpt"
) -> List[Dict[str, str]]:
    '''
    :param text: массив предложений
    :return: массив словарей, где ключ - язык, значение - предложение.
    В каждом словаре содержится перевод исходного предложения на русский и оригинальное польское предложени
    '''
    print("Translating sentences...")

    translated_text = []

    for sentence in text:
        if translator_type == "chatgpt":
            translated_text.append(translate_sentence_with_openai_api(sentence, source_lang=source_lang))
        else:
            raise ValueError(f"Unknown translator type: {translator_type}")

    translated_text = [
        {
            'ru': translation,
            'pl': sentence.rstrip(),
        } for sentence, translation in zip(text, translated_text)]

    translated_text.insert(0, {
        "header": add_author_and_date(autor, date, url),
    })

    translated_text.append({
        "footer": add_footer(),
    })

    print(f"Done.\n")

    return translated_text


def translate_sentence_with_openai_api(sentence: str, source_lang: str = "polish") -> str:

    has_newline_at_the_end = sentence.endswith("\n")

    chat_completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": f"You are a translator from {source_lang.upper()} to Russian, preparing translations for those who are beginning to learn {source_lang.upper()}."},
            {"role": "user",
             "content": f"Translate the following {source_lang.upper()} sentence to Russian as close as possible, preserving the word order: {sentence}"}
        ],
        max_tokens=500,
        temperature=0.5
    )

    translated = chat_completion.choices[0].message.content.strip()

    if has_newline_at_the_end:
        translated = translated + "\n"

    return translated
