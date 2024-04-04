import json

import nltk
import pysbd
import spacy

from spacy.lang.pl import Polish


# spacy
def split_into_sentences(text):
    print("Splitting into sentences...")
    # before first run: python -m spacy download pl_core_news_sm
    # nlp = spacy.load('pl_core_news_sm')  # 50 mb
    nlp = spacy.load('pl_core_news_lg')  # 570 mb
    # nlp.enable_pipe("senter")
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]

    print(f"Done.\n")
    return sentences


# ntlk
# def split_into_sentences(text):
#     nltk.download('punkt')
#     sentences = nltk.tokenize.sent_tokenize(text, language='polish')
#     return sentences

# pysbd
# def split_into_sentences(text):
#     seg = pysbd.Segmenter(language="pl", clean=True)
#     res = seg.segment(text)
#     return res


if __name__ == "__main__":
    # read text from file extracted_text.txt
    with open('extracted_text.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    sentences = split_into_sentences(text)
    print(json.dumps(sentences, indent=4, ensure_ascii=False))
