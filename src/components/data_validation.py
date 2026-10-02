import pandas as pd
from components.data_ingestion import load_data
def dataset_check(data: pd.DataFrame):
    '''
    performs basic dataset checks
    '''
    print('\n'+'*'*60)
    print('Dataset Overview'.center(60))
    print('*'*60)

    print(f'Shape: {data.shape}')
    print('\nShape of dataframe\n')
    print(data.shape)

    print('\nColumns of dataframe\n')
    print(data.columns.tolist())

    print('\nMissing values of dataframe\n')
    print(data.isnull().sum())

    print('\nDuplicate values in dataframe\n')
    print(data.duplicated().sum())

def main():
    data = load_data()
    dataset_check(data)

if __name__ == '__main__':
    main()

