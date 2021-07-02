
import sys
#from wordcloud import WordCloud

from collections import Counter
import pandas as pd
import numpy as np

data = pd.read_excel('',encoding='UTF-8',sep=",")
print(data.columns)
data = data['word']
data_values = data.values
datalist=[]
datalist.append(data_values)
datalist=np.array(datalist)
print(datalist)
#listFrame =  pd.DataFrame(datalist)
df = pd.read_excel('',encoding='UTF-8',sep=",")
noun = df['Noun']

noun = df['Noun']
# noun = noun.str.replace("]","")
# noun = noun.str.replace("[","")
noun = noun.str.replace(",","")
noun = noun.str.replace("'","")

#print(noun)
nounlist = noun.values.tolist()

#print(nounlist[0])
# a = nounlist[0].split()
  
def intersection (list1, list2):
    
    temp = (list2)
    list3 = [value for value in list1 if value in temp]
    return list3

cleandata =[]
for i in nounlist:
    cleanlist = intersection(i.split(), datalist)
    #print(cleanlist)
    cleandata.append(cleanlist)

#print(cleandata)
    
cleanframe = pd.DataFrame(cleandata)

# cleanframe = cleanframe.T
# print(cleanframe)
#print(nounlist)
print(cleanframe)
cleandrop = cleanframe.dropna(how = 'all')
print(cleandrop)
# cleandrop.to_excel('',encoding='UTF-8')


#단어들을 줄글 문서로 합치는 코드

roottext = pd.DataFrame()
roottext['new_col'] = cleandrop.apply(lambda x: ' '.join(x.dropna().astype(str).values), axis=1)
print(roottext)

roottext.to_excel('',encoding='UTF-8')
