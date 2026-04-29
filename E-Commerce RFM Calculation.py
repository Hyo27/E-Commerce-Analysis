'RFM Calculation'
import pandas as pd
import datetime as dt

# 1. 
df = pd.read_csv('ecommerce_cleaned.csv', encoding='unicode_escape')

# InvoiceDate date format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# analysis criteria date
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)


rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Recency (최근성)
    'InvoiceNo': 'count',                                   # Frequency (빈도)
    'TotalPrice': 'sum'                                     # Monetary (금액)
})

# column name change
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# 3. Scoring
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

# final score
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

# 4. 결과 저장
rfm.to_csv('rfm_result.csv')
print("✅ 2단계 성공: 'rfm_result.csv' 생성 완료!")
print(rfm.head())