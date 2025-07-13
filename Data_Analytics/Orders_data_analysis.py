import kaggle
import pandas as pd
import os
from kaggle.api.kaggle_api_extended import KaggleApi


# Set API key manually (if not using .kaggle folder)
os.environ['KAGGLE_USERNAME'] = "nehadhakad"
os.environ['KAGGLE_KEY'] = "ec62f985b0f3cff658f2fa3fdd7c5928"

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Download dataset by name
api.dataset_download_files('ankitbansal06/retail-orders', path='./datasets', unzip=True)


df = pd.read_csv('./datasets/orders.csv')
#(df.head(20))

df['Ship Mode'].unique()

df = pd.read_csv('./datasets/orders.csv',na_values=('Not Available', 'unknown'))

df.columns = df.columns.str.lower()

df.columns=df.columns.str.replace(' ','_')

# print(df.head(5))

df['discount']=df['list_price']*df['discount_percent']/100

df['sale_price']=df['list_price']-df['discount']

df['profit']=df['sale_price']-df['cost_price']

print(df.dtypes)