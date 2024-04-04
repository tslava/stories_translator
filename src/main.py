from src.extractor import extract_text
from src.output_formatter import format_text
from src.splitter import split_into_sentences
from src.translator import translate_sentences
from src.utils import read_text_from_file
from src.utils import save_text_to_file


def run(source: str, extract: bool = True):
    '''

    :param source: имя файла или url
    :param extract: если True, то извлекаем текст из url, иначе читаем текст из файла
    :return:
    '''

    if extract:
        # extract text from url
        extracted_text = extract_text(source)
    else:
        # read text from file extracted_text.txt
        extracted_text = read_text_from_file(source)

    # split into sentences
    splitted_sentences = split_into_sentences(extracted_text)

    # translate sentences
    translated_sentences = translate_sentences(splitted_sentences)

    # format text
    output_formatted_text = format_text(translated_sentences)

    # save the formatted text to a file
    save_text_to_file('output', output_formatted_text)


def extract_only(url: str):
    # extract text from url
    _, filename = extract_text(url)

    return filename


if __name__ == "__main__":
    url = "https://podroze.onet.pl/aktualnosci/to-jedyny-taki-pingwin-na-swiecie-spotkacie-go-w-gdanskim-zoo/7cy0d2y"

    # full pipeline
    # run(source=url, extract=True)

    # partial pipeline
    # Step 1: extract text from url
    # filename = extract_only(url)
    # print(f"Extracted text saved to {filename}")

    # Step 2: run the pipeline without extraction
    filename = "url_extracted_text_6y2qq.txt"
    run(source=filename, extract=False)
