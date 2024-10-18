import json

import spacy
from spacy.language import Language


# spacy
def split_into_sentences(text):
    print("Splitting into sentences...")
    # before first run: python -m spacy download pl_core_news_sm
    # nlp = spacy.load('pl_core_news_sm')  # 50 mb
    nlp = spacy.load('pl_core_news_lg')  # 570 mb
    # nlp.enable_pipe("senter")

    @Language.component("set_custom_boundaries")
    def set_custom_boundaries(doc):
        for token in doc[:-1]:
            if token.text == "\n":
                doc[token.i + 1].is_sent_start = True
        return doc

    nlp.add_pipe("set_custom_boundaries", before="parser")

    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]

    print(f"Done.\n")
    return sentences


if __name__ == "__main__":
    # read text from file extracted_text.txt
    with open('extracted_text.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    sentences = split_into_sentences(text)
    print(json.dumps(sentences, indent=4, ensure_ascii=False))
