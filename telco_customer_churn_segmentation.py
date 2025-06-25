import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# load the telco dataset
raw_telco_customer = pd.read_csv(r'c:\Users\Hp\Desktop\my_first_project\mydata project\WA_Fn-UseC_-Telco-Customer-Churn.csv')
pd.set_option('display.max_rows', None)


# data cleaning
telco_customer = raw_telco_customer.copy()
telco_customer.dropna(inplace=True)

# select features for segmentation
telco_seg_feature = telco_customer[['tenure', 'PaymentMethod', 'MonthlyCharges', 'Contract']]

# encoding the selected categorical feature
contract_map = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
telco_seg_feature['Contract'] = telco_seg_feature['Contract'].map(contract_map)

payment_map = {'Electronic check': 0,'Mailed check': 1,'Bank transfer (automatic)': 2,'Credit card (automatic)': 3}
telco_seg_feature['PaymentMethod'] = telco_seg_feature['PaymentMethod'].map(payment_map)

# standardise the features
scale = StandardScaler()
scale_feature = scale.fit_transform(telco_seg_feature)

# Use Elbow Method to choose cluster number
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(scale_feature)
    wcss.append(kmeans.inertia_)

# Plot Elbow Curve
plt.figure(figsize=(8,5))
plt.plot(range(1,11), wcss, marker='o')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()


# cluster the related churn rate
kmeans_models = KMeans(n_clusters = 4,  random_state=42)
telco_seg_feature['segment'] = kmeans_models.fit_predict(scale_feature)

# save segment_value_count
segment_value_count = telco_seg_feature['segment'].value_counts()
segment_value_count.to_csv(r'c:\Users\Hp\Desktop\my_first_project\mydata project\segment_value_count.csv')

# save average_segment_feature
average_segment_feature = telco_seg_feature.groupby('segment')[['tenure', 'MonthlyCharges', 'Contract', 'PaymentMethod']].mean()
print(average_segment_feature)
average_segment_feature.to_csv(r'c:\Users\Hp\Desktop\my_first_project\mydata project\average_segment_feature.csv')

# Map segment labels to names and descriptions
segment_name_map = {
    0: 'Stable Value Seekers',
    1: 'Premium Loyalists',
    2: 'Churn-Prone Mid-Termers',
    3: 'High-Risk New Entrants'
}

segment_desc_map = {
    0: 'Long-term customers with moderate tenure and low charges, preferring stable payments and longer contracts.',
    1: 'Your most valuable, loyal customers with the longest tenure, highest charges, and long-term contract preference.',
    2: 'Mid-term customers with moderate to high charges, primarily on month-to-month contracts, indicating higher churn risk.',
    3: 'The newest, shortest-tenure customers with high charges and month-to-month contracts, making them highly susceptible to churn.'
}

# Add the new columns to the telco_customer
telco_customer['segment'] = telco_seg_feature['segment']
telco_customer['SegmentName'] = telco_customer['segment'].map(segment_name_map)
telco_customer['SegmentDescription'] = telco_customer['segment'].map(segment_desc_map)
print(telco_customer)

# save telco_customer_segmentation
telco_customer.to_csv(r'c:\Users\Hp\Desktop\my_first_project\mydata project\telco_customer_segmentation.csv')

# save churn_by_segment
churn_by_segment = telco_customer.groupby('segment')['Churn'].value_counts(normalize=True).unstack()
churn_by_segment.to_csv(r'c:\Users\Hp\Desktop\my_first_project\mydata project\churn_by_segment.csv')




