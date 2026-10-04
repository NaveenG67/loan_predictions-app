import pandas as pd
from config.paths import DATA_PATH

def load_data():
    data = pd.read_csv(DATA_PATH/"loan-prediction.csv")
    return data

if __name__ == '__main__':
    data = load_data()
    print('Top 5 values:')
    print(data.head(),'\n','_'*60)
    print(data.shape,'\n','_'*60)
    print(data.isna().sum())