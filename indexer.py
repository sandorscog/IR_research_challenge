from data_handler import load_corpus
import pandas as pd
import pyterrier as pt


pt.init()
corpus = load_corpus()
print(corpus[:5])
pd_indexer = pt.DFIndexer('index/pd_index')

indexref = pd_indexer.index(corpus['text'], docno=corpus['id'])
