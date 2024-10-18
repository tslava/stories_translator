import json
import os
from typing import Optional

from src.extractor import extract_text
from src.formatter import Language
from src.formatter import format_text
from src.splitter import split_into_sentences
from src.translator import translate_sentences
from src.utils import Stage
from src.utils import read_text_from_file
from src.utils import save_text_to_file


def get_article_title_from_url(url: str) -> str:
    return url.split("/")[-1].replace(".", "_")[:40]


def run(
        stage: Stage,
        title: str,
        url: Optional[str] = None,
        autor: Optional[str] = None,
        date: Optional[str] = None,
        source_lang: Optional[str] = 'polish'
):
    if stage == Stage.EXTRACT:
        extracted_text = extract_text(url)
        save_text_to_file(title, stage, extracted_text)

        return

    if stage == Stage.TRANSLATE:
        extracted_text = read_text_from_file(title, stage)
        splitted_sentences = split_into_sentences(extracted_text)

        translated_sentences = translate_sentences(splitted_sentences, url, autor, date, source_lang)
        save_text_to_file(title, stage, translated_sentences)

        return

    if stage == Stage.FORMAT:
        translated_sentences = read_text_from_file(title, stage)

        try:
            translated_sentences = json.loads(translated_sentences)
        except json.JSONDecodeError:
            raise ValueError("The file with translation does not contain a valid JSON.")

        output_formatted_text_ru_pl = format_text(title, translated_sentences, Language.RU_PL)
        save_text_to_file(title, stage, output_formatted_text_ru_pl, lang_suffix=Language.RU_PL.value)

        output_formatted_text_ru = format_text(title, translated_sentences, Language.RU)
        save_text_to_file(title, stage, output_formatted_text_ru, lang_suffix=Language.RU.value)

        return


if __name__ == "__main__":
    url = "https://www.trojmiasto.pl/moto/Kabrioletem-przewozil-plyty-gipsowe-n194722.html"
    number = 90
    date = "16 ноября 2024"
    autor = "Янэк Михалак (Janek Michalak)"

    # title = f"0{number}_{get_article_title_from_url(url)}"
    title = f"0{number}_kabrioletem_przewozil_plyty_gipsowe"

    source_lang = 'polish'

    if not os.path.exists(f"generated/{title}"):
        run(stage=Stage.EXTRACT, title=title, url=url, autor=autor, date=date)
    elif not os.path.exists(f"generated/{title}/translated_{title}.json"):
        run(stage=Stage.TRANSLATE, title=title, url=url, autor=autor, date=date, source_lang=source_lang)
    elif not os.path.exists(f"generated/{title}/formatted_{title}_RU-PL.txt"):
        run(stage=Stage.FORMAT, title=title)
    else:
        print("The text has been already extracted, translated and formatted.")
