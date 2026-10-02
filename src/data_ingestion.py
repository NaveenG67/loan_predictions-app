import pandas as pd

def load_data():
    data = pd.read_csv("./Data/Raw/loan-prediction.csv")
    return data

if __name__ == '__main__':
    data = load_data()
    print('Top 5 values:')
    print(data.head(),'\n','_'*60)
    print(data.shape,'\n','_'*60)
    print(data.isna().sum())