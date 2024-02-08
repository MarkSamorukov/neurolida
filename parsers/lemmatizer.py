import pandas as pd
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pymorphy2

import csv

# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')

morph = pymorphy2.MorphAnalyzer()
stops = stopwords.words('russian')


def preprocess_text(text):
    lemmas = []
    for word in word_tokenize(text):
        if word.isalpha():
            word = morph.parse(word.lower())[0]
            lemma = word.normal_form
            lemmas.append(lemma)
    return ' '.join(lemmas)


clean_rows = []

directory_path = '../texts'

for filename in os.listdir(directory_path):
    with open(f'{directory_path}/{filename}', 'r', encoding='utf-8') as file:
        for row in file.readlines():
            if row.strip():
                preprocess_row = preprocess_text(row)
                if preprocess_row:
                    clean_rows.append({
                        'text': row.strip(),
                        'clean_text': preprocess_row.strip()
                    })

with open(f'../texts/clean_texts.csv', 'w', newline='\n', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['text', 'clean_text'])
    for text_dct in clean_rows:
        writer.writerow([text_dct['text'], text_dct['clean_text']])
