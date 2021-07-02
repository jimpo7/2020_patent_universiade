#https://liveyourit.tistory.com/58 wordcloud 설치
#https://liveyourit.tistory.com/56 konlpy 설치
#https://foreverhappiness.me/30 csv 데이터 분류
#https://hwao-story.tistory.com/3 konlpy 사용
import sys
from konlpy.utils import pprint
from konlpy.tag import Okt

import pandas as pd

df= pd.read_csv('',encoding='UTF-8',low_memory=False)
print(df)

summary = df[['발명의 명칭']]
twit = Okt()
summary['token_review']=summary['발명의 명칭'].apply(twit.morphs)
summary['tagging']=summary['발명의 명칭'].apply(twit.pos)
summary['Noun']=summary['발명의 명칭'].apply(twit.nouns)

print(summary)
summary.to_csv('',encoding='utf-8-sig')