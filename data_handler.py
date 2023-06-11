import pandas as pd


def load_corpus():
    corpus = pd.read_json('data/corpus.jsonl', lines=True)
    return corpus
