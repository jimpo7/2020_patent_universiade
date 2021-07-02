import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA

doc = pd.read_excel('',encoding='UTF-8',sep=',')
# doc = doc.astype(np.float)
print(doc)
doc.rename(columns = {'Unnamed: 0' : 'year'}, inplace = True)
doc.rename(columns = {'출원일' : 'count'}, inplace = True)
print(doc)

# 전 꺼 확인용
average = doc['count'] 
   
doc['date'] = pd.to_datetime(doc.year, format='yyyy-MM')
doc = doc.set_index('date')
doc = doc[['count']]
print(doc)


# print(doc.info())
order = (2,1,1)
model = ARIMA(doc['count'],order)
fit = model.fit(trend='nc',full_output=True,disp=1)
average = sum(average)/len(average)*12
print(average)
# print(fit.summary())
# # # fit.plot_predict()
summ=fit.forecast(12)[0]
print(sum(summ))# # # # preds = fit.predict(1,30,typ='levels')
# # # # print(preds)

