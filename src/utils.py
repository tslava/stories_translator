import os
import json
from enum import Enum
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from src.formatter import Language


class Stage(Enum):
    EXTRACT = "extract"
    TRANSLATE = "translate"
    FORMAT = "format"


def create_dir_if_not_exists(dirname: str):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def save_text_to_file(
        title: str,
        stage: Stage,
        text: Union[str, List[Dict[str, str]]],
        lang_suffix: Optional[Language] = None,
) -> str:
    if stage == Stage.EXTRACT:
        output_filename = f'extracted_{title}.txt'
    elif stage == Stage.TRANSLATE:
        output_filename = f'translated_{title}.json'
        text = json.dumps(text, ensure_ascii=False, indent=4)
    elif stage == Stage.FORMAT:
        if lang_suffix is None:
            raise ValueError("Language suffix is required for the FORMAT stage.")

        output_filename = f'formatted_{title}_{lang_suffix}.txt'
    else:
        raise ValueError(f"Unhandled stage: {stage}")

    print(f"Saving text to a file {output_filename}...")

    create_dir_if_not_exists(os.path.join('generated', title))
    create_dir_if_not_exists(os.path.join('generated', title, 'images'))
    path = os.path.join('generated', title, output_filename)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Done.\n")

    return output_filename


def read_text_from_file(title: str, stage: Stage) -> str:
    if stage == Stage.TRANSLATE:
        filename = f'extracted_{title}.txt'
    elif stage == Stage.FORMAT:
        filename = f'translated_{title}.json'
    else:
        raise ValueError(f"Unhandled stage: {stage}")

    path = os.path.join('generated', title, filename)

    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    return text
