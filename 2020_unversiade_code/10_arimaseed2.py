# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 01:08:01 2020

@author: kyuri
"""

import pandas as pd

doc1 = pd.read_excel('D:\\universiad\\realtry\\arima\\cn0511_blue_patent.xlsx',encoding='UTF-8',sep=',')
doc2 = pd.read_excel('D:\\universiad\\realtry\\arima\\kr0311_blue_patent.xlsx',encoding='UTF-8',sep=',')
doc3 = pd.read_excel('D:\\universiad\\realtry\\arima\\jp0511_blue_patent.xlsx',encoding='UTF-8',sep=',')
doc4 = pd.read_excel('D:\\universiad\\realtry\\arima\\ep0511_blue_patent.xlsx',encoding='UTF-8',sep=',')
doc5 = pd.read_excel('D:\\universiad\\realtry\\arima\\us0511_blue_patent.xlsx',encoding='UTF-8',sep=',')
doc6 = pd.read_excel('D:\\universiad\\realtry\\arima\\cn1218_blue_patent.xlsx',encoding='UTF-8',sep=',')
doc7 = pd.read_excel('D:\\universiad\\realtry\\arima\\kr1218_blue_patent.xlsx',encoding='UTF-8',sep=',')
doc8 = pd.read_excel('D:\\universiad\\realtry\\arima\\jp1218_blue_patent.xlsx',encoding='UTF-8',sep=',')
doc9 = pd.read_excel('D:\\universiad\\realtry\\arima\\ep1218_blue_patent.xlsx',encoding='UTF-8',sep=',')
doc10 = pd.read_excel('D:\\universiad\\realtry\\arima\\us1218_blue_patent.xlsx',encoding='UTF-8',sep=',')

# doc1 = pd.read_excel('D:\\universiad\\realtry\\arima\\cn0511_yellow_patent.xlsx',encoding='UTF-8',sep=',')
# doc2 = pd.read_excel('D:\\universiad\\realtry\\arima\\kr0311_yellow_patent.xlsx',encoding='UTF-8',sep=',')
# doc3 = pd.read_excel('D:\\universiad\\realtry\\arima\\jp0511_yellow_patent.xlsx',encoding='UTF-8',sep=',')
# doc4 = pd.read_excel('D:\\universiad\\realtry\\arima\\ep0511_yellow_patent.xlsx',encoding='UTF-8',sep=',')
# doc5 = pd.read_excel('D:\\universiad\\realtry\\arima\\us0511_yellow_patent.xlsx',encoding='UTF-8',sep=',')
# doc6 = pd.read_excel('D:\\universiad\\realtry\\arima\\cn1218_yellow_patent.xlsx',encoding='UTF-8',sep=',')
# doc7 = pd.read_excel('D:\\universiad\\realtry\\arima\\kr1218_yellow_patent.xlsx',encoding='UTF-8',sep=',')
# doc8 = pd.read_excel('D:\\universiad\\realtry\\arima\\jp1218_yellow_patent.xlsx',encoding='UTF-8',sep=',')
# doc9 = pd.read_excel('D:\\universiad\\realtry\\arima\\ep1218_yellow_patent.xlsx',encoding='UTF-8',sep=',')
# doc10 = pd.read_excel('D:\\universiad\\realtry\\arima\\us1218_yellow_patent.xlsx',encoding='UTF-8',sep=',')

# doc1 = pd.read_excel('D:\\universiad\\realtry\\arima\\cn0511_red_patent.xlsx',encoding='UTF-8',sep=',')
# doc2 = pd.read_excel('D:\\universiad\\realtry\\arima\\kr0311_red_patent.xlsx',encoding='UTF-8',sep=',')
# doc3 = pd.read_excel('D:\\universiad\\realtry\\arima\\jp0511_red_patent.xlsx',encoding='UTF-8',sep=',')
# doc4 = pd.read_excel('D:\\universiad\\realtry\\arima\\ep0511_red_patent.xlsx',encoding='UTF-8',sep=',')
# doc5 = pd.read_excel('D:\\universiad\\realtry\\arima\\us0511_red_patent.xlsx',encoding='UTF-8',sep=',')
# doc6 = pd.read_excel('D:\\universiad\\realtry\\arima\\cn1218_red_patent.xlsx',encoding='UTF-8',sep=',')
# doc7 = pd.read_excel('D:\\universiad\\realtry\\arima\\kr1218_red_patent.xlsx',encoding='UTF-8',sep=',')
# doc8 = pd.read_excel('D:\\universiad\\realtry\\arima\\jp1218_red_patent.xlsx',encoding='UTF-8',sep=',')
# doc9 = pd.read_excel('D:\\universiad\\realtry\\arima\\ep1218_red_patent.xlsx',encoding='UTF-8',sep=',')
# doc10 = pd.read_excel('D:\\universiad\\realtry\\arima\\us1218_red_patent.xlsx',encoding='UTF-8',sep=',')

doc = pd.concat([doc1,doc2,doc3,doc4,doc5,doc6,doc7,doc8,doc9,doc10])
print(doc.columns)

doc['출원일'] = doc['출원일'].str[0:8]
print(doc['출원일'])

arimaseed = doc['출원일'].value_counts()
arimaseed = arimaseed.sort_index(ascending=True)
print(arimaseed)

arimaseed.to_excel('',encoding='utf-8-sig')

