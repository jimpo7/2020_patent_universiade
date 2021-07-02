import pandas as pd

df= pd.read_csv('',encoding='CP949',low_memory=False)
df.shape

part = df['메인 IPC']

part=pd.DataFrame(part)
print(part)

# 4개로 짜른 것
#part['메인 IPC'] = part['메인 IPC'].apply(lambda e: e.split('-')[0])
#print(part)

#duplicate1 = part['메인 IPC'].value_counts()
#print(duplicate1)
#duplicate1.to_csv('')

# 3개로 자른 것
part['메인 IPC'] = part['메인 IPC'].str[0:3]
duplicate2 = part['메인 IPC'].value_counts()
print(duplicate2)
duplicate2.to_csv('')