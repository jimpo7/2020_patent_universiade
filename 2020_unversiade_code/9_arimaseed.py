import pandas as pd

data_= pd.read_excel('',encoding='UTF-8',sep=",")

#해당 단어가 들어있는 특허 뽑아오기 - 단어는 대회 알고리즘 중 하나이므로 숨김
blue = ['-','-','-','-','-','-','-','-']
yellow = ['-','-','-','-','-','-','-','-'] 
red = ['-','-','-','-','-','-','-']

data = data_['new_col']
for i in range(len(data)):
    data[i] = ' '.join("'{}'".format(word) for word in data[i].split(' '))
    

data = pd.DataFrame(data)
data['keycount']=0
data['Unnamed: 0'] = data_['Unnamed: 0']
print(data)
 
# 나라, 연도에 맞게 수정
for i in range(len(blue)):
    data['keycount'] += data.new_col.str.count(blue[i])
print(data)

data['count'] = data.new_col.str.count('')
data['score'] = data['keycount']/data['count']
print(data)

index = data[data.keycount >= 1]
index = index['Unnamed: 0']

print(index)
data['index'] = index
print(data)

# #key count 보고 싶으면 저장
data.to_excel('',encoding='utf-8-sig')


# # # 뽑아온 index를 이용하여 원본 특허의 내용들을 불러오기 위한 코드
# # # 나라, 연도에 맞게 수정
doc= pd.read_excel('',encoding='UTF-8',sep=",")
print(doc.shape)
print(doc)
doc_ = doc.iloc[index]
print(doc_)

doc_.to_excel('',encoding='utf-8-sig')