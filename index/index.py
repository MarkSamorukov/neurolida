from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from navec import Navec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pymorphy2
from russian_tagsets import converters

morph = pymorphy2.MorphAnalyzer()
stops = stopwords.words('russian')

df = pd.read_csv('texts/clean_texts.csv')
path = 'index/navec_hudlit_v1_12B_500K_300d_100q.tar'
navec_model = Navec.load(path)


def preprocess_text(text):
    lemmas = []
    for word in word_tokenize(text):
        if word.isalpha():
            word = morph.parse(word.lower())[0]
            lemma = word.normal_form
            lemmas.append(lemma)
    return ' '.join(lemmas)


def tag(word):
    ana = morph.parse(word)[0].tag.POS
    if ana is None:
        return word + '_' + 'X'
    else:
        to_ud = converters.converter('opencorpora-int', 'ud20')
        return word + '_' + to_ud(ana).split()[0]


def document_to_vector(doc):
    words = doc.split()
    word_vectors = []
    for word in words:
        tagged_word = word
        real_model = navec_model
        if tagged_word in real_model:
            word_vectors.append(real_model[tagged_word])
    if len(word_vectors) == 0:
        return None
    document_vector = sum(word_vectors) / len(word_vectors)
    return np.array(document_vector)


def index_navec(query_text):
    query_vector = document_to_vector(query_text).reshape(1, -1)
    matrix = []
    for doc in df['clean_text']:
        x = document_to_vector(doc)
        if x is not None:
            matrix.append(x)
    cosine_similarities = cosine_similarity(query_vector, matrix)
    sorted_indices = cosine_similarities.argsort()[0][::-1]

    return [(df['text'].iloc[i], cosine_similarities[0][i]) for i in sorted_indices[:5]]


def search(query):
    res = index_navec(query)
    return res
