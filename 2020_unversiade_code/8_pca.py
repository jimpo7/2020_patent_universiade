
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import seaborn as sns
import numpy as np

data= pd.read_excel('',encoding='UTF-8',sep=",")
df = data[['weighed_degree','count','betweeness_centrality']]
print(df)

#StandardScaler로 값 변환
scaler = StandardScaler()
# scaler=MinMaxScaler()
scaler.fit(df.values)
X_scaled = scaler.transform(df.values)
print(X_scaled.shape)
X_scaled = pd.DataFrame(X_scaled)
print(X_scaled)

#PCA modeling
pca=PCA(n_components=1)
pca.fit(X_scaled)

# data transform
X_pca = pca.transform(X_scaled)
print(pca.components_)
# print(X_scaled.shape)
# print(X_pca.shape)
# print1(X_pca)
# data['resultscore'] = X_scaled[0]*0.85184421 + X_scaled[1] * 0.36858082 + X_scaled[2]*0.37216881
data['resultscore'] = X_pca
print(data)


data.to_excel('',encoding='UTF-8')


