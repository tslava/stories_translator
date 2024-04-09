import json
from typing import Optional

from src.extractor import extract_text
from src.formatter import Language
from src.formatter import format_text
from src.splitter import split_into_sentences
from src.translator import translate_sentences
from src.utils import Stage
from src.utils import read_text_from_file
from src.utils import save_text_to_file


def run(stage: Stage, suffix: str, url: Optional[str] = None):
    if stage == Stage.EXTRACT:
        extracted_text = extract_text(url)
        save_text_to_file(suffix, stage, extracted_text)

        return

    if stage == Stage.TRANSLATE:
        extracted_text = read_text_from_file(suffix, stage)
        splitted_sentences = split_into_sentences(extracted_text)

        translated_sentences = translate_sentences(splitted_sentences)
        save_text_to_file(suffix, stage, translated_sentences)

        return

    if stage == Stage.FORMAT:
        translated_sentences = read_text_from_file(suffix, stage)

        try:
            translated_sentences = json.loads(translated_sentences)
        except json.JSONDecodeError:
            raise ValueError("The file with translation does not contain a valid JSON.")

        output_formatted_text_ru_pl = format_text(suffix, translated_sentences, Language.RU_PL)
        save_text_to_file(suffix, stage, output_formatted_text_ru_pl, lang_suffix=Language.RU_PL.value)

        output_formatted_text_ru = format_text(suffix, translated_sentences, Language.RU)
        save_text_to_file(suffix, stage, output_formatted_text_ru, lang_suffix=Language.RU.value)

        return


if __name__ == "__main__":
    url = "https://pomorska.pl/wieza-klimek-w-grudziadzu-nowa-atrakcja-regionu-wideo-zdjecia/ar/6472962"
    random_suffix = "Wieża_Klimek_w_Grudziądzu_2015"

    # run(stage=Stage.EXTRACT, suffix=random_suffix, url=url)
    # run(stage=Stage.TRANSLATE, suffix=random_suffix)
    run(stage=Stage.FORMAT, suffix=random_suffix)
