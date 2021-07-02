import pandas as pd
import numpy as np
from collections import defaultdict

def co_occurrence(sentences, window_size):
    d = defaultdict(int)
    vocab = set()
    for text in sentences:
        # preprocessing (use tokenizer instead)
        text = text.lower().split()
        # iterate over sentences
        for i in range(len(text)):
            token = text[i]
            vocab.add(token)  # add to vocab
            next_token = text[i+1 : i+1+window_size]
            for t in next_token:
                key = tuple( sorted([t, token]) )
                d[key] += 1
                
                
    vocab = sorted(vocab) # sort vocab
    df = pd.DataFrame(data=np.zeros((len(vocab), len(vocab)), dtype=np.int16),
                          index=vocab,
                          columns=vocab)
    for key, value in d.items():
            df.at[key[0], key[1]] = value
            df.at[key[1], key[0]] = value
    return df

text= pd.read_excel('',encoding='UTF-8')
print(text)
#text = text.drop(columns=['word'])
docs = list(np.array(text['new_col'].tolist()))
df = co_occurrence(docs,2)
print(df)
df.to_csv('',encoding='utf-8-sig')