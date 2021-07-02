from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

text = pd.read_excel('',encoding='UTF-8',sep=",")

textnoun = text['발명의 명칭']
# textnoun = text['요약']
# textnoun = text['Noun']

tfidf_vectorizer = TfidfVectorizer()

tfidf_vectorizer.fit(textnoun)

tfidf = sorted(tfidf_vectorizer.vocabulary_.items())
tfidf = pd.DataFrame(tfidf)
new_name = tfidf[0]

tfidf_vectorizer.idf_
hi= tfidf_vectorizer.transform(textnoun).toarray()

hi = pd.DataFrame(hi)
# hi.to_csv('',encoding='UTF-8')

textsum = pd.read_excel('',encodinging='UTF-8',sep=",")
print((textsum))
textsum = textsum.loc[3117]
textsum = textsum.T
print(textsum)
textsum = textsum.iloc[1:2608]
textsum = textsum.to_frame()
textsum.rename(index = new_name, inplace = True)
print(textsum)
textsum = textsum.sort_values(textsum.columns[0],ascending=False)
textsum.columns=["tfidf"]

textresult = textsum[textsum['tfidf'] >=  4.989093267]
textexcept = textsum[textsum['tfidf'] <  4.989093267]
print(textsum)
print(textresult)
print(textexcept)

textsum.to_csv('',encoding='UTF-8')
textresult.to_csv('',encoding='UTF-8')
textexcept.to_csv('',encoding='UTF-8')