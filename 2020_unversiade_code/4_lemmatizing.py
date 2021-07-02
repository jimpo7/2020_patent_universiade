from nltk.stem import WordNetLemmatizer
import numpy as np
import pandas as pd
import re
import nltk
import csv
import openpyxl
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

data = pd.read_excel('',encoding='UTF-8',sep=",")
data = data[['발명의 명칭']]
# data = data[['요약']]
data.values

values = "".join(str(i) for i in data.values)
values

tokenized = word_tokenize(values)
no_capitals = str(tokenized).lower().split()

no_capitals

only_english = re.sub('[^a-zA-Z]',' ', str(no_capitals)).split() 
only_english

stops = set(stopwords.words('english'))
no_stops = [word for word in only_english if not word in stops]# 불용어제거

no_stops

lem = WordNetLemmatizer()

try_lemmatization = [lem.lemmatize(w) for w in no_stops] #표제어 추출

#print(no_capitals)
#print(try_lemmatization)
word_list = pd.Series(try_lemmatization)

result = word_list.value_counts() # 최종결과 빈도 체크 
print(result)
result.to_csv('',encoding='UTF-8')

# 단어 빈도수 tf-idf 교집합 dataframe 만드는 코드
result_ = result.to_frame().reset_index()
result_.columns = ["word","count"]

print(result_)

resultword= pd.read_csv('',encoding='UTF-8',low_memory=False)
resultword.columns = ["word","tfidf"]
print(resultword)
intersected_df = pd.merge(result_,resultword, how='inner')
print(intersected_df)
intersected_df.to_csv('',encoding='UTF-8')
