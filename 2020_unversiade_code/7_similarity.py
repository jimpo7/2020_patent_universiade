import numpy as np
import pandas as pd
from gensim.models import Word2Vec
import gensim

#https://github.com/RaRe-Technologies/gensim/blob/3b9bb59dac0d55a1cd6ca8f984cead38b9cb0860/gensim/models/word2vec.py#L441 gensim word2vec

# nltk.download()
data = pd.read_excel('D:\\universiad\\realtry\\cn0511_realfinaldoc.xlsx',encoding='UTF-8',sep=",")
#data_df = data['발명의 명칭'].str.replace("[^a-zA-Z]" , " ") #특수문자 제거 
#data_df = data_df.apply(lambda x: ' '.join([w for w in x.split() if len(w)>3])) #단어길이 3미만 제거
#data_df = data_df.apply(lambda x: x.lower()) # 소문자 전환

#stop_words = stopwords.words('english')
#tokenized_data = data_df.apply(lambda x: x.split())
#tokenized_data = tokenized_data.apply(lambda x: [item for item in x if item not in stop_words]) # 불용어 제거
data_df= data['new_col']
data_df = np.array(data_df)
data2list = data_df.tolist()
#data2list = data_df.to_list()

veclist = []
for w in data2list:
    a = w.split()
    veclist.append(a)

print(veclist)

#dataarray = data.to_numpy()   
#new_df = pd.DataFrame(data})

model = Word2Vec(sentences = veclist , size = 300 , window = 2, min_count = 1 , workers = 4, sg = 1) # 데이터 학습 Skip-gram 사용
model.init_sims(replace=True)
model_name = 'model'
model.save(model_name)


similarity_matrix = []
index = gensim.similarities.MatrixSimilarity(gensim.matutils.Dense2Corpus(model.wv.syn0.T))
for sims in index:
    similarity_matrix.append(sims)
similarity_array = np.array(similarity_matrix)
similarity= pd.DataFrame(similarity_array)

index_ = model.wv.index2word
similarity.index = index_
similarity.columns = index_
print(similarity)
similarity.to_csv('',encoding='UTF-8')
